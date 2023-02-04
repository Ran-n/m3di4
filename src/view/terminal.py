#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:41:57.231414
#+ Editado:	2023/02/04 19:41:39.473829
# ------------------------------------------------------------------------------
#* Concrete Strategy (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.view import iView
# ------------------------------------------------------------------------------
import logging
from typing import List, Union

from src.exception import NoMediaTypes, NoMediaStatuses
from src.model.entity import Media, MediaType, MediaStatus
# ------------------------------------------------------------------------------
class Terminal(iView):

    model = None

    def __init__(self) -> None:
        logging.info(_('Starting Terminal view'))

        print('----------------------------------------')
        print(_('Media4 Manager'))
        print('----------------------------------------')

    def menu(self, options: dict) -> int:
        print()
        print('*** '+_('MENU')+' ***')

        for key, value in zip(options.keys(), options.values()):
            print(f'{key}. {value[0]}')

        while True:
            option = input(_('Pick: '))
            if option in options:
                break

        print('*** '+_('MENU')+' ***')
        print()

        return option

    def exit(self) -> None:
        print('----------------------------------------')

    @staticmethod
    def __pick_from_options(message_title: str, message: str, options: List[Union[MediaType, MediaStatus]]) -> Union[MediaType, MediaStatus]:
        while True:
            print(f'< {message_title}')
            for index, ele in enumerate(options):
                print(f'{index}. {ele.name}')
            choice = input(f'> {message}: ')

            if choice.isdigit():
                choice = int(choice)
            else:
                continue

            if (choice >= 0 and choice <= len(options)-1):
                value = options[choice]
                break
        return value

    @staticmethod
    def __yn_question(message: str, as_str: bool = False) -> [str, int]:
        no_opts = ['n', 'no', 'non']
        str_answer = {0: _('No'), 1: _('Yes')}

        user_input = input(f'> {message}'+_(' [Y/n]')+': ')

        answer = 1  # yes by default
        if user_input.lower() in no_opts: answer = 0

        if as_str: return str_answer[answer]
        return answer


    def add_media_type(self) -> MediaType:
        logging.info(_('Requesting the user for the information on the media type'))
        print('** '+_('Add Media Type')+' **')

        while True:
            name = input('> '+_('Name')+': ')
            if len(self.model.get_by_name(MediaType.table_name, name)) == 0:
                break
            print('!! '+_('The given name is already in use'))

        groupable = self.__yn_question(_('Groupable?'))

        print('** '+_('Add Media Type')+' **')

        return MediaType(name = name, groupable = groupable)

    def add_media_status(self) -> MediaStatus:
        logging.info(_('Requesting the user for the information on the media status'))
        print('** '+_('Add Media Status')+' **')

        while True:
            name = input('> '+_('Name')+': ')
            if len(self.model.get_by_name(MediaStatus.table_name, name)) == 0:
                break
            print('!! '+_('The given name is already in use'))

        print('** '+_('Add Media Status')+' **')

        return MediaStatus(name= name)

    def add_media(self) -> Union[Media, NoMediaStatuses, NoMediaTypes]:
        logging.info(_('Requesting the user for the information on the media'))

        print('** '+_('Add Media')+' **')
        # name
        name = input('> '+_('Name')+': ')
        print()

        # type_
        type_options = self.model.get_all(MediaType.table_name)
        if len(type_options) == 0:
            logging.error(_('There are no media types available'))
            raise NoMediaTypes

        type_ = self.__pick_from_options(
                        message_title = _('Types'),
                        message = _('Type'),
                        options = type_options
        )
        print()

        # status
        status_options = self.model.get_all(MediaStatus.table_name)
        if len(status_options) == 0:
            logging.error(_('There are no media statuses available'))
            raise NoMediaStatuses

        status = self.__pick_from_options(
                        message_title = _('Statuses'),
                        message = _('Status'),
                        options = status_options
        )
        print()

        # year_start
        while True:
            year_start = input('> '+_('Start Year')+': ')
            if year_start.isdigit():
                break
        print()

        # year_end
        while True:
            year_end = input('> '+_('End Year')+': ')
            if year_end.isdigit():
                break
            elif year_end == '=':
                year_end = year_start
                break
        print('** '+_('Add Media')+' **')

        return Media(
                name = name,
                type_ = type_,
                status = status,
                year_start = year_start,
                year_end = year_end
        )

# ------------------------------------------------------------------------------
