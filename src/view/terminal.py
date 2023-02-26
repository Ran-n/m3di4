#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:41:57.231414
#+ Editado:	2023/02/26 16:02:31.257577
# ------------------------------------------------------------------------------
#* Concrete Strategy (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.view import iView
# ------------------------------------------------------------------------------
import logging
from datetime import datetime
import validators as valid
import readline
from typing import List, Union, Callable

from src.enum import PaginationEnum
from src.utils import Config, center

from src.model.entity import Media, MediaGroup, MediaIssue
from src.model.entity import MediaType, MediaStatus
from src.model.entity import Platform, ShareSiteType, ShareSite
from src.model.entity import WarehouseType, Warehouse
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
        """
        """
        options = {
                '+'             :   [_('Save'), self.controller.save],
                '.'             :   [_('Exit'), self.controller.exit_save],
                '..'            :   [_('Exit (No Save)'), self.controller.exit_no_save],
                _('#members')   :   [_('Update Member Count'), self.controller.update_member_count],
                _('+mt')        :   [_('Add Media Type'), self.controller.add_media_type],
                _('+ms')        :   [_('Add Media Status'), self.controller.add_media_status],
                _('+m')         :   [_('Add Media'), self.controller.add_media],
                _('+mg')        :   [_('Add Media Group'), self.controller.add_media_group],
                _('+mi')        :   [_('Add Media Issue'), self.controller.add_media_issue],
                _('+p')         :   [_('Add Platform'), self.controller.add_platform],
                _('+st')        :   [_('Add ShareSiteType'), self.controller.add_sharesite_type],
                _('+s')         :   [_('Add ShareSite'), self.controller.add_sharesite],
                _('+wt')        :   [_('Add WarehouseType'), self.controller.add_warehouse_type],
                _('+w')         :   [_('Add Warehouse'), self.controller.add_warehouse],
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

        #for key, value in zip(options.keys(), options.values()):
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
        """
        """
        print()
        print(self.separator)
        text = f'{Config().title_symbol} ' + _('Searching for the values') + f' {Config().title_symbol}'
        print(center(text, self.line_len))
        print(self.separator)
        print()

    def __pick_from_options(self, message: dict[str, str], option_count: int, add_fn: Callable, get_opts_fn: Callable, limit: int = None, offset: int = 0) -> Union[MediaType, MediaStatus, Media]:
        """
            message
            {'title': 'a', 'pick': 'b', 'empty': 'c'}
        """

        # if not option exists, it starts the add option function
        while option_count == 0:
            logging.warning(message['empty'])
            print()
            print(f'{Config().error_symbol} {message["empty"]}')
            add_fn()
            option_count += 1

        # this variable allows the print to be smart and only reprint
        # and reask for the options if anyting was changed
        load_options = True
        # loop choice of option
        while True:
            if load_options:
                load_options = False

                lst_option = get_opts_fn(limit= limit, offset= offset)

                title = f'{Config().option_title_symbol} {message["title"]}'
                if limit: title += f' {len(lst_option) + offset}/{option_count}'
                print(title)

                for index, ele in enumerate(lst_option):
                    print(f'{index + offset + 1}. {ele.name}')
            choice = input(f'{Config().input_symbol} {message["pick"]}: ')

            # add new element
            if choice == Config().add_symbol:
                add_fn()
                option_count += 1
                load_options = True
            # move in pagination (limit = None | 0 will be false)
            elif limit and (choice in PaginationEnum.OPTIONS.value):
                choice_enum = PaginationEnum(choice)
                if (choice_enum == PaginationEnum.NEXT) and (option_count > offset + limit):
                    offset += limit
                    load_options = True
                elif (choice_enum == PaginationEnum.PREVIOUS) and (offset != 0):
                    offset -= limit
                    load_options = True
            # user selected something in the list
            elif choice.isdigit():
                choice = int(choice)
                if (choice > 0 and choice <= (len(lst_option) + offset)):
                    value = lst_option[choice - offset - 1]
                    break
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

    @staticmethod
    def __is_valid_date(date: str, date_format: str) -> bool:
        """
        """
        try:
            datetime.strptime(date, date_format)
        except:
            return False
        return True

    def __pick_date(self, message: str, date_format: str = '%Y-%m-%d', nullable: bool = False, equal_to: str = None, restrictions: List[List[str]] = None) -> str:
        """
        restrictions
            [['>=15', 'Is smaller than 15']]
        """
        date_formats = {
                '%Y'    :   'yyyy',
                '%m'    :   'mm',
                '%d'    :   'dd',
                '%H'    :   'hh',
                '%M'    :   'mm',
                '%S'    :   'ss',
        }

        date_format_ui = date_format
        for key, value in date_formats.items():
            date_format_ui = date_format_ui.replace(key, value)

        while True:
            date = input(f'{Config().input_symbol} {message} [{date_format_ui}]: ')

            if nullable and (date == ''):
                return None

            if (equal_to != None) and (date == Config().equal_symbol):
                return equal_to

            if self.__is_valid_date(date= date, date_format= date_format):
                if restrictions:
                    exit_ = True
                    for compare, error_msg in restrictions:
                        eval_value = True
                        try:
                            eval_value = eval(f'{int(date)}{compare}')
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


    def add_media_type(self) -> MediaType:
        """ Terminal View function for adding a media type element.
        @ Input:
        @ Output:
        ╚═  MediaType   -   The MediaType created by the user.
        """
        logging.info(_('Requesting the user for the information on the media type'))

        title = f'{2*Config().title_symbol} ' + _('Add Media Type') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added Media Type') + f' {2*Config().title_symbol}'
        print()
        print(self.separator)
        print(center(title, self.line_len))
        print(self.separator)

        while True:
            name = input(f'{Config().input_symbol} ' + _('Name') + ': ')
            if name != '':
                if len(self.model.get_by_name(MediaType.table_name, name)) == 0:
                    break
                print(f'{Config().error_symbol} ' + _('The given name is already in use'))

        groupable = self.__yn_question(_('Groupable?'))

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return MediaType(name = name, groupable = groupable)

    def add_media_status(self) -> MediaStatus:
        """ Terminal View function for adding a media status element.
        @ Input:
        @ Output:
        ╚═  MediaStatus   -   The MediaStatus created by the user.
        """
        logging.info(_('Requesting the user for the information on the media status'))

        title = f'{2*Config().title_symbol} ' + _('Add Media Status') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added Media Status') + f' {2*Config().title_symbol}'
        print()
        print(self.separator)
        print(center(title, self.line_len))
        print(self.separator)

        while True:
            name = input(f'{Config().input_symbol} ' + _('Name') + ': ')
            if name != '':
                if len(self.model.get_by_name(MediaStatus.table_name, name)) == 0:
                    break
                print(f'{Config().error_symbol} ' + _('The given name is already in use'))

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return MediaStatus(name= name)

    def add_media(self) -> Media:
        """ Terminal View function for adding a media element.
        @ Input:
        @ Output:
        ╚═  Media   -   The Media created by the user.
        """
        logging.info(_('Requesting the user for the information on the media'))

        title = f'{2*Config().title_symbol} ' + _('Add Media') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added Media') + f' {2*Config().title_symbol}'
        print()
        print(self.separator)
        print(center(title, self.line_len))
        print(self.separator)

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
        type_ = self.__pick_from_options(
                message     =   {
                    'title':    _('Types'),
                    'pick':     _('Type'),
                    'empty':    _('There are no media types available')
                },
                option_count    =   self.model.get_num(table_name= MediaType.table_name),
                add_fn          =   self.controller.add_media_type,
                get_opts_fn     =   lambda limit, offset: self.model.get_all(table_name= MediaType.table_name, limit= limit, offset= offset),
                limit           =   Config().pagination_limit
        )
        print()

        # status
        status = self.__pick_from_options(
                message     =   {
                    'title':    _('Statuses'),
                    'pick':     _('Status'),
                    'empty':    _('There are no media statuses available')
                },
                option_count    =   self.model.get_num(table_name= MediaStatus.table_name),
                add_fn          =   self.controller.add_media_status,
                get_opts_fn     =   lambda limit, offset: self.model.get_all(table_name= MediaStatus.table_name, limit= limit, offset= offset),
                limit           =   Config().pagination_limit
        )
        print()

        # year_start
        year_start = self.__pick_date(
                message     =   _('Start Year'),
                date_format =   '%Y',
                nullable    =   True
        )
        print()

        # year_end
        year_end = self.__pick_date(
                message         =   _('End Year'),
                date_format     =   '%Y',
                nullable        =   True,
                equal_to        =   year_start,
                restrictions    =   [
                    [f'>={year_start}', _(f'The end year must be equal or bigger than the start one ({year_start})')],
                ]
        )
        print()

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return Media(
                name        =   name,
                type_       =   type_,
                status      =   status,
                year_start  =   year_start,
                year_end    =   year_end
        )

    def add_media_group(self, id_media: int) -> MediaGroup:
        """ Terminal View function for adding a media group element.
        @ Input:
        ╚═  · id_media  -   int -   None
            └ The id of the media the group should be added to.
        @ Output:
        ╚═  MediaGroup  -   The MediaGroup created by the user.
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
                    option_count    =   self.model.get_num(table_name= Media.table_name),
                    add_fn          =   self.controller.add_media,
                    get_opts_fn     =   lambda limit, offset: self.model.get_all(table_name= Media.table_name, limit= limit, offset= offset),
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

            if not self.model.exists(MediaGroup(media= media, number= number)):
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

        # year_start
        year_start = self.__pick_date(
                message         =   _('Start Year'),
                date_format     =   '%Y',
                nullable        =   True,
                restrictions    =   [
                    [f'>={media.year_start}',   _(f'The start year must be equal or bigger than the start year of its Media ({media.year_start})')],
                    [f'<={media.year_end}',     _(f'The start year must be equal or smaller than the end year of its Media ({media.year_end})')]
                ]
        )
        print()

        # year_end
        year_end = self.__pick_date(
                message         =   _('End Year'),
                date_format     =   '%Y',
                nullable        =   True,
                equal_to        =   year_start,
                restrictions    =   [
                    [f'>={year_start}',         _(f'The end year must be equal or bigger than the start one ({year_start})')],
                    [f'>={media.year_start}',   _(f'The end year must be equal or bigger than the start year of its Media ({year_start})')],
                    [f'<={media.year_end}',     _(f'The end year must be equal or smaller than the end year of its Media ({media.year_end})')]
                ]
        )

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return MediaGroup(
                media       =   media,
                number      =   number,
                name        =   name,
                year_start  =   year_start,
                year_end    =   year_end
        )

    def add_media_issue(self) -> MediaIssue:
        """ Terminal View function for adding a media issue element.
        @ Input:
        @ Output:
        ╚═  MediaIssue  -   The MediaIssue created by the user.
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
                option_count    =   self.model.get_num(table_name= Media.table_name),
                add_fn          =   self.controller.add_media,
                get_opts_fn     =   lambda limit, offset: self.model.get_all(table_name= Media.table_name, limit= limit, offset= offset),
                limit           =   Config().pagination_limit
        )
        print()

        # media group
        media_group = self.__pick_from_options(
                message         =   {
                    'title':    _('Media Groups'),
                    'pick':     _('Media'),
                    'empty':    _('There are no media groups available')
                },
                option_count    =   self.model.get_media_group_num_by_media_id(media_id= media.id_),
                add_fn          =   lambda: self.controller.add_media_group(id_media= media.id_),
                get_opts_fn     =   lambda limit, offset: self.model.get_media_group_by_media_id(id_= media.id_, limit= limit, offset= offset),
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

            if not self.model.exists(MediaIssue(media= media, media_group= media_group, position= position)):
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

        return MediaIssue(
                position    =   position,
                media       =   media,
                media_group =   media_group,
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
            name = input(f'{Config().input_symbol} ' + _('Name') + ': ')
            if name != '':
                if self.model.exists(Platform(name= name)):
                    print(f'{Config().error_symbol} ' + _('The platform already exists, pick another name.'))
                else:
                    break
        #print()

        """
        # description
        desc = input(f'{Config().input_symbol} ' + _('Description') + ': ')
        if desc == '':
            desc = None
        print()
        """

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return Platform(
                name    =   name.capitalize()
        )

    def add_sharesite_type(self) -> ShareSiteType:
        """
        """
        logging.info(_('Requesting the user for the information on the ShareSiteType'))
        title = f'{2*Config().title_symbol} ' + _('Add ShareSiteType') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added ShareSiteType') + f' {2*Config().title_symbol}'
        print()
        print(self.separator)
        print(center(title, self.line_len))
        print(self.separator)

        # name
        while True:
            name = input(f'{Config().input_symbol} ' + _('Name') + ': ')
            if name != '':
                if self.model.exists(ShareSiteType(name=name)):
                    print(f'{Config().error_symbol} ' + _('It already exists, pick another name.'))
                else:
                    break

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return ShareSiteType(name=name)

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
        type_ = self.__pick_from_options(
                message     =   {
                    'title':    _('ShareSiteTypes'),
                    'pick':     _('ShareSiteType'),
                    'empty':    _('There are no ShareSiteTypes available')
                },
                option_count    =   self.model.get_num(table_name=ShareSiteType.table_name),
                add_fn          =   self.controller.add_sharesite_type,
                get_opts_fn     =   lambda limit, offset: self.model.get_all(table_name=ShareSiteType.table_name, limit=limit, offset=offset),
                limit           =   Config().pagination_limit
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
                get_opts_fn     =   lambda limit, offset: self.model.get_all(table_name=Platform.table_name, limit=limit, offset=offset),
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

    def add_warehouse_type(self) -> WarehouseType:
        logging.info(_('Requesting the user for the information on the WarehouseType'))
        title = f'{2*Config().title_symbol} ' + _('Add WarehouseType') + f' {2*Config().title_symbol}'
        ender = f'{2*Config().title_symbol} ' + _('Added WarehouseType') + f' {2*Config().title_symbol}'
        print()
        print(self.separator)
        print(center(title, self.line_len))
        print(self.separator)

        # name
        while True:
            name = input(f'{Config().input_symbol} ' + _('Name') + ': ')
            if name != '':
                if self.model.exists(WarehouseType(name=name)):
                    print(f'{Config().error_symbol} ' + _('It already exists, pick another name.'))
                else:
                    break

        print()
        print(self.separator)
        print(center(ender, self.line_len))
        print(self.separator)
        print()

        return WarehouseType(name=name)

    def add_warehouse(self) -> Warehouse:
        """
        """
        logging.info(_('Requesting the user for the information on the ShareSite'))
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
        type_ = self.__pick_from_options(
                message     =   {
                    'title':    _('WarehouseTypes'),
                    'pick':     _('WarehouseType'),
                    'empty':    _('There are no WarehouseTypes available')
                },
                option_count    =   self.model.get_num(table_name=WarehouseType.table_name),
                add_fn          =   self.controller.add_warehouse_type,
                get_opts_fn     =   lambda limit, offset: self.model.get_all(table_name=WarehouseType.table_name, limit=limit, offset=offset),
                limit           =   Config().pagination_limit
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

# ------------------------------------------------------------------------------
