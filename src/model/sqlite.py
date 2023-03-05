#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/03/05 21:42:49.981918
# ------------------------------------------------------------------------------
#* Concrete Strategy (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.model import iModel
# ------------------------------------------------------------------------------
import sqlite3
from sqlite3 import Connection, Cursor, IntegrityError
from uteis.ficheiro import cargarFich as load_file
import logging
from typing import List, Union

from src.utils import Config

from src.model.entity import Warehouse, WarehouseType
from src.model.entity import Media, MediaGroup, MediaIssue
from src.model.entity import MediaType, MediaStatus
from src.model.entity import Platform, ShareSiteType, ShareSite, ShareSiteSubs
from src.model.entity import WarehouseType, Warehouse
from src.model.entity import Extension, Folder, App, AppVersion, Encoder, File
# ------------------------------------------------------------------------------
class Sqlite(iModel):
    def __init__(self, ficheiro: str) -> None:
        logging.info(_('Starting the sqlite database'))
        # xFCR check if better to add the declaration here an not in creation of object
        self.ficheiro = ficheiro
        self.conn = None
        self.cur = None

        # if the DB doesnt have all the number of supposed tables, run the creation script.
        if(self.__get_num_tables_db() < Config().get_num_entities()):
            logging.info(_('Creating the sqlite database'))
            self.cur.executescript(''.join(load_file('./src/model/db_scripts/sqlite/Media4.db.create.sql')))
            if Config().populate_db:
                logging.info(_('Populating the sqlite database'))
                self.cur.executescript(''.join(load_file('./src/model/db_scripts/sqlite/Media4.db.insert.sql')))

    def __get_num_tables_db(self) -> int:
        self.connect_db()
        return self.cur.execute('select count(*) from sqlite_master where type="table"').fetchone()[0];

    def get_conn_db(self) -> Connection:
        """ Returns a connection to the DB.
        @ Input:
        @ Output:
        ╚═ Connection   -   Connection object to the DB.
        """
        if self.conn == None:
            logging.info(_('Creating a new connection to the sqlite database'))
            return self.connect_db()[0]
        return self.conn

    def get_cur_db(self) -> Cursor:
        """ Returns a cursor to the DB.
        @ Input:
        @ Output:
        ╚═ Cursor   -   Cursor object in the DB.
        """
        if self.cur == None:
            return self.connect_db()[1]
        return self.cur

    def connect_db(self) -> tuple([Connection, Cursor]):
        """ Does the whole process of connecting to a DB.
        @ Input:
        @ Ouput:
        ╚═ (Connection, Cursor) -   Tuple with objects of DB Connection and Cursor.
        """
        # this check_same_thread option may give problems
        # may need to make a queue
        self.conn = sqlite3.connect(database=self.ficheiro, check_same_thread=False)
        self.cur = self.conn.cursor()
        return (self.conn, self.cur)

    def disconnect_db(self, commit: bool = True) -> None:
        """ Does the whole process of disconnecting from a DB.
        @ Input:
        ╚═  · commit -   bool    -   True
            └ Indicates if changes to the DB should be commited or rolled back.
        @ Output:
        """
        if self.conn:
            if commit:
                self.conn.commit()
            self.conn.close()
            self.conn = None
            self.cur = None

    def save_db(self) -> None:
        """ Saves the non commited changes to the DB.
        @ Input:
        @ Output:
        """
        if self.conn:
            self.conn.commit()


    # EXISTS
    def exists(self, obj: Union[MediaGroup, MediaIssue, Platform,
            ShareSiteType, ShareSite, WarehouseType, Warehouse,
            Extension]) -> bool:
        """ Checks if a element is saved in the DB.
        @ Input:
        ╚═  · obj   -   Any Entity Object   -   True
            └ Object to check if it exists in the DB.

        @ Output:
        ╚═  bool    -   Indicating if the object exists or not.
        """
        pass

    def exists_media_group(self, obj: MediaGroup) -> bool:
        sql_result = self.get_cur_db().execute(f'select id from "{MediaGroup.table_name}" where id_media="{obj.media.id_}" and number="{obj.number}"').fetchall()
        if len(sql_result) > 0:
            return True
        return False

    def exists_media_issue(self, obj: MediaIssue) -> bool:
        sql_result = self.get_cur_db().execute(f'select id from "{MediaIssue.table_name}" where id_media="{obj.media.id_}" and id_media_group="{obj.media_group.id_}" and position="{obj.position}"').fetchall()
        if len(sql_result) > 0:
            return True
        return False

    def exists_platform(self, obj: Platform) -> bool:
        sql_result = self.get_cur_db().execute(f'select id from "{Platform.table_name}" where name like "{obj.name}"').fetchall()
        if len(sql_result) > 0:
            return True
        return False

    def exists_sharesite_type(self, obj: ShareSiteType) -> bool:
        sql_result = self.get_cur_db().execute(f'select id from "{ShareSiteType.table_name}" where name like "{obj.name}"').fetchall()
        if len(sql_result) > 0:
            return True
        return False

    def exists_sharesite(self, obj: ShareSite) -> bool:
        sql_result = self.get_cur_db().execute(f'select id from "{ShareSite.table_name}" \
                where link like "{obj.link}"').fetchall()
        if len(sql_result) > 0:
            return True
        return False

    def exists_sharesite_subs(self, obj: ShareSiteSubs) -> bool:
        sql_result = self.get_cur_db().execute(f'select id from "{ShareSiteSubs.table_name}" where \
                id_share_site={obj.share_site.id_} and sub_num={obj.sub_num} \
                and added_ts like "{obj.added_ts}%"').fetchall()
        if len(sql_result) > 0:
            return True
        return False

    def exists_warehouse_type(self, obj: WarehouseType) -> bool:
        """
        """
        sql_result = self.get_cur_db().execute(f'select id from "{WarehouseType.table_name}" \
                where name like "{obj.name}"').fetchall()
        if len(sql_result) > 0:
            return True
        return False

    def exists_warehouse(self, obj: Warehouse) -> bool:
        """
        """
        sql_result = self.get_cur_db().execute(f'select id from "{Warehouse.table_name}" \
                where name like "{obj.name}"').fetchall()
        if len(sql_result) > 0:
            return True
        return False

    def exists_extension(self, obj: Extension) -> bool:
        """
        """
        sql_result = self.get_cur_db().execute(f'select id from "{Extension.table_name}" \
                where name like "{obj.name}"').fetchall()
        if len(sql_result) > 0:
            return True
        return False
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
        return self.get_cur_db().execute(f'select count(*) from "{table_name}"').fetchone()[0]

    def get_media_group_num_by_media_id(self, media_id: int) -> int:
        """Returns the number of group elements discriminating by media id.
        @ Input:
        ╚═  · media_id  -   int
            └ Id of the media to use as a discriminator.
        @ Output:
        ╚═  int - Number of entries on the table that meet the criteria.
        """
        return self.get_cur_db().execute(f'select count(*) from "{MediaGroup.table_name}" where id_media = "{media_id}"').fetchone()[0]
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
        pass

    def get_all_media_type(self, limit: int, offset: int, alfabetic: bool) -> List[MediaType]:
        sentence = f'select id, active, name, groupable, added_ts, modified_ts from "{MediaType.table_name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(MediaType(
                id_         = result[0],
                active      = result[1],
                name        = result[2],
                groupable   = result[3],
                added_ts    = result[4],
                modified_ts = result[5]
            ))
        return results

    def get_all_media_status(self, limit: int, offset: int, alfabetic: bool) -> List[MediaStatus]:
        sentence = f'select id, active, name, added_ts, modified_ts from "{MediaStatus.table_name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(MediaStatus(
                id_         = result[0],
                active      = result[1],
                name        = result[2],
                added_ts    = result[3],
                modified_ts = result[4]
            ))
        return results

    def get_all_media(self, limit: int, offset: int, alfabetic: bool) -> List[Media]:
        sentence = f'select id, active, name, year_start, year_end, id_type, id_status, added_ts, modified_ts from "{Media.table_name}"'
        if alfabetic: sentence += ' order by name asc'
        if limit != None and offset != None: sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(Media(
                    id_         = result[0],
                    active      = result[1],
                    name        = result[2],
                    year_start  = result[3],
                    year_end    = result[4],
                    type_       = self.get_media_type_by_id(result[5]),
                    status      = self.get_media_status_by_id(result[6]),
                    added_ts    = result[7],
                    modified_ts = result[8]
            ))
        return results

    def get_all_sharesite_type(self, limit: int, offset: int, alfabetic: bool) -> List[ShareSiteType]:
        """
        """
        sentence = f'select id, active, name, added_ts, modified_ts from "{ShareSiteType.table_name}"'
        if alfabetic: sentence += ' order by name asc'
        if limit != None and offset != None: sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(ShareSiteType(
                    id_         = result[0],
                    active      = result[1],
                    name        = result[2],
                    added_ts    = result[3],
                    modified_ts = result[4]
            ))
        return results

    def get_all_platform(self, limit: int, offset: int, alfabetic: bool) -> List[Platform]:
        """
        """
        sentence = f'select id, active, name, added_ts, modified_ts from "{Platform.table_name}"'
        if alfabetic: sentence += ' order by name asc'
        if limit != None and offset != None: sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(Platform(
                    id_         = result[0],
                    active      = result[1],
                    name        = result[2],
                    added_ts    = result[3],
                    modified_ts = result[4]
            ))
        return results

    def get_all_sharesite(self, limit: int, offset: int, alfabetic: bool) -> List[ShareSite]:
        """
        """
        sentence = f'select id, active, in_platform_id, name, private, link, id_type, \
                id_platform, added_ts, modified_ts from "{ShareSite.table_name}"'
        if alfabetic: sentence += ' order by name asc'
        if limit != None and offset != None: sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(ShareSite(
                    id_             = result[0],
                    active          = result[1],
                    in_platform_id  = result[2],
                    name            = result[3],
                    private         = result[4],
                    link            = result[5],
                    type_           = self.get_sharesite_type_by_id(result[6]),
                    platform        = self.get_platform_by_id(result[7]),
                    added_ts        = result[8],
                    modified_ts     = result[9]
            ))
        return results

    def get_all_warehouse_type(self, limit: int, offset: int, alfabetic: bool) -> List[WarehouseType]:
        """
        """
        sentence = f'select id, active, name, added_ts, modified_ts from "{WarehouseType.table_name}"'
        if alfabetic: sentence += ' order by name asc'
        if limit != None and offset != None: sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(WarehouseType(
                    id_             = result[0],
                    active          = result[1],
                    name            = result[2],
                    added_ts        = result[3],
                    modified_ts     = result[4]
            ))
        return results

    def get_all_media_issue(self, limit: int, offset: int, alfabetic: bool) -> List[MediaIssue]:
        """
        """
        sentence = f'select id, active, position, name, date, id_media, id_media_group, added_ts, modified_ts from "{MediaIssue.table_name}"'
        if alfabetic: sentence += ' order by name asc'
        if limit != None and offset != None: sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(MediaIssue(
                    id_             = result[0],
                    active          = result[1],
                    position        = result[2],
                    name            = result[3],
                    date            = result[4],
                    media           = self.get_media_by_id(result[5]),
                    media_group     = self.get_media_group_by_id(result[6]),
                    added_ts        = result[7],
                    modified_ts     = result[8]
            ))
        return results

    def get_all_warehouse(self, limit: int, offset: int, alfabetic: bool) -> List[Warehouse]:
        """
        """
        sentence = f'select id, active, name, size, filled, content, id_type, health, \
                added_ts, modified_ts from "{Warehouse.table_name}"'
        if alfabetic: sentence += ' order by name asc'
        if limit != None and offset != None: sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(Warehouse(
                    id_         = result[0],
                    active      = result[1],
                    name        = result[2],
                    size        = result[3],
                    filled      = result[4],
                    content     = result[5],
                    type_       = self.get_warehouse_type_by_id(result[6]),
                    health      = result[7],
                    added_ts    = result[8],
                    modified_ts = result[9]
            ))
        return results
    # GET ALL #

    # GET BY ID
    def get_by_id(self, table_name: str, id_: int) ->\
            Union[MediaType, MediaStatus, Media, ShareSiteType,
                  Platform, MediaGroup, WarehouseType, App,
                  Extension, Warehouse, Folder, MediaIssue,
                  AppVersion, Encoder]:
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
        pass

    def get_media_type_by_id(self, id_: int) -> Union[None, MediaType]:
        sql_result = self.get_cur_db().execute(f'select id, active, name, groupable, added_ts, modified_ts from "{MediaType.table_name}" where id={id_}').fetchone()
        if sql_result:
            return MediaType(
                id_         = sql_result[0],
                active      = sql_result[1],
                name        = sql_result[2],
                groupable   = sql_result[3],
                added_ts    = sql_result[4],
                modified_ts = sql_result[5]
            )

    def get_media_status_by_id(self, id_: int) -> Union[None, MediaStatus]:
        sql_result = self.get_cur_db().execute(f'select id, active, name, added_ts, modified_ts from "{MediaStatus.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return MediaStatus(
                id_         = sql_result[0],
                active      = sql_result[1],
                name        = sql_result[2],
                added_ts    = sql_result[3],
                modified_ts = sql_result[4]
            )

    def get_media_by_id(self, id_: int) -> Union[None, Media]:
        sql_result = self.get_cur_db().execute(f'select id, active, name, year_start, year_end, \
                id_type, id_status, added_ts, modified_ts from "{Media.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return Media(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    name        = sql_result[2],
                    year_start  = sql_result[3],
                    year_end    = sql_result[4],
                    type_       = self.get_media_type_by_id(sql_result[5]),
                    status      = self.get_media_status_by_id(sql_result[6]),
                    added_ts    = sql_result[7],
                    modified_ts = sql_result[8]
            )

    def get_sharesite_type_by_id(self, id_: int) -> Union[None, ShareSiteType]:
        """"""
        sql_result = self.get_cur_db().execute(f'select id, active, name, added_ts, \
                modified_ts from "{ShareSiteType.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return ShareSiteType(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    name        = sql_result[2],
                    added_ts    = sql_result[3],
                    modified_ts = sql_result[4]
            )

    def get_platform_by_id(self, id_: int) -> Union[None, Platform]:
        """"""
        sql_result = self.get_cur_db().execute(f'select id, active, name, added_ts, \
                modified_ts from "{Platform.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return Platform(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    name        = sql_result[2],
                    added_ts    = sql_result[3],
                    modified_ts = sql_result[4]
            )

    def get_media_group_by_id(self, id_: int) -> Union[None, MediaGroup]:
        sql_result = self.get_cur_db().execute(f'select id, active, number, name, year_start, \
                year_end, id_media, added_ts, modified_ts from "{MediaGroup.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return MediaGroup(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    number      = sql_result[2],
                    name        = sql_result[3],
                    year_start  = sql_result[4],
                    year_end    = sql_result[5],
                    media       = self.get_media_by_id(sql_result[6]),
                    added_ts    = sql_result[7],
                    modified_ts = sql_result[8]
            )

    def get_warehouse_type_by_id(self, id_: int) -> WarehouseType:
        sql_result = self.get_cur_db().execute(f'select id, active, name, added_ts, \
                modified_ts from "{WarehouseType.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return WarehouseType(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    name        = sql_result[2],
                    added_ts    = sql_result[3],
                    modified_ts = sql_result[4]
            )

    def get_app_by_id(self, id_: int) -> App:
        sql_result = self.get_cur_db().execute(f'select id, active, name, added_ts, \
                modified_ts from "{App.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return App(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    name        = sql_result[2],
                    added_ts    = sql_result[3],
                    modified_ts = sql_result[4]
            )

    def get_extension_by_id(self, id_: int) -> Extension:
        sql_result = self.get_cur_db().execute(f'select id, active, name, format_name, \
                format_name_long, added_ts, modified_ts from "{Extension.table_name}" \
                where id="{id_}"').fetchone()
        if sql_result:
            return Extension(
                    id_                 = sql_result[0],
                    active              = sql_result[1],
                    name                = sql_result[2],
                    format_name         = sql_result[3],
                    format_name_long    = sql_result[4],
                    added_ts            = sql_result[5],
                    modified_ts         = sql_result[6]
            )

    def get_warehouse_by_id(self, id_: int) -> Warehouse:
        sql_result = self.get_cur_db().execute(f'select id, active, name, size, \
                filled, content, id_type, health, added_ts, modified_ts \
                from "{Warehouse.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return Warehouse(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    name        = sql_result[2],
                    size        = sql_result[3],
                    filled      = sql_result[4],
                    content     = sql_result[5],
                    type_       = self.get_warehouse_type_by_id(sql_result[6]),
                    health      = sql_result[7],
                    added_ts    = sql_result[8],
                    modified_ts = sql_result[9]
            )

    def get_folder_by_id(self, id_: int) -> Folder:
        sql_result = self.get_cur_db().execute(f'select id, active, path, added_ts, \
                modified_ts from "{Folder.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return Folder(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    path        = sql_result[2],
                    added_ts    = sql_result[3],
                    modified_ts = sql_result[4]
            )

    def get_media_issue_by_id(self, id_: int) -> MediaIssue:
        sql_result = self.get_cur_db().execute(f'select id, active, position, \
                name, date, id_media, id_media_group, added_ts, modified_ts \
                from "{MediaIssue.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return MediaIssue(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    position    = sql_result[2],
                    name        = sql_result[3],
                    date        = sql_result[4],
                    media       = self.get_media_by_id(sql_result[5]),
                    media_group = self.get_media_group_by_id(sql_result[6]),
                    added_ts    = sql_result[7],
                    modified_ts = sql_result[8]
            )

    def get_app_version_by_id(self, id_: int) -> AppVersion:
        sql_result = self.get_cur_db().execute(f'select id, active, number, name, \
                num_bit_processor, added_ts, modified_ts from "{AppVersion.table_name}" \
                where id="{id_}"').fetchone()
        if sql_result:
            return AppVersion(
                    id_                 = sql_result[0],
                    active              = sql_result[1],
                    number              = sql_result[2],
                    name                = sql_result[3],
                    num_bit_processor   = sql_result[4],
                    added_ts            = sql_result[5],
                    modified_ts         = sql_result[6]
            )

    def get_encoder_by_id(self, id_: int) -> Encoder:
        sql_result = self.get_cur_db().execute(f'select id, active, name, \
                added_ts, modified_ts from "{Encoder.table_name}" \
                where id="{id_}"').fetchone()
        if sql_result:
            return Encoder(
                    id_                 = sql_result[0],
                    active              = sql_result[1],
                    name                = sql_result[2],
                    added_ts            = sql_result[3],
                    modified_ts         = sql_result[4]
            )
    # GET BY ID

    # GET BY NK
    def get_by_nk(self, obj: Union[MediaGroup, AppVersion, Encoder, File]) -> \
            Union[MediaGroup, AppVersion, Encoder, File]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   Entity
            └ The Entity object to use in the search.
        @ Output:
        ╠═  Any Entity  -   The element of the table discriminated by natural key.
        ╚═  None        -   If no matches exists.
        """
        pass

    def get_media_group_by_nk(self, obj: MediaGroup) -> Union[None, MediaGroup]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   MediaGroup
            └ The MediaGroup object to use in the search.
        @ Output:
        ╠═  MediaGroup   -   The element of the table discriminated by natural key.
        ╚═  None         -   If no matches exists.
        """
        sql_result = self.get_cur_db().execute(f'select id, active, name, number, year_start, year_end, id_media, added_ts, modified_ts from "{MediaGroup.table_name}" where number="{obj.number}" and id_media="{obj.media.id_}"').fetchone()
        if sql_result:
            return MediaGroup(
                    id_         =   sql_result[0],
                    active      =   sql_result[1],
                    name        =   sql_result[2],
                    number      =   sql_result[3],
                    year_start  =   sql_result[4],
                    year_end    =   sql_result[5],
                    media       =   self.get_media_by_id(sql_result[6]),
                    added_ts    =   sql_result[7],
                    modified_ts =   sql_result[8]
            )

    def get_app_version_by_nk(self, obj: AppVersion) -> Union[None, AppVersion]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   AppVersion
            └ The AppVersion object to use in the search.
        @ Output:
        ╠═  AppVersion  -   The element of the table discriminated by natural key.
        ╚═  None        -   If no matches exists.
        """
        sql_result = self.get_cur_db().execute(f'select id, active, id_app, number, name, num_bit_processor, \
                added_ts, modified_ts from "{AppVersion.table_name}" where id_app="{obj.app.id_}"\
                and number="{obj.number}"').fetchone()
        if sql_result:
            return AppVersion(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    app         = self.get_app_by_id(sql_result[2]),
                    number      = sql_result[3],
                    name        = sql_result[4],
                    added_ts    = sql_result[5],
                    modified_ts = sql_result[6]
            )

    def get_encoder_by_nk(self, obj: Encoder) -> Union[None, Encoder]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   Encoder
            └ The Encoder object to use in the search.
        @ Output:
        ╠═  Encoder -   The element of the table discriminated by natural key.
        ╚═  None    -   If no matches exists.
        """
        sql_result = self.get_cur_db().execute(f'select id, active, name, added_ts, \
                modified_ts from "{Encoder.table_name}" where name="{obj.name}"').fetchone()
        if sql_result:
            return Encoder(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    name        = sql_result[2],
                    added_ts    = sql_result[3],
                    modified_ts = sql_result[4]
            )

    def get_file_by_nk(self, obj: File) -> Union[None, File]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   File
            └ The File object to use in the search.
        @ Output:
        ╠═  File    -   The element of the table discriminated by natural key.
        ╚═  None    -   If no matches exists.
        """
        sql_result = self.get_cur_db().execute(f'select id, active, name, id_extension, \
                id_warehouse, id_folder, id_media, id_media_issue, title, nb_streams, \
                nb_programs, start, duration, size, bit_rate, probe_score, creation_ts, \
                id_app_version, id_encoder, original_name, added_ts, modified_ts \
                from "{File.table_name}" where name="{obj.name}" and \
                id_extension="{obj.extension.id_}" and id_folder="{obj.folder.id_}" and \
                id_warehouse="{obj.warehouse.id_}"').fetchone()
        if sql_result:
            return File(
                    id_             = sql_result[0],
                    active          = sql_result[1],
                    name            = sql_result[2],
                    extension       = self.get_extension_by_id(sql_result[3]),
                    warehouse       = self.get_warehouse_by_id(sql_result[4]),
                    folder          = self.get_folder_by_id(sql_result[5]),
                    media           = self.get_media_by_id(sql_result[6]),
                    media_issue     = self.get_media_issue_by_id(sql_result[7]),
                    title           = sql_result[8],
                    nb_streams      = sql_result[9],
                    start           = sql_result[10],
                    duration        = sql_result[11],
                    size            = sql_result[12],
                    bit_rate        = sql_result[13],
                    probe_score     = sql_result[14],
                    creation_ts     = sql_result[15],
                    app_version     = self.get_app_version_by_id(sql_result[16]),
                    encoder         = self.get_encoder_by_id(sql_result[17]),
                    original_name   = sql_result[18],
                    added_ts        = sql_result[19],
                    modified_ts     = sql_result[20]
            )
    # GET BY NK #

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
        sentence = f'select id, active, name, number, year_start, year_end, id_media, added_ts, modified_ts from "{MediaGroup.table_name}" where id_media="{id_}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(MediaGroup(
                    id_         =   result[0],
                    active      =   result[1],
                    name        =   result[2],
                    number      =   result[3],
                    year_start  =   result[4],
                    year_end    =   result[5],
                    media       =   self.get_media_by_id(result[6]),
                    added_ts    =   result[7],
                    modified_ts =   result[8]
            ))
        return results
    # GET BY X #

    # GET BY NAME
    def get_by_name(self, table_name: str, name: str, limit: int = None,
                    offset: int = 0, alfabetic: bool = False
                    ) -> Union[None, List[Union[MediaType, MediaStatus,
                                                Extension, Folder, App]]]:
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
        pass

    def get_by_media_type_name(self, name: str, limit: int, offset: int, alfabetic: bool) -> List[MediaType]:
        sentence = f'select id, active, name, groupable, added_ts, modified_ts from {MediaType.table_name} where name="{name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(MediaType(
                id_         = result[0],
                active      = result[1],
                name        = result[2],
                groupable   = result[3],
                added_ts    = result[4],
                modified_ts = result[5]
            ))
        return results

    def get_by_media_status_name(self, name: str, limit: int, offset: int, alfabetic: bool) -> List[MediaStatus]:
        sentence = f'select id, active, name, added_ts, modified_ts from {MediaStatus.table_name} where name="{name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(MediaStatus(
                id_         = result[0],
                active      = result[1],
                name        = result[2],
                added_ts    = result[3],
                modified_ts = result[4]
            ))
        return results

    def get_extension_by_name(self, name: str, limit: int, offset: int, alfabetic: bool) -> List[Extension]:
        sentence = f'select id, active, name, format_name, format_name_long, added_ts, \
                modified_ts from {Extension.table_name} where name="{name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(Extension(
                id_                 = result[0],
                active              = result[1],
                name                = result[2],
                format_name         = result[3],
                format_name_long    = result[4],
                added_ts            = result[5],
                modified_ts         = result[6]
            ))
        if results:
            return results[0]

    def get_folder_by_name(self, name: str, limit: int, offset: int, alfabetic: bool) -> List[Folder]:
        sentence = f'select id, active, path, added_ts, modified_ts \
                from {Folder.table_name} where path="{name}"'
        if alfabetic:
            sentence += ' order by path asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(Folder(
                id_         = result[0],
                active      = result[1],
                path        = result[2],
                added_ts    = result[3],
                modified_ts = result[4]
            ))
        if results:
            return results[0]

    def get_app_by_name(self, name: str, limit: int, offset: int, alfabetic: bool) -> List[App]:
        sentence = f'select id, active, name, added_ts, modified_ts \
                from {App.table_name} where name="{name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(App(
                id_         = result[0],
                active      = result[1],
                name        = result[2],
                added_ts    = result[3],
                modified_ts = result[4]
            ))
        if results:
            return results[0]
    # GET BY NAME #

    # INSERT
    def insert(self, obj: Union[MediaStatus, MediaType, Media, MediaGroup,
                                MediaIssue, Platform, ShareSiteType, ShareSite,
                                WarehouseType, Warehouse, Extension, Folder, App,
                                AppVersion, Encoder, File]
               ) -> None:
        """ Adds an element to a DB table.
        @ Input:
        ╚═  · obj   -   Any Entity Type
            └ Entity to insert in the DB.
        @ Output:
        ╚═  None
        """
        pass

    def insert_media_status(self, obj: MediaStatus) -> None:
        self.get_cur_db().execute(f'insert into "{MediaStatus.table_name}" (active, name) values (?, ?)', (obj.active, obj.name))

    def insert_media_type(self, obj: MediaType) -> None:
        self.get_cur_db().execute(f'insert into "{MediaType.table_name}" (active, name, groupable) values (?, ?, ?)', (obj.active, obj.name, obj.groupable))

    def insert_media(self, obj: Media) -> None:
        self.get_cur_db().execute(f'insert into "{Media.table_name}" (active, name, year_start, year_end, id_type, id_status) values (?, ?, ?, ?, ?, ?)', (obj.active, obj.name, obj.year_start, obj.year_end, obj.type_.id_, obj.status.id_))

    def insert_media_group(self, obj: MediaGroup) -> None:
        self.get_cur_db().execute(f'insert into "{MediaGroup.table_name}" (active, name, number, year_start, year_end, id_media) values (?, ?, ?, ?, ?, ?)', (obj.active, obj.name, obj.number, obj.year_start, obj.year_end, obj.media.id_))

    def insert_media_issue(self, obj: MediaGroup) -> None:
        self.get_cur_db().execute(f'insert into "{MediaIssue.table_name}" (active, position, name, date, id_media, id_media_group) values (?, ?, ?, ?, ?, ?)', (obj.active, obj.position, obj.name, obj.date, obj.media.id_, obj.media_group.id_))

    def insert_platform(self, obj: Platform) -> None:
        self.get_cur_db().execute(f'insert into "{Platform.table_name}" (active, name) values (?, ?)', (obj.active, obj.name))

    def insert_sharesite_type(self, obj: ShareSiteType) -> None:
        self.get_cur_db().execute(f'insert into "{ShareSiteType.table_name}" (active, name) values (?, ?)', (obj.active, obj.name))

    def insert_sharesite(self, obj: ShareSite) -> None:
        self.get_cur_db().execute(f'insert into "{ShareSite.table_name}" (active, in_platform_id, name, private, link, id_type, id_platform) values (?, ?, ?, ?, ?, ?, ?)', (obj.active, obj.in_platform_id, obj.name, obj.private, obj.link, obj.type_.id_, obj.platform.id_))

    def insert_sharesite_subs(self, obj: ShareSiteSubs) -> None:
        self.get_cur_db().execute(f'insert into "{ShareSiteSubs.table_name}" (id_share_site, sub_num) values (?, ?)', (obj.share_site.id_, obj.sub_num))

    def insert_warehouse_type(self, obj: WarehouseType) -> None:
        self.get_cur_db().execute(f'insert into "{WarehouseType.table_name}" \
                (active, name) values (?, ?)', (obj.active, obj.name))

    def insert_warehouse(self, obj: Warehouse) -> None:
        self.get_cur_db().execute(f'insert into "{Warehouse.table_name}" \
                (active, name, size, filled, content, id_type, health) values \
                (?, ?, ?, ?, ?, ?, ?)', (obj.active, obj.name, obj.size, obj.filled, \
                obj.content, obj.type_.id_, obj.health))

    def insert_extension(self, obj: Extension) -> None:
        self.get_cur_db().execute(f'insert into "{Extension.table_name}" \
                (active, name, format_name, format_name_long) values \
                (?, ?, ?, ?)', (obj.active, obj.name, obj.format_name, obj.format_name_long))

    def insert_folder(self, obj: Folder) -> None:
        self.get_cur_db().execute(f'insert into "{Folder.table_name}" \
                (active, path) values (?, ?)', (obj.active, obj.path))

    def insert_app(self, obj: App) -> None:
        self.get_cur_db().execute(f'insert into "{App.table_name}" \
                (active, name) values (?, ?)', (obj.active, obj.name))

    def insert_app_version(self, obj: AppVersion) -> None:
        self.get_cur_db().execute(f'insert into "{AppVersion.table_name}" \
                (active, id_app, number, name, num_bit_processor) \
                values (?, ?, ?, ?, ?)', (obj.active, obj.app.id_, obj.number,
                                          obj.name, obj.num_bit_processor))

    def insert_encoder(self, obj: Encoder) -> None:
        self.get_cur_db().execute(f'insert into "{Encoder.table_name}" \
                (active, name) values (?, ?)', (obj.active, obj.name))

    def insert_file(self, obj: File) -> None:
        id_media=None
        if obj.media: id_media=obj.media.id_
        id_media_issue=None
        if obj.media_issue: id_media_issue=obj.media_issue.id_
        id_app_version=None
        if obj.app_version: id_app_version=obj.app_version.id_
        id_encoder=None
        if obj.encoder: id_encoder=obj.encoder.id_

        self.get_cur_db().execute(f'insert into "{File.table_name}" \
                (active, name, id_extension, id_warehouse, id_folder, id_media, \
                id_media_issue, title, nb_streams, nb_programs, start, duration, \
                size, bit_rate, probe_score, creation_ts, id_app_version, id_encoder, \
                original_name) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
                ?, ?, ?, ?, ?, ?)', (obj.active, obj.name, obj.extension.id_,
                                     obj.warehouse.id_, obj.folder.id_, id_media,
                                     id_media_issue, obj.title, obj.nb_streams,
                                     obj.nb_programs, obj.start, obj.duration, obj.size,
                                     obj.bit_rate, obj.probe_score, obj.creation_ts,
                                     id_app_version, id_encoder, obj.original_name))
    # INSERT #
# ------------------------------------------------------------------------------
