#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/03/15 21:23:18.569016
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.model import iModel
# ------------------------------------------------------------------------------
from sqlite3 import Connection, Cursor
import logging
from typing import List, Union


from src.exception import InheritException

from src.model.entity import Warehouse, WarehouseType
from src.model.entity import Media, MediaGroup, MediaIssue
from src.model.entity import MediaType, MediaStatus
from src.model.entity import Platform, ShareSiteType, ShareSite, ShareSiteSubs
from src.model.entity import WarehouseType, Warehouse
from src.model.entity import Extension, Folder, App, AppVersion, Encoder, File
from src.model.entity import CodecType, Codec, Language, FileStream, FileStreamLanguage
from src.model.entity import LanguageCode
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
    def exists(self, obj: Union[MediaGroup, MediaIssue, Platform,
            ShareSiteType, ShareSite, WarehouseType, Warehouse,
            Extension, LanguageCode]) -> bool:
        """ Checks if a element is saved in the DB.
        @ Input:
        ╚═  · obj   -   Any Entity Object   -   True
            └ Object to check if it exists in the DB.
        @ Output:
        ╚═  bool    -   Indicating if the object exists or not.
        """
        logging.info(_(f'Checking on table "{obj.table_name}" if the information already exists'))
        if isinstance(obj, MediaGroup):
            return self.model.exists_media_group(obj)
        elif isinstance(obj, MediaIssue):
            return self.model.exists_media_issue(obj)
        elif isinstance(obj, Platform):
            return self.model.exists_platform(obj)
        elif isinstance(obj, ShareSiteType):
            return self.model.exists_sharesite_type(obj)
        elif isinstance(obj, ShareSite):
            return self.model.exists_sharesite(obj)
        elif isinstance(obj, ShareSiteSubs):
            return self.model.exists_sharesite_subs(obj)
        elif isinstance(obj, WarehouseType):
            return self.model.exists_warehouse_type(obj)
        elif isinstance(obj, Warehouse):
            return self.model.exists_warehouse(obj)
        elif isinstance(obj, Extension):
            return self.model.exists_extension(obj)
        elif isinstance(obj, LanguageCode):
            return self.model.exists_language_code(obj)
    # EXISTS #

    # GET NUM
    def get_num(self, table_name: str) -> int:
        """ Returns the number of elements in a table.
        @ Input:
        ╚═  · table_name    -   str
            └ Name of the table to query.
        @ Output:
        ╚═  int - Number of entries on the table.
        """
        logging.info(_(f'Counting the number of elements saved on table "{table_name}"'))
        return self.model.get_num(table_name)

    def get_media_group_num_by_media_id(self, media_id: int) -> int:
        """Returns the number of group elements discriminating by media id.
        @ Input:
        ╚═  · media_id  -   int
            └ Id of the media to use as a discriminator.
        @ Output:
        ╚═  int - Number of entries on the table that meet the criteria.
        """
        logging.info(_(f'Counting the number of elements saved on table "{MediaGroup.table_name}" using the media id "{media_id}"'))
        return self.model.get_media_group_num_by_media_id(media_id)
    # GET NUM #

    # GET ALL
    def get_all(self, table_name: str, limit: int = None, offset: int = 0, alfabetic: bool = False
                ) -> List[Union[MediaType, MediaStatus, Media, ShareSiteType, Platform, ShareSite,
                                WarehouseType, MediaIssue, Warehouse]]:
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
        logging.info(_(f'Getting all entries of table "{table_name}" with limit "{limit}", offset "{offset}" and alfabetic order "{alfabetic}"'))
        if table_name == MediaType.table_name:
            return self.model.get_all_media_type(limit, offset, alfabetic)
        elif table_name == MediaStatus.table_name:
            return self.model.get_all_media_status(limit, offset, alfabetic)
        elif table_name == Media.table_name:
            return self.model.get_all_media(limit, offset, alfabetic)
        elif table_name == ShareSiteType.table_name:
            return self.model.get_all_sharesite_type(limit, offset, alfabetic)
        elif table_name == Platform.table_name:
            return self.model.get_all_platform(limit, offset, alfabetic)
        elif table_name == ShareSite.table_name:
            return self.model.get_all_sharesite(limit, offset, alfabetic)
        elif table_name == WarehouseType.table_name:
            return self.model.get_all_warehouse_type(limit, offset, alfabetic)
        elif table_name == MediaIssue.table_name:
            return self.model.get_all_media_issue(limit, offset, alfabetic)
        elif table_name == Warehouse.table_name:
            return self.model.get_all_warehouse(limit, offset, alfabetic)
    # GET ALL #

    # GET BY ID
    def get_by_id(self, table_name: str, id_: int) ->\
            Union[MediaType, MediaStatus, Media, ShareSiteType,
                  Platform, MediaGroup, WarehouseType, App,
                  Extension, Warehouse, Folder, MediaIssue,
                  AppVersion, Encoder, CodecType, File, Codec,
                  FileStream, Language]:
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
        elif table_name == MediaType.table_name:
            return self.model.get_media_type_by_id(id_)
        elif table_name == MediaStatus.table_name:
            return self.model.get_media_status_by_id(id_)
        elif table_name == Media.table_name:
            return self.model.get_media_by_id(id_)
        elif table_name == ShareSiteType.table_name:
            return self.model.get_sharesite_type_by_id(id_)
        elif table_name == Platform.table_name:
            return self.model.get_platform_by_id(id_)
        elif table_name == MediaGroup.table_name:
            return self.model.get_media_group_by_id(id_)
        elif table_name == WarehouseType.table_name:
            return self.model.get_warehouse_type_by_id(id_)
        elif table_name == App.table_name:
            return self.model.get_app_by_id(id_)
        elif table_name == Extension.table_name:
            return self.model.get_extension_by_id(id_)
        elif table_name == Warehouse.table_name:
            return self.model.get_warehouse_by_id(id_)
        elif table_name == Folder.table_name:
            return self.model.get_folder_by_id(id_)
        elif table_name == MediaIssue.table_name:
            return self.model.get_media_issue_by_id(id_)
        elif table_name == AppVersion.table_name:
            return self.model.get_app_version_by_id(id_)
        elif table_name == Encoder.table_name:
            return self.model.get_encoder_by_id(id_)
        elif table_name == CodecType.table_name:
            return self.model.get_codec_type_by_id(id_)
        elif table_name == File.table_name:
            return self.model.get_file_by_id(id_)
        elif table_name == Codec.table_name:
            return self.model.get_codec_by_id(id_)
        elif table_name == FileStream.table_name:
            return self.model.get_file_stream_by_id(id_)
        elif table_name == Language.table_name:
            return self.model.get_language_by_id(id_)
    # GET BY ID #

    # GET BY NK
    def get_by_nk(self, obj: Union[MediaGroup, AppVersion, Encoder, File, CodecType, Codec]) -> \
            Union[None, MediaGroup, AppVersion, Encoder, File, CodecType, Codec, FileStream,
                  Language, FileStreamLanguage]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   Entity
            └ The Entity object to use in the search.
        @ Output:
        ╠═  Any Entity  -   The element of the table discriminated by natural key.
        ╚═  None        -   If no matches exists.
        """
        logging.info(_(f'Searching on "{obj.table_name}" table any entries that match its natural key'))
        if isinstance(obj, MediaGroup):
            return self.model.get_media_group_by_nk(obj)
        elif isinstance(obj, AppVersion):
            return self.model.get_app_version_by_nk(obj)
        elif isinstance(obj, Encoder):
            return self.model.get_encoder_by_nk(obj)
        elif isinstance(obj, File):
            return self.model.get_file_by_nk(obj)
        elif isinstance(obj, CodecType):
            return self.model.get_codec_type_by_nk(obj)
        elif isinstance(obj, Codec):
            return self.model.get_codec_by_nk(obj)
        elif isinstance(obj, FileStream):
            return self.model.get_file_stream_by_nk(obj)
        elif isinstance(obj, Language):
            return self.model.get_language_by_nk(obj)
        elif isinstance(obj, FileStreamLanguage):
            return self.model.get_file_stream_language_by_nk(obj)
    # GET BY NK

    # GET BY X
    def get_media_group_by_media_id(self, id_: int, limit: int = None,
                                    offset: int = 0, alfabetic: bool = None
                                    ) -> Union[None, List[MediaGroup]]:
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
        ╠═  MediaGroup   -   The element of the table discriminated by natural key.
        ╚═  None         -   If no matches exists.
        """
        logging.info(_(f'Searching on "{MediaGroup.table_name}" table any entries '+
        'that match its media foreign key "{id_}"'))
        return self.model.get_media_group_by_media_id(id_= id_, limit= limit,
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
                    ) -> Union[None, List[Union[MediaType, MediaStatus,
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
        if table_name == MediaType.table_name:
            return self.model.get_by_media_type_name(name= name, limit= limit, offset= offset, alfabetic= alfabetic)
        elif table_name == MediaStatus.table_name:
            return self.model.get_by_media_status_name(name= name, limit= limit, offset= offset, alfabetic= alfabetic)
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
    def insert(self, obj: Union[MediaStatus, MediaType, Media, MediaGroup,
                                MediaIssue, Platform, ShareSiteType, ShareSite,
                                WarehouseType, Warehouse, Extension, Folder, App,
                                AppVersion, Encoder, CodecType, Codec, FileStream,
                                FileStreamLanguage]
               ) -> None:
        """ Adds an element to a DB table.
        @ Input:
        ╚═  · obj   -   Any Entity Type
            └ Entity to insert in the DB.
        @ Output:
        ╚═  None
        """
        logging.info(_(f'Inserting new value in the table "{obj.table_name}"'))
        if isinstance(obj, MediaStatus):
            return self.model.insert_media_status(obj)
        elif isinstance(obj, MediaType):
            return self.model.insert_media_type(obj)
        elif isinstance(obj, Media):
            return self.model.insert_media(obj)
        elif isinstance(obj, MediaGroup):
            return self.model.insert_media_group(obj)
        elif isinstance(obj, MediaIssue):
            return self.model.insert_media_issue(obj)
        elif isinstance(obj, Platform):
            return self.model.insert_platform(obj)
        elif isinstance(obj, ShareSiteType):
            return self.model.insert_sharesite_type(obj)
        elif isinstance(obj, ShareSite):
            return self.model.insert_sharesite(obj)
        elif isinstance(obj, ShareSiteSubs):
            return self.model.insert_sharesite_subs(obj)
        elif isinstance(obj, WarehouseType):
            return self.model.insert_warehouse_type(obj)
        elif isinstance(obj, Warehouse):
            return self.model.insert_warehouse(obj)
        elif isinstance(obj, Extension):
            return self.model.insert_extension(obj)
        elif isinstance(obj, Folder):
            return self.model.insert_folder(obj)
        elif isinstance(obj, App):
            return self.model.insert_app(obj)
        elif isinstance(obj, AppVersion):
            return self.model.insert_app_version(obj)
        elif isinstance(obj, Encoder):
            return self.model.insert_encoder(obj)
        elif isinstance(obj, File):
            return self.model.insert_file(obj)
        elif isinstance(obj, CodecType):
            return self.model.insert_codec_type(obj)
        elif isinstance(obj, Codec):
            return self.model.insert_codec(obj)
        elif isinstance(obj, FileStream):
            return self.model.insert_file_stream(obj)
        elif isinstance(obj, FileStreamLanguage):
            return self.model.insert_file_stream_language(obj)
    # INSERT #

# ------------------------------------------------------------------------------
