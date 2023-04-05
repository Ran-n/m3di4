#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:41:57.231414
#+ Editado:	2023/03/28 22:15:34.603811
# ------------------------------------------------------------------------------
#* Concrete Strategy (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.view import iView
# ------------------------------------------------------------------------------
import logging
from datetime import datetime
import validators as valid
import readline
import os
from pathlib import Path
from dateutil.parser import parse
from typing import List, Union, Callable, Tuple

from src.enum import PaginationEnum
from src.utils import Config, center

from src.utils import AddFileTerminalViewOutput

from src.model.entity import Media, Group, Issue
from src.model.entity import Type, Status
from src.model.entity import Platform, ShareSite
from src.model.entity import Warehouse, MediaPlatform
# ------------------------------------------------------------------------------
class Terminal(iView):
    def __init__(self) -> None:
        logging.info(_('Starting Terminal view'))

        self.model = None
        self.controller = None

        self.line_len = None
        self.separator = None
        self.tab_len = 3

    def start(self) -> None:
        while True:
            self.__menu()

    def __menu(self) -> None:
        """"""
        options = {
                '+'             :   [_('Save'), self.controller.save],
                '.'             :   [_('Exit'), self.controller.exit_save],
                '..'            :   [_('Exit (No Save)'), self.controller.exit_no_save],
                _('#members')   :   [_('Update Member Count'), self.controller.update_member_count],
                _('#posters')   :   [_('Download posters'), self.controller.download_posters],
                _('+t')         :   [_('Add a Type'), self.controller.add_type],
                _('+s')         :   [_('Add a Status'), self.controller.add_status],
                _('+m')         :   [_('Add Media'), self.controller.add_media],
                _('+g')         :   [_('Add Group'), self.controller.add_group],
                _('+i')         :   [_('Add Issue'), self.controller.add_issue],
                _('+p')         :   [_('Add Platform'), self.controller.add_platform],
                _('+ss')        :   [_('Add ShareSite'), self.controller.add_sharesite],
                _('+w')         :   [_('Add Warehouse'), self.controller.add_warehouse],
                _('+mp')        :   [_('Add Media Platform'), self.controller.add_media_platform],
                _('+f')         :   [_('Add File'), self.controller.add_file],
        }

        try:
            options[self.__show_menu(options)][1]()
        except KeyboardInterrupt:
            print()
            print(self.separator)
            print()
            pass

    def __show_menu(self, options: dict) -> int:
        biggest_key_len = len(max(options.keys(), key=len)) + self.tab_len
        biggest_value_len = len(max([ele[0] for ele in options.values()], key=len)) + self.tab_len

        if not self.line_len:
            self.line_len = biggest_key_len + biggest_value_len + (self.tab_len*6)
            self.separator = Config().separator_symbol * (self.line_len + 2)

            print(self.separator)
            print(center(_('Media4 Manager'), self.line_len))
            print(self.separator)


        title = center(f'{Config().title_symbol*3} ' + _('MENU') + f' {Config().title_symbol*3}', self.line_len)
        print()
        print('█'+ '▀'*self.line_len +'█')
        print('█'+ title +'█')
        print('█'+ '▄'*self.line_len +'█')

        for key, value in options.items():
            value0 = value[0]
            print('▌'+center(f'\t{key:<{biggest_key_len}}\t\t▐\t\t{value0:<{biggest_value_len}}\t'.expandtabs(self.tab_len), self.line_len)+'▐')

        print('▀'*(self.line_len+2))
        while True:
            option = input(_('Pick: '))
            if option in options:
                break
        return option

    def save(self) -> None:
        print()
        print(self.separator)
        text = f'{Config().title_symbol} ' + _('The Database was saved') + f' {Config().title_symbol}'
        print(center(text, self.line_len))
        print(self.separator)
        print()

    def exit(self) -> None:
        print()
        print(self.separator)
        text = _('Goodbye!')
        print(center(text, self.line_len))
        print(self.separator)

    def update_member_count(self) -> None:
        """"""
        print()
        print(self.separator)
        text = f'{Config().title_symbol} ' + _('Searching for the values') + f' {Config().title_symbol}'
        print(center(text, self.line_len))
        print(self.separator)
        print()

    def download_posters(self) -> None:
        """"""
        print()
        print(self.separator)
        text = f'{Config().title_symbol} ' + _('Downloading the posters') + f' {Config().title_symbol}'
        print(center(text, self.line_len))
        print(self.separator)
        print()

    def __pick_from_options(self, message: dict[str, str], option_count: Union[int, Callable],
                            add_fn: Callable, get_opts_fn: Callable, limit: int = None,
                            offset: int = 0, show_all: bool = False) -> Union[Type, Status, Media]:
        """
            message
            {'title': 'a', 'pick': 'b', 'empty': 'c'}
        """

        original_limit = limit
        original_offset = offset

        option_count_fn = None
        if not isinstance(option_count, int):
            option_count_fn = option_count
            option_count = option_count()

        # if not option exists, it starts the add option function
        while option_count == 0:
            logging.warning(message['empty'])
            print(f'{Config().error_symbol} {message["empty"]}.')
            if self.__yn_question(_('Add new?')):
                add_fn()
                if option_count_fn:
                    option_count = option_count_fn()
                else:
                    option_count += 1
            else:
                print()
                break

        # this variable allows the print to be smart and only reprint
        # and reask for the options if anyting was changed
        load_options = True
        # loop choice of option
        while True:
            if load_options:
                load_options = False

                lst_option = get_opts_fn(limit=limit, offset=offset)

                title = f'{Config().option_title_symbol} {message["title"]}'
                if limit: title += f' {len(lst_option) + offset}/{option_count}'
                print(title)

                for index, ele in enumerate(lst_option):
                    print(f'{index + offset + 1}. {ele}')
            choice = input(f'{Config().input_symbol} {message["pick"]}: ')

            # add new element
            if choice == Config().add_symbol:
                add_fn()
                if option_count_fn:
                    option_count = option_count_fn()
                else:
                    option_count += 1
                load_options = True
            elif show_all and choice == Config().all_symbol:
                return None
            # move in pagination (limit = None | 0 will be false)
            elif limit and (choice in PaginationEnum.OPTIONS.value):
                choice_enum = PaginationEnum(choice)
                if (choice_enum == PaginationEnum.NEXT) and (len(lst_option) < option_count):
                    if (option_count > offset + limit):
                        offset += limit
                    else:
                        offset = 0
                        limit = original_limit
                    load_options = True
                elif (choice_enum == PaginationEnum.PREVIOUS) and (len(lst_option) < option_count):
                    if offset > 0:
                        offset -= limit
                    else:
                        limit = option_count
                        module = option_count % original_limit
                        if module == 0:
                            offset = option_count - original_limit
                        else:
                            offset = option_count - module

                    if offset < 0:
                        offset = 0
                        limit = original_limit
                    load_options = True
            # user selected something in the list
            elif choice.isdigit():
                choice = int(choice)
                if (choice > offset and choice <= (len(lst_option) + offset)):
                    value = lst_option[choice - offset - 1]
                    break
        return value

    def __pick_from_joined_options(self, message: dict[str, str], option_count: Union[int, Callable],
                            add_fn: Callable, get_opts_fn: Callable,
                            base_table: str, limit: int = None,
                            offset: int = 0) -> Union[Status, Media]:
        """When you want to use a joined table you may want to unjoin you use this function
        to call the pick_from_options one."""
        value = self.__pick_from_options(message=message, option_count=option_count,
                                        add_fn=add_fn, get_opts_fn=get_opts_fn,
                                        limit=limit, offset=offset, show_all=True)
        if value is None:
            print()
            option_count = lambda: self.model.get_num(table_name=base_table)
            get_opts_fn = lambda limit, offset: self.model.get_all(table_name=base_table,
                                                                   limit=limit, offset=offset)
            value = self.__pick_from_options(message=message, option_count=option_count,
                                            add_fn=add_fn, get_opts_fn=get_opts_fn,
                                             limit=limit, offset=offset)
        return value

    @staticmethod
    def __yn_question(message: str, as_str: bool = False) -> Union[str, int]:
        """ Return the answer of a yes/no question to the user.
        @ Input:
        ╠═  * message   -   str
        ║   └ What will the user see to indicate what to insert.
        ║
        ╚═  · as_str    -   bool    -   False
            └ Indicates if the return should be in str or int form.
        @ Output:
        ╚═  [str | int] -   The answer picked by the user.
        """
        no_opts = ['n', 'no', 'non']
        str_answer = {0: _('No'), 1: _('Yes')}

        user_input = input(f'{Config().input_symbol} {message}'+_(' [Y/n]')+': ')

        answer = 1  # yes by default
        if user_input.lower() in no_opts: answer = 0

        if as_str: return str_answer[answer]
        return answer

    @staticmethod
    def __pick_number(message: str, nullable: bool = False, equal_to: int = None, compare_msg: List[dict[str, str, str]] = None) -> int:
        """ Questions the user to pick a number, the number selected can be within a set a defined constraints.
        @ Input:
        ╠═  * message       -   str
        ║   └ What will the user see to indicate what to insert.
        ║
        ╠═  · nullable      -   bool                        -   False
        ║   └ Whether or not a number must be picked.
        ║
        ╠═  · equal_to      -   int                         -   None
        ║   └ What number will be used in case the user inputs the equal sign in the number picked.
        ║
        ╚═  · compare_msg   -   List[dict[str, str, str]]   -   None
            └ Example: [{'number'= '14', 'symbol'= '>', 'message'= 'The number must be bigger than 14'}].
              The first part will be evaluated, and if failed will show the second one to the user.
        @ Output:
        ╚═  int -   The number picked by the user.
        """
        while True:
            exit_ = False
            number = input(f'{Config().input_symbol} {message}: ')
            if nullable and number == '':
                number = None
                break
            elif number.isdigit():
                for ele in compare_msg:
                    if ele['number'] != None:
                        if eval(number + ele['symbol'] + ele['number']):
                            exit_ = True
                        else:
                            exit_ = False
                            print(f'{Config().error_symbol} '+ele['message'])
                            break

                if exit_:
                    break
            elif equal_to and number == Config().equal_symbol:
                number = equal_to
                break
        return number

    # this has high pctg of prob of going to a utils
    @staticmethod
    def __is_valid_date(date: str, date_format: str) -> bool:
        """"""
        try:
            datetime.strptime(date, date_format)
        except:
            return False
        return True

    def __pick_date(self, message: str, date_formats: List[str] = ['%Y-%m-%d'], nullable: bool = False, equal_to: str = None, restrictions: List[List[str]] = None) -> str:
        """
        restrictions
            [['>=15', 'Is smaller than 15']]
        """
        dict_date_formats = {
                '%Y'    :   'yyyy',
                '%m'    :   'mm',
                '%d'    :   'dd',
                '%H'    :   'hh',
                '%M'    :   'mm',
                '%S'    :   'ss',
        }

        date_format_ui = date_formats[0]
        for key, value in dict_date_formats.items():
            date_format_ui = date_format_ui.replace(key, value)

        while True:
            date = input(f'{Config().input_symbol} {message} [{date_format_ui}]: ')

            if nullable and (date == ''):
                return None

            if (equal_to != None) and (date == Config().equal_symbol):
                return equal_to

            if any([self.__is_valid_date(date=date, date_format=date_format) for date_format in date_formats]):
                if restrictions:
                    exit_ = True
                    for symbol, compare, error_msg in restrictions:
                        eval_value = True
                        try:
                            if symbol == '>':
                                eval_value = parse(date) > parse(compare)
                            elif symbol == '>=':
                                eval_value = parse(date) >= parse(compare)
                            elif symbol == '=' or symbol == '==':
                                eval_value = parse(date) == parse(compare)
                            elif symbol == '<':
                                eval_value = parse(date) < parse(compare)
                            elif symbol == '<=':
                                eval_value = parse(date) <= parse(compare)
                        except TypeError:
                            pass
                        if not eval_value:
                            exit_ = False
                            print(f'{Config().error_symbol} {error_msg}')
                            break
                    if exit_:
                        return date
                else:
                    return date
            else:
                print(f'{Config().error_symbol} ' + _('The date format is incorrect'))


    def add_type(self) -> Type:
        """ Terminal View function for adding a media type element.
        @ Input:
        @ Output:
        ╚═  Type   -   The Type created by the user.
        """
        logging.info(_('Requesting the user for the information on the media type'))

        title = f'{2*Config().title_symbol} ' + _('Add Type') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added Type') + f' {2*Config().title_symbol}'
        print()
        print(self.separator)
        print(center(title, self.line_len))
        print(self.separator)

        while True:
            name = input(f'{Config().input_symbol} ' + _('Name') + ': ')
            if name != '':
                if len(self.model.get_by_name(Type.table_name, name)) == 0:
                    break
                print(f'{Config().error_symbol} ' + _('The given name is already in use'))

        groupable = None
        if self.__yn_question(_('Is it a media type?')) == 1:
            groupable = self.__yn_question(_('Groupable?'))

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return Type(name=name, groupable=groupable)

    def add_status(self) -> Status:
        """ Terminal View function for adding a media status element.
        @ Input:
        @ Output:
        ╚═  Status   -   The Status created by the user.
        """
        logging.info(_('Requesting the user for the information on the media status'))

        title = f'{2*Config().title_symbol} ' + _('Add Status') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added Status') + f' {2*Config().title_symbol}'
        print()
        print(self.separator)
        print(center(title, self.line_len))
        print(self.separator)

        while True:
            name = input(f'{Config().input_symbol} ' + _('Name') + ': ')
            if name != '':
                if len(self.model.get_by_name(Status.table_name, name)) == 0:
                    break
                print(f'{Config().error_symbol} ' + _('The given name is already in use'))

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return Status(name= name)

    def add_media(self) -> Media:
        """ Terminal View function for adding a media element.
        @ Input:
        @ Output:
        ╚═  Media   -   The Media created by the user.
        """
        logging.info(_('Requesting the user for the information on the media'))

        title = f'{2*Config().title_symbol} ' + _('Add Media') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added Media') + f' {2*Config().title_symbol}'

        def start():
            print()
            print(self.separator)
            print(center(title, self.line_len))
            print(self.separator)

        def finish(added: bool = True):
            print()
            print(self.separator)
            if added:
                print(center(ender, self.line_len))
            else:
                print(center(title, self.line_len))
            print(self.separator)
            print()

        start()

        # name
        while True:
            name = input(f'{Config().input_symbol} ' + _('Name') + ': ')
            if name != '':
                break
        print()

        """
        # description
        description = input(f'{Config().input_symbol} ' + _('Description') + ': ')
        if description == '':
            description = None
        print()
        """

        # type_
        type_ = self.__pick_from_joined_options(
                message     =   {
                    'title':    _('Types'),
                    'pick':     _('Type'),
                    'empty':    _('There are no media types available')
                },
                option_count    =   lambda: self.model.get_num(table_name=(Type.table_name, Media.table_name)),
                add_fn          =   self.controller.add_type,
                get_opts_fn     =   lambda limit, offset: self.model.get_all(
                    table_name=(Type.table_name, Media.table_name), limit=limit, offset=offset),
                limit           =   Config().pagination_limit,
                base_table      = Type.table_name
        )
        print()

        # status
        status = self.__pick_from_options(
                message     =   {
                    'title':    _('Statuses'),
                    'pick':     _('Status'),
                    'empty':    _('There are no media statuses available')
                },
                option_count    =   self.model.get_num(table_name=Status.table_name),
                add_fn          =   self.controller.add_status,
                get_opts_fn     =   lambda limit, offset: self.model.get_all(
                    table_name=Status.table_name, limit=limit, offset=offset),
                limit           =   Config().pagination_limit
        )
        print()

        # date_start
        date_start = self.__pick_date(
                message         =   _('Start Date'),
                date_formats    =   ['%Y-%m-%d', '%Y'],
                nullable        =   True
        )
        print()

        if (self.model.exists(Media(name=name, type_=type_,
                                    status=status, date_start=date_start))):
            if self.__yn_question(_('The media already exists, retry?')):
                print()
                return self.add_media()
            else:
                finish(added=False)
                return None

        # date_end
        date_end = self.__pick_date(
                message         =   _('End Date'),
                date_formats    =   ['%Y-%m-%d', '%Y'],
                nullable        =   True,
                equal_to        =   date_start,
                restrictions    =   [
                    ['>=', date_start, _(f'The end date must be equal or bigger than the start one ({date_start})')],
                ]
        )
        print()

        finish()

        return Media(
                name        =   name,
                type_       =   type_,
                status      =   status,
                date_start  =   date_start,
                date_end    =   date_end
        )

    def add_group(self, id_media: int) -> Group:
        """ Terminal View function for adding a media group element.
        @ Input:
        ╚═  · id_media  -   int -   None
            └ The id of the media the group should be added to.
        @ Output:
        ╚═  Group  -   The Group created by the user.
        """
        logging.info(_('Requesting the user for the information on the media group'))

        title = f'{2*Config().title_symbol} ' + _('Add Media Group') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added Media Group') + f' {2*Config().title_symbol}'
        print()
        print(self.separator)
        print(center(title, self.line_len))
        print(self.separator)

        # media
        if id_media == None:
            media = self.__pick_from_options(
                    message     =   {
                        'title':    _('Medias'),
                        'pick':     _('Media'),
                        'empty':    _('There are no medias available')
                    },
                    option_count    =   self.model.get_num(table_name=Media.table_name),
                    add_fn          =   self.controller.add_media,
                    get_opts_fn     =   lambda limit, offset: self.model.get_all(
                        table_name=Media.table_name, limit=limit, offset=offset),
                    limit           =   Config().pagination_limit
            )
        else:
            media = self.model.get_by_id(table_name= Media.table_name, id_= id_media)
        print()

        # number
        while True:
            number = self.__pick_number(
                    message     =   _('Group Number'),
                    compare_msg =   [
                        {'symbol': '>=', 'number': '0', 'message': 'The group number must be bigger than 0'}
                    ]
            )

            if not self.model.exists(Group(media= media, number= number)):
                break
            else:
                logging.info(_('The requested media group to be added already exists, a number change will be adviced'))
                print(f'{Config().error_symbol} '+_('The Media Group already exists, pick another number.'))
        print()

        # name
        name = input(f'{Config().input_symbol} ' + _('Name') + ': ')
        if name == '':
            name = None
        print()

        """
        # description
        description = input(f'{Config().input_symbol} ' + _('Description') + ': ')
        if description == '':
            description = None
        print()
        """

        # date_start
        date_start = self.__pick_date(
                message         =   _('Start Date'),
                date_formats    =   ['%Y-%m-%d', '%Y'],
                nullable        =   True,
                restrictions    =   [
                    ['>=', media.date_start, _(f'The start date must be equal or bigger than the start date of its Media ({media.date_start})')],
                    ['<=', media.date_end, _(f'The start date must be equal or smaller than the end date of its Media ({media.date_end})')]
                ]
        )
        print()

        # date_end
        date_end = self.__pick_date(
                message         =   _('End Date'),
                date_formats    =   ['%Y-%m-%d', '%Y'],
                nullable        =   True,
                equal_to        =   date_start,
                restrictions    =   [
                    ['>=', date_start, _(f'The end date must be equal or bigger than the start one ({date_start})')],
                    ['>=', media.date_start, _(f'The end date must be equal or bigger than the start date of its Media ({date_start})')],
                    ['<=', media.date_end, _(f'The end date must be equal or smaller than the end date of its Media ({media.date_end})')]
                ]
        )

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return Group(
                media       =   media,
                number      =   number,
                name        =   name,
                date_start  =   date_start,
                date_end    =   date_end
        )

    def add_issue(self) -> Issue:
        """ Terminal View function for adding a media issue element.
        @ Input:
        @ Output:
        ╚═  Issue  -   The Issue created by the user.
        """
        logging.info(_('Requesting the user for the information on the media issue'))

        title = f'{2*Config().title_symbol} ' + _('Add Media Issue') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added Media Issue') + f' {2*Config().title_symbol}'
        print()
        print(self.separator)
        print(center(title, self.line_len))
        print(self.separator)

        # media
        media = self.__pick_from_options(
                message     =   {
                    'title':    _('Medias'),
                    'pick':     _('Media'),
                    'empty':    _('There are no medias available')
                },
                option_count    =   self.model.get_num(table_name=Media.table_name),
                add_fn          =   self.controller.add_media,
                get_opts_fn     =   lambda limit, offset: self.model.get_all(
                    table_name=Media.table_name, limit=limit, offset=offset),
                limit           =   Config().pagination_limit
        )
        print()

        # xFCR group is optional
        # media group
        group = self.__pick_from_options(
                message         =   {
                    'title':    _('Media Groups'),
                    'pick':     _('Media'),
                    'empty':    _('There are no media groups available')
                },
                option_count    =   self.model.get_group_num_by_media_id(media_id= media.id_),
                add_fn          =   lambda: self.controller.add_group(id_media= media.id_),
                get_opts_fn     =   lambda limit, offset: self.model.get_group_by_media_id(id_= media.id_, limit= limit, offset= offset),
                limit           =   Config().pagination_limit
        )
        print()


        # position
        while True:
            position = self.__pick_number(
                    message     =   _('Issue Number within the Group'),
                    compare_msg =   [
                        {'symbol': '>=', 'number': '0', 'message': 'The issue number must be bigger than 0'}
                    ]
            )

            if not self.model.exists(Issue(media= media, group= group, position= position)):
                break
            else:
                logging.info(_('The requested media issue to be added already exists, a number change will be adviced'))
                print(f'{Config().error_symbol} '+ _('The Media Issue already exists, pick another number.'))
        print()

        # name
        name = input(f'{Config().input_symbol} ' + _('Name') + ': ')
        if name == '':
            name = None
        print()

        """
        # description
        description = input(f'{Config().input_symbol} ' + _('Description') + ': ')
        if description == '':
            description = None
        print()
        """

        # xFCR restrictions media and group
        # date
        date = self.__pick_date(
                message     =   _('Date'),
                nullable    =   True
        )

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return Issue(
                position    =   position,
                media       =   media,
                group =   group,
                name        =   name,
                date        =   date
        )

    def add_platform(self) -> Platform:
        """ Terminal View function for adding a platform element.
        @ Input:
        @ Output:
        ╚═  Platform    -   The Platform created by the user.
        """
        logging.info(_('Requesting the user for the information on the platform'))

        title = f'{2*Config().title_symbol} ' + _('Add Platform') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added Platform') + f' {2*Config().title_symbol}'
        print()
        print(self.separator)
        print(center(title, self.line_len))
        print(self.separator)

        # name
        while True:
            name = input(f'{Config().input_symbol} ' + _('Name') + ': ').capitalize()
            if name != '':
                if self.model.exists(Platform(name= name)):
                    print(f'{Config().error_symbol} ' + _('The platform already exists, pick another name.'))
                else:
                    break
        print()

        # name_long
        name_long = input(f'{Config().input_symbol} ' + _('Long name') + ': ').capitalize()
        if name_long == '':
            name_long = None
        print()

        # acronym
        acronym = input(f'{Config().input_symbol} ' + _('Acronym') + ': ')
        print()

        # link
        while True:
            link = input(f'{Config().input_symbol} ' + _('Link') + ': ')
            if link != '' and valid.url(link):
                if not self.model.exists(ShareSite(name=name, type_=None, link=link)):
                    break
                else:
                    logging.info(_('The requested Platform to be added already exists, a link change will be adviced'))
                    print(f'{Config().error_symbol} '+_('The Platform already exists, pick another link.'))
        print()

        # type
        type_ = self.__pick_from_joined_options(
                message     =   {
                    'title':    _('Types'),
                    'pick':     _('Type'),
                    'empty':    _('There are no Types available')
                },
                option_count    =   lambda: self.model.get_num(table_name=(Type.table_name, Platform.table_name)),
                add_fn          =   self.controller.add_type,
                get_opts_fn     =   lambda limit, offset: self.model.get_all(
                    table_name=(Type.table_name, Platform.table_name), limit=limit, offset=offset),
                limit           =   Config().pagination_limit,
                base_table      = Type.table_name
        )
        print()

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return Platform(name=name, name_long=name_long,
                        acronym=acronym, link=link, type_=type_)

    def add_sharesite(self) -> ShareSite:
        """
        """
        logging.info(_('Requesting the user for the information on the ShareSite'))
        title = f'{2*Config().title_symbol} ' + _('Add ShareSite') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added ShareSite') + f' {2*Config().title_symbol}'
        print()
        print(self.separator)
        print(center(title, self.line_len))
        print(self.separator)

        # in_platform_id
        in_platform_id = input(f'{Config().input_symbol} ' + _('Identifier') + ': ')
        if in_platform_id == '':
            in_platform_id = None
        print()

        # name
        while True:
            name = input(f'{Config().input_symbol} ' + _('Name') + ': ')
            if name != '':
                break
        print()

        # link
        while True:
            link = input(f'{Config().input_symbol} ' + _('Link') + ': ')
            if link != '' and valid.url(link):
                if not self.model.exists(ShareSite(name=name, type_=None, link=link)):
                    break
                else:
                    logging.info(_('The requested ShareSite to be added already exists, a link change will be adviced'))
                    print(f'{Config().error_symbol} '+_('The ShareSite already exists, pick another link.'))
        print()

        # private
        private = self.__yn_question(_('Private?'))
        print()

        # type
        type_ = self.__pick_from_joined_options(
                message     =   {
                    'title':    _('Types'),
                    'pick':     _('Type'),
                    'empty':    _('There are no Types available')
                },
                option_count    =   lambda: self.model.get_num(table_name=(Type.table_name, ShareSite.table_name)),
                add_fn          =   self.controller.add_type,
                get_opts_fn     =   lambda limit, offset: self.model.get_all(
                    table_name=(Type.table_name, ShareSite.table_name), limit=limit, offset=offset),
                limit           =   Config().pagination_limit,
                base_table      = Type.table_name
        )
        print()

        # platform
        platform = self.__pick_from_options(
                message     =   {
                    'title':    _('Platforms'),
                    'pick':     _('Platform'),
                    'empty':    _('There are no Platforms available')
                },
                option_count    =   self.model.get_num(table_name=Platform.table_name),
                add_fn          =   self.controller.add_platform,
                get_opts_fn     =   lambda limit, offset: self.model.get_all(
                    table_name=Platform.table_name, limit=limit, offset=offset),
                limit           =   Config().pagination_limit
        )

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return ShareSite(
                in_platform_id  =   in_platform_id,
                name            =   name,
                private         =   private,
                link            =   link,
                type_           =   type_,
                platform        =   platform
        )

    def add_warehouse(self) -> Warehouse:
        """"""
        logging.info(_('Requesting the user for the information on the Warehouse'))
        title = f'{2*Config().title_symbol} ' + _('Add Warehouse') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added Warehouse') + f' {2*Config().title_symbol}'
        print()
        print(self.separator)
        print(center(title, self.line_len))
        print(self.separator)

        # name
        while True:
            name = input(f'{Config().input_symbol} ' + _('Name') + ': ')
            if name != '':
                if self.model.exists(Warehouse(name=name, type_=None)):
                    print(f'{Config().error_symbol} ' + _('It already exists, pick another name.'))
                else:
                    break
        print()

        # type
        type_ = self.__pick_from_joined_options(
                message     =   {
                    'title':    _('Types'),
                    'pick':     _('Type'),
                    'empty':    _('There are no Types available')
                },
                option_count    =   lambda: self.model.get_num(table_name=(Type.table_name, Warehouse.table_name)),
                add_fn          =   self.controller.add_type,
                get_opts_fn     =   lambda limit, offset: self.model.get_all(
                    table_name=(Type.table_name, Warehouse.table_name), limit=limit, offset=offset),
                limit           =   Config().pagination_limit,
                base_table      = Type.table_name
        )
        print()

        # size
        size = self.__pick_number(
                message     =   _('Size (B)'),
                nullable    =   True,
                compare_msg =   [
                    {'symbol': '>=', 'number': '0', 'message': 'The size number must be bigger than 0'}
                ]
        )
        print()

        # filled
        filled = self.__pick_number(
                message     =   _('Filled (B)'),
                nullable    =   True,
                compare_msg =   [
                    {'symbol': '>=', 'number': '0', 'message': 'The filled number must be bigger than 0'}
                ]
        )
        print()

        # content
        content = input(f'{Config().input_symbol} ' + _('Content') + ': ')
        if content == '':
            content = None
        print()

        # health
        health = input(f'{Config().input_symbol} ' + _('Health') + ': ')
        if health == '':
            health = None

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return Warehouse(name=name, type_=type_, size=size, filled=filled, content=content, health=health)

    def add_file(self) -> AddFileTerminalViewOutput:
        """"""
        def ask_original_name(original_names) -> None:
            """ Auxiliar function for asking the user the original filename."""
            # original name
            name = input(f'{Config().input_symbol} ' + _('Original filename') + ': ')
            if name == '':
                name = None
            original_names.append(name)

        logging.info(_('Requesting the user for the information on the File'))
        title = f'{2*Config().title_symbol} ' + _('Add File') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added File') + f' {2*Config().title_symbol}'
        print()
        print(self.separator)
        print(center(title, self.line_len))
        print(self.separator)


        # file path
        while True:
            file_path = os.path.expanduser(input(f'{Config().input_symbol} ' + _('File Path') + ': '))
            if os.path.exists(file_path):
                file_path = Path(file_path)
                break
            else:
                print(f'{Config().error_symbol} ' + _('The file doesnt exist.'))
        print()

        if file_path.is_dir():
            file_path = [file for file in file_path.glob('**/*') if file.is_file()]
        else:
            file_path = [file_path]

        is_media = self.__yn_question(message=_('Are you inserting a Media?'))
        print()

        original_names = []
        if is_media == 1:
            # warehouse
            warehouse = [self.__pick_from_options(
                    message     =   {
                        'title':    _('Warehouses'),
                        'pick':     _('Warehouse'),
                        'empty':    _('There are no Warehouses available')
                    },
                    option_count    =   self.model.get_num(table_name=Warehouse.table_name),
                    add_fn          =   self.controller.add_warehouse,
                    get_opts_fn     =   lambda limit, offset: self.model.get_all(
                        table_name=Warehouse.table_name, limit=limit, offset=offset),
                    limit           =   Config().pagination_limit
            )] * len(file_path)
            print()

            # media
            media = [self.__pick_from_options(
                    message     =   {
                        'title':    _('Medias'),
                        'pick':     _('Media'),
                        'empty':    _('There are no Medias available')
                    },
                    option_count    =   self.model.get_num(table_name=Media.table_name),
                    add_fn          =   self.controller.add_media,
                    get_opts_fn     =   lambda limit, offset: self.model.get_all(
                        table_name=Media.table_name, limit=limit, offset=offset),
                    limit           =   Config().pagination_limit
            )] * len(file_path)

            # original name
            for path in file_path:
                print()
                if len(file_path) > 1:
                    print(center(_('File')+f': "{path}"\n', self.line_len))
                ask_original_name(original_names)

            output_obj = AddFileTerminalViewOutput(original_names=original_names, file_paths=file_path,
                                                   warehouses=warehouse, medias=media)
        else:
            # if they are all in the same warehouse dont ask again for warehouse
            same_warehouse = self.__yn_question(message=_('Are all Issues in the same Warehouse?'))
            ask_for_warehouse = True
            issues = []
            warehouses = []
            for path in file_path:
                print()
                if not same_warehouse:
                    print(center(_('File')+f': "{path}"\n', self.line_len))

                if ask_for_warehouse:
                    if same_warehouse: ask_for_warehouse = False

                    # warehouse
                    warehouses.append(self.__pick_from_options(
                            message     =   {
                                'title':    _('Warehouses'),
                                'pick':     _('Warehouse'),
                                'empty':    _('There are no Warehouses available')
                            },
                            option_count    =   self.model.get_num(table_name=Warehouse.table_name),
                            add_fn          =   self.controller.add_warehouse,
                            get_opts_fn     =   lambda limit, offset: self.model.get_all(
                                table_name=Warehouse.table_name, limit=limit, offset=offset),
                            limit           =   Config().pagination_limit
                    ))
                    # if it wont ask for the warehouse again
                    if not ask_for_warehouse:
                        # fill the list of all the same warehouse
                        warehouses = [warehouses[0]] * len(file_path)
                    print()

                if same_warehouse:
                    print(center(_('File')+f': "{path}"\n', self.line_len))

                # media issue
                issues.append(self.__pick_from_options(
                        message     =   {
                            'title':    _('Issues'),
                            'pick':     _('Issue'),
                            'empty':    _('There are no Issues available')
                        },
                        option_count    =   self.model.get_num(table_name=Issue.table_name),
                        add_fn          =   self.controller.add_issue,
                        get_opts_fn     =   lambda limit, offset: self.model.get_all(
                            table_name=Issue.table_name, limit=limit, offset=offset),
                        limit           =   Config().pagination_limit
                ))
                print()

                # original name
                ask_original_name(original_names)

            output_obj = AddFileTerminalViewOutput(original_names=original_names, file_paths=file_path,
                                                   warehouses=warehouses, issues=issues)

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return output_obj

    def add_media_platform(self) -> MediaPlatform:
        """"""
        logging.info(_('Requesting the user for the information on the MediaPlatform'))
        title = f'{2*Config().title_symbol} ' + _('Add MediaPlatform') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added MediaPlatform') + f' {2*Config().title_symbol}'
        print()
        print(self.separator)
        print(center(title, self.line_len))
        print(self.separator)

        # media
        media = self.__pick_from_options(
                message = {'title': _('Medias'),
                          'pick': _('Media'),
                          'empty': _('There are no Types available')},
                option_count = lambda: self.model.get_num(table_name=Media.table_name),
                add_fn = self.controller.add_media,
                get_opts_fn = lambda limit, offset: self.model.get_all(
                    table_name=Media.table_name, limit=limit, offset=offset),
                limit = Config().pagination_limit
        )
        print()

        # platform
        platform = self.__pick_from_options(
                message = {'title': _('Platforms'),
                          'pick': _('Platform'),
                          'empty': _('There are no Platforms available')},
                option_count = lambda: self.model.get_num(table_name=Platform.table_name),
                add_fn = self.controller.add_platform,
                get_opts_fn = lambda limit, offset: self.model.get_all(
                    table_name=Platform.table_name, limit=limit, offset=offset),
                limit = Config().pagination_limit
        )
        print()

        # link
        while True:
            link = input(f'{Config().input_symbol} ' + _('Link') + ': ')
            if link != '' and valid.url(link) and link.startswith(platform.link):
                link = link[len(platform.link):]
                break
        print()

        # check if exits
        if self.model.exists(MediaPlatform(media=media, platform=platform, link=link)):
            print(_('It already exists'))
            return None

        # in_platform_id
        in_platform_id = input(f'{Config().input_symbol} ' + _('In platform id') + ': ')
        if in_platform_id == '':
            in_platform_id = None
        print()

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return MediaPlatform(media=media, platform=platform, link=link, in_platform_id=in_platform_id)

# ------------------------------------------------------------------------------
