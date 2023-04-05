#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/03/30 22:19:31.782560
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.model import iModel
# ------------------------------------------------------------------------------
from sqlite3 import Connection, Cursor
import logging
from typing import List, Union, Tuple


from src.exception import InheritException

from src.model.entity import Media, Group, Issue
from src.model.entity import Type, Status
from src.model.entity import Platform, ShareSite, ShareSiteSubs
from src.model.entity import Warehouse
from src.model.entity import Extension, Folder, App, Version, Encoder, File
from src.model.entity import Codec, Language, Track, TrackLanguage
from src.model.entity import LanguageCode, Poster, MediaPlatform
# ------------------------------------------------------------------------------
class Model:
    def __init__(self, strategy: iModel):
        # object must instance the interface
        if isinstance(strategy, iModel):
            self.model = strategy
        else:
            raise InheritException(_(f'Must inherit from {iModel.__name__}'))

    def get_conn_db(self) -> Connection:
        """ Returns a connection to the DB.
        @ Input:
        @ Output:
        ╚═ Connection   -   Connection object to the DB.
        """
        return self.model.get_conn_db()

    def get_cur_db(self) -> Cursor:
        """ Returns a cursor to the DB.
        @ Input:
        @ Output:
        ╚═ Cursor   -   Cursor object in the DB.
        """
        return self.model.get_cur_db()

    def connect_db(self) -> tuple([Connection, Cursor]):
        """ Does the whole process of connecting to a DB.
        @ Input:
        @ Ouput:
        ╚═ (Connection, Cursor) -   Tuple with objects of DB Connection and Cursor.
        """
        logging.info(_('Connecting to the database'))
        return self.model.connect_db()

    def disconnect_db(self, commit: bool = True) -> None:
        """ Does the whole process of disconnecting from a DB.
        @ Input:
        ╚═  · commit -   bool    -   True
            └ Indicates if changes to the DB should be commited or rolled back.
        @ Output:
        """
        logging.info(_('Disconnecting from the database'))
        return self.model.disconnect_db(commit)

    def save_db(self) -> None:
        """ Saves the non commited changes to the DB.
        @ Input:
        @ Output:
        """
        logging.info(_('Saving the databse'))
        return self.model.save_db()


    # EXISTS
    def exists(self, obj: Union[Group, Issue, Platform,
            Type, ShareSite, Warehouse, Extension,
            LanguageCode, Media, MediaPlatform, Poster]) -> bool:
        """ Checks if a element is saved in the DB.
        @ Input:
        ╚═  · obj   -   Any Entity Object   -   True
            └ Object to check if it exists in the DB.
        @ Output:
        ╚═  bool    -   Indicating if the object exists or not.
        """
        logging.info(_(f'Checking on table "{obj.table_name}" if the information already exists'))

        if isinstance(obj, Group):
            return self.model.exists_group(obj)
        elif isinstance(obj, Issue):
            return self.model.exists_issue(obj)
        elif isinstance(obj, Platform):
            return self.model.exists_platform(obj)
        elif isinstance(obj, Type):
            return self.model.exists_type(obj)
        elif isinstance(obj, ShareSite):
            return self.model.exists_sharesite(obj)
        elif isinstance(obj, ShareSiteSubs):
            return self.model.exists_sharesite_subs(obj)
        elif isinstance(obj, Warehouse):
            return self.model.exists_warehouse(obj)
        elif isinstance(obj, Extension):
            return self.model.exists_extension(obj)
        elif isinstance(obj, LanguageCode):
            return self.model.exists_language_code(obj)
        elif isinstance(obj, Media):
            return self.model.exists_media(obj)
        elif isinstance(obj, MediaPlatform):
            return self.model.exists_media_platform(obj)
        elif isinstance(obj, Poster):
            return self.model.exists_poster(obj)
    # EXISTS #

    # GET NUM
    def get_num(self, table_name: Union[str, Tuple[str, str]]) -> int:
        """ Returns the number of elements in a table.
        @ Input:
        ╚═  · table_name    -   str, Tuple[str]
            └ Name/s of the table to query.
        @ Output:
        ╚═  int - Number of entries on the table/s.
        """
        if isinstance(table_name, tuple):
            logging.info(_(f'''Counting the number of elements saved on the joined
                           tables "{'" & "'.join(table_name)}"'''))
            return self.model.get_num_type_of_x(table_name[1])
        else:
            logging.info(_(f'Counting the number of elements saved on table "{table_name}"'))
            return self.model.get_num(table_name)

    def get_group_num_by_media_id(self, media_id: int) -> int:
        """Returns the number of group elements discriminating by media id.
        @ Input:
        ╚═  · media_id  -   int
            └ Id of the media to use as a discriminator.
        @ Output:
        ╚═  int - Number of entries on the table that meet the criteria.
        """
        logging.info(_(f'Counting the number of elements saved on table "{Group.table_name}" using the media id "{media_id}"'))
        return self.model.get_group_num_by_media_id(media_id)
    # GET NUM #

    # GET ALL
    def get_all(self, table_name: Union[str, Tuple[str, str]], limit: int = None,
                offset: int = 0, alfabetic: bool = False) -> List[Union[
                    Type, Status, Media, Platform, ShareSite, Issue, Warehouse, Poster,
                    MediaPlatform]]:
        """ Return all elements of a table.
        @ Input:
        ╠═  · table_name    -   str
        ║   └ Name of the table to query.
        ╠═  · limit         -   int     -   None
        ║   └ Maximum number of elements to retrieve.
        ╠═  · offset        -   int     -   0
        ║   └ How far removed from the start should the results to return start.
        ╚═  · alfabetic     -   bool    -   None
            └ Indicate if the output should be alfabetically ordered.
        @ Output:
        ╚═  List[Any Entity Object]   -   With all the information of the table.
        """
        if isinstance(table_name, tuple):
            logging.info(_(f'''Getting all entries of joined tables "{'" & "'.join(table_name)}"
                    with limit "{limit}", offset "{offset}" and alfabetic order "{alfabetic}"'''))
        else:
            logging.info(_(f'Getting all entries of table "{table_name}" with limit "{limit}", \
                    offset "{offset}" and alfabetic order "{alfabetic}"'))

        if isinstance(table_name, tuple) and table_name[0] == Type.table_name and len(table_name) > 1:
            return self.model.get_all_type(table_name=table_name[1], limit=limit,
                                            offset=offset, alfabetic=alfabetic)
        elif table_name == Type.table_name or table_name[0] == Type.table_name:
            return self.model.get_all_type(table_name=None, limit=limit,
                                            offset=offset, alfabetic=alfabetic)
        elif table_name == Status.table_name:
            return self.model.get_all_status(limit, offset, alfabetic)
        elif table_name == Media.table_name:
            return self.model.get_all_media(limit, offset, alfabetic)
        elif table_name == Platform.table_name:
            return self.model.get_all_platform(limit, offset, alfabetic)
        elif table_name == ShareSite.table_name:
            return self.model.get_all_sharesite(limit, offset, alfabetic)
        elif table_name == Issue.table_name:
            return self.model.get_all_issue(limit, offset, alfabetic)
        elif table_name == Warehouse.table_name:
            return self.model.get_all_warehouse(limit, offset, alfabetic)
        elif table_name == Poster.table_name:
            return self.model.get_all_poster(limit, offset, alfabetic)
        elif table_name == MediaPlatform.table_name:
            return self.model.get_all_media_platform(limit, offset, alfabetic)
    # GET ALL #

    # GET BY ID
    def get_by_id(self, table_name: str, id_: int) ->\
            Union[Type, Status, Media,
                  Platform, Group, App,
                  Extension, Warehouse, Folder, Issue,
                  Version, Encoder, File, Codec,
                  Track, Language, Poster]:
        """ Returns a element of the table discriminating by its id.
        @ Input:
        ╠═  · table_name    -   str
        ║   └ Name of the table to query.
        ╚═  · id_           -   int
            └ Identifier of the element to gather from the table.
        @ Output:
        ╠═  Any Entity Object    -   The element of the table discriminated by id.
        ╚═  None                 -   If no matches exists.
        """
        logging.info(_(f'Searching on "{table_name}" table any entries that\
                match the given id "{id_}"'))
        if id_ is None: return None
        elif table_name == Type.table_name:
            return self.model.get_type_by_id(id_)
        elif table_name == Status.table_name:
            return self.model.get_status_by_id(id_)
        elif table_name == Media.table_name:
            return self.model.get_media_by_id(id_)
        elif table_name == Platform.table_name:
            return self.model.get_platform_by_id(id_)
        elif table_name == Group.table_name:
            return self.model.get_group_by_id(id_)
        elif table_name == App.table_name:
            return self.model.get_app_by_id(id_)
        elif table_name == Extension.table_name:
            return self.model.get_extension_by_id(id_)
        elif table_name == Warehouse.table_name:
            return self.model.get_warehouse_by_id(id_)
        elif table_name == Folder.table_name:
            return self.model.get_folder_by_id(id_)
        elif table_name == Issue.table_name:
            return self.model.get_issue_by_id(id_)
        elif table_name == Version.table_name:
            return self.model.get_version_by_id(id_)
        elif table_name == Encoder.table_name:
            return self.model.get_encoder_by_id(id_)
        elif table_name == File.table_name:
            return self.model.get_file_by_id(id_)
        elif table_name == Codec.table_name:
            return self.model.get_codec_by_id(id_)
        elif table_name == Track.table_name:
            return self.model.get_track_by_id(id_)
        elif table_name == Language.table_name:
            return self.model.get_language_by_id(id_)
        elif table_name == Poster.table_name:
            return self.model.get_poster_by_id(id_)
    # GET BY ID #

    # GET BY NK
    def get_by_nk(self, obj: Union[Group, Version, Encoder, File, Type, Codec]) -> \
            Union[Group, Version, Encoder, File, Type, Codec, Track,
                  Language, TrackLanguage, Poster, Media]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   Entity
            └ The Entity object to use in the search.
        @ Output:
        ╠═  Any Entity  -   The element of the table discriminated by natural key.
        ╚═  None        -   If no matches exists.
        """
        logging.info(_(f'Searching on "{obj.table_name}" table any entries that match its natural key'))
        if isinstance(obj, Group):
            return self.model.get_group_by_nk(obj)
        elif isinstance(obj, Version):
            return self.model.get_version_by_nk(obj)
        elif isinstance(obj, Encoder):
            return self.model.get_encoder_by_nk(obj)
        elif isinstance(obj, File):
            return self.model.get_file_by_nk(obj)
        elif isinstance(obj, Type):
            return self.model.get_type_by_nk(obj)
        elif isinstance(obj, Codec):
            return self.model.get_codec_by_nk(obj)
        elif isinstance(obj, Track):
            return self.model.get_track_by_nk(obj)
        elif isinstance(obj, Language):
            return self.model.get_language_by_nk(obj)
        elif isinstance(obj, TrackLanguage):
            return self.model.get_track_language_by_nk(obj)
        elif isinstance(obj, Poster):
            return self.model.get_poster_by_nk(obj)
        elif isinstance(obj, Media):
            return self.model.get_media_by_nk(obj)
    # GET BY NK

    # GET BY X
    def get_group_by_media_id(self, id_: int, limit: int = None,
                                    offset: int = 0, alfabetic: bool = None
                                    ) -> Union[None, List[Group]]:
        """ Returns a group discriminated by its id.
        @ Input:
        ╠═  · id_       -   int
        ║   └ Id of the media to use as a discriminator.
        ╠═  · limit     -   int     -   None
        ║   └ Maximum number of elements to retrieve.
        ╠═  · offset    -   int     -   0
        ║   └ How far removed from the start should the results to return start.
        ╚═  · alfabetic -   bool    -   None
            └ Indicate if the output should be alfabetically ordered.
        @ Output:
        ╠═  Group   -   The element of the table discriminated by natural key.
        ╚═  None         -   If no matches exists.
        """
        logging.info(_(f'Searching on "{Group.table_name}" table any entries '+
        'that match its media foreign key "{id_}"'))
        return self.model.get_group_by_media_id(id_= id_, limit= limit,
                                                      offset= offset, alfabetic= alfabetic)

    def get_language_by_codename(self, codename: str) -> Union[None, Language]:
        """ Returns a language discriminated by the given codename.
        If a new code is added that makes it so codenames are reused
        for different languages this function must be rewritten.
        @ Input:
        ╠═  · codename  -   str
        ║   └ Code that identifies the language in some system.
        ╠═  · limit     -   int     -   None
        ║   └ Maximum number of elements to retrieve.
        ╠═  · offset    -   int     -   0
        ║   └ How far removed from the start should the results to return start.
        ╚═  · alfabetic -   bool    -   None
            └ Indicate if the output should be alfabetically ordered.
        @ Output:
        ╠═  Language    -   That matches the codename posibilities.
        ╚═  None        -   If no matches exists.
        """
        logging.info(_(f'Searching on "{Language.table_name}" and "{LanguageCode.table_name}"'+
        'tables the entry that matches the codename "{codename}."'))
        return self.model.get_language_by_codename(codename=codename)

    # GET BY X #

    # GET BY NAME
    def get_by_name(self, table_name: str, name: str, limit: int = None,
                    offset: int = 0, alfabetic: bool = False
                    ) -> Union[None, List[Union[Type, Status,
                                                Extension, Folder, App, Language]]]:
        """ Returns all elements of table that match the given name.
        @ Input:
        ╠═  · table_name    -   str
        ║   └ Id of the media to use as a discriminator.
        ╠═  · name          -   str
        ║   └ Name to use to descriminate the data of the table by.
        ╠═  · limit         -   int     -   None
        ║   └ Maximum number of elements to retrieve.
        ╠═  · offset        -   int     -   0
        ║   └ How far removed from the start should the results to return start.
        ╚═  · alfabetic     -   bool    -   None
            └ Indicate if the output should be alfabetically ordered.
        @ Output:
        ╠═  List[Any Entity Object] -   The elements of the table discriminated by name.
        ╚═  None                    -   If no matches exists.
        """
        logging.info(_(f'Searching on "{table_name}" table any entries that match the given name "{name}"'))
        if table_name == Type.table_name:
            return self.model.get_by_type_name(name= name, limit= limit, offset= offset, alfabetic= alfabetic)
        elif table_name == Status.table_name:
            return self.model.get_by_status_name(name= name, limit= limit, offset= offset, alfabetic= alfabetic)
        elif table_name == Extension.table_name:
            return self.model.get_extension_by_name(name= name, limit= limit, offset= offset, alfabetic= alfabetic)
        elif table_name == Folder.table_name:
            return self.model.get_folder_by_name(name=name, limit=limit, offset=offset, alfabetic=alfabetic)
        elif table_name == App.table_name:
            return self.model.get_app_by_name(name=name, limit=limit, offset=offset, alfabetic=alfabetic)
        elif table_name == Language.table_name:
            return self.model.get_language_by_name(name=name, limit=limit, offset=offset, alfabetic=alfabetic)
    # GET BY NAME

    # INSERT
    def insert(self, obj: Union[Status, Type, Media, Group,
                                Issue, Platform, ShareSite,
                                Warehouse, Extension, Folder, App,
                                Version, Encoder, Codec, Track,
                                TrackLanguage, Poster, MediaPlatform]
               ) -> None:
        """ Adds an element to a DB table.
        @ Input:
        ╚═  · obj   -   Any Entity Type
            └ Entity to insert in the DB.
        @ Output:
        ╚═  None
        """
        logging.info(_(f'Inserting new value in the table "{obj.table_name}"'))
        if isinstance(obj, Status):
            return self.model.insert_status(obj)
        elif isinstance(obj, Type):
            return self.model.insert_type(obj)
        elif isinstance(obj, Media):
            return self.model.insert_media(obj)
        elif isinstance(obj, Group):
            return self.model.insert_group(obj)
        elif isinstance(obj, Issue):
            return self.model.insert_issue(obj)
        elif isinstance(obj, Platform):
            return self.model.insert_platform(obj)
        elif isinstance(obj, ShareSite):
            return self.model.insert_sharesite(obj)
        elif isinstance(obj, ShareSiteSubs):
            return self.model.insert_sharesite_subs(obj)
        elif isinstance(obj, Warehouse):
            return self.model.insert_warehouse(obj)
        elif isinstance(obj, Extension):
            return self.model.insert_extension(obj)
        elif isinstance(obj, Folder):
            return self.model.insert_folder(obj)
        elif isinstance(obj, App):
            return self.model.insert_app(obj)
        elif isinstance(obj, Version):
            return self.model.insert_version(obj)
        elif isinstance(obj, Encoder):
            return self.model.insert_encoder(obj)
        elif isinstance(obj, File):
            return self.model.insert_file(obj)
        elif isinstance(obj, Codec):
            return self.model.insert_codec(obj)
        elif isinstance(obj, Track):
            return self.model.insert_track(obj)
        elif isinstance(obj, TrackLanguage):
            return self.model.insert_track_language(obj)
        elif isinstance(obj, Poster):
            return self.model.insert_poster(obj)
        elif isinstance(obj, MediaPlatform):
            return self.model.insert_media_platform(obj)
    # INSERT #

# ------------------------------------------------------------------------------
