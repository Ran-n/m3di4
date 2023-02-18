#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/02/18 15:29:13.901555
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
from src.model.entity import Platform
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
        self.conn = sqlite3.connect(self.ficheiro)
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
    def exists(self, obj: Union[MediaGroup, MediaIssue]) -> bool:
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


    # GET
    def get_all(self, table_name: str, limit: int = None,
                offset: int = 0, alfabetic: bool = False) -> List[Union[MediaType, MediaStatus]]:
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
        sentence = f'select id, name, description, groupable, active, added_ts, modified_ts from "{MediaType.table_name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(MediaType(
                id_         = result[0],
                name        = result[1],
                desc        = result[2],
                groupable   = result[3],
                active      = result[4],
                added_ts    = result[5],
                modified_ts = result[6]
            ))
        return results

    def get_all_media_status(self, limit: int, offset: int, alfabetic: bool) -> List[MediaStatus]:
        sentence = f'select id, name, description, active, added_ts, modified_ts from "{MediaStatus.table_name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(MediaStatus(
                id_         = result[0],
                name        = result[1],
                desc        = result[2],
                added_ts    = result[3],
                modified_ts = result[4]
            ))
        return results

    def get_all_media(self, limit: int, offset: int, alfabetic: bool) -> List[Media]:
        sentence = f'select id, name, description, year_start, year_end, id_type, id_status, active, added_ts, modified_ts from "{Media.table_name}"'
        if alfabetic: sentence += ' order by name asc'
        if limit != None and offset != None: sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(Media(
                    id_         = result[0],
                    name        = result[1],
                    desc        = result[2],
                    year_start  = result[3],
                    year_end    = result[4],
                    type_       = self.get_media_type_by_id(result[5]),
                    status      = self.get_media_status_by_id(result[6]),
                    active      = result[7],
                    added_ts    = result[8],
                    modified_ts = result[9]
            ))
        return results


    # GET BY X
    def get_by_id(self, table_name: str, id_: int) -> Union[None, MediaType, MediaStatus, Media]:
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
        sql_result = self.get_cur_db().execute(f'select id, name, description, groupable, active, added_ts, modified_ts from "{MediaType.table_name}" where id={id_}').fetchone()
        if sql_result:
            return MediaType(
                id_         = sql_result[0],
                name        = sql_result[1],
                desc        = sql_result[2],
                groupable   = sql_result[3],
                active      = sql_result[4],
                added_ts    = sql_result[5],
                modified_ts = sql_result[6]
            )

    def get_media_status_by_id(self, id_: int) -> Union[None, MediaStatus]:
        sql_result = self.get_cur_db().execute(f'select id, name, description, active, added_ts, modified_ts from "{MediaStatus.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return MediaStatus(
                id_         = sql_result[0],
                name        = sql_result[1],
                desc        = sql_result[2],
                added_ts    = sql_result[3],
                modified_ts = sql_result[4]
            )

    def get_media_by_id(self, id_: int) -> Union[None, Media]:
        sql_result = self.get_cur_db().execute(f'select id, name, description, year_start, year_end, id_type, id_status, active, added_ts, modified_ts from "{Media.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return Media(
                    id_         = sql_result[0],
                    name        = sql_result[1],
                    desc        = sql_result[2],
                    year_start  = sql_result[3],
                    year_end    = sql_result[4],
                    type_       = self.get_media_type_by_id(sql_result[5]),
                    status      = self.get_media_status_by_id(sql_result[6]),
                    active      = sql_result[7],
                    added_ts    = sql_result[8],
                    modified_ts = sql_result[9]
            )

    def get_media_group_by_nk(self, obj: MediaGroup) -> Union[None, MediaGroup]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   MediaGroup
            └ The MediaGroup object to use in the search.
        @ Output:
        ╠═  MediaGroup   -   The element of the table discriminated by natural key.
        ╚═  None         -   If no matches exists.
        """
        sql_result = self.get_cur_db().execute(f'select id, name, description, number, year_start, year_end, id_media, active, added_ts, modified_ts from "{MediaGroup.table_name}" where number="{obj.number}" and id_media="{obj.media.id_}"').fetchone()
        if sql_result:
            return MediaGroup(
                    id_         =   sql_result[0],
                    name        =   sql_result[1],
                    desc        =   sql_result[2],
                    number      =   sql_result[3],
                    year_start  =   sql_result[4],
                    year_end    =   sql_result[5],
                    media       =   self.get_media_by_id(sql_result[6]),
                    active      =   sql_result[7],
                    added_ts    =   sql_result[8],
                    modified_ts =   sql_result[9]
            )

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
        sentence = f'select id, name, description, number, year_start, year_end, id_media, active, added_ts, modified_ts from "{MediaGroup.table_name}" where id_media="{id_}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(MediaGroup(
                    id_         =   result[0],
                    name        =   result[1],
                    desc        =   result[2],
                    number      =   result[3],
                    year_start  =   result[4],
                    year_end    =   result[5],
                    media       =   self.get_media_by_id(result[6]),
                    active      =   result[7],
                    added_ts    =   result[8],
                    modified_ts =   result[9]
            ))
        return results


    def get_by_name(self, table_name: str, name: str, limit: int = None,
                    offset: int = 0, alfabetic: bool = False
                    ) -> Union[None, List[Union[MediaType, MediaStatus]]]:
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
        sentence = f'select id, name, description, groupable, active, added_ts, modified_ts from {MediaType.table_name} where name="{name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(MediaType(
                id_         = result[0],
                name        = result[1],
                desc        = result[2],
                groupable   = result[3],
                active      = result[4],
                added_ts    = result[5],
                modified_ts = result[6]
            ))
        return results

    def get_by_media_status_name(self, name: str, limit: int, offset: int, alfabetic: bool) -> List[MediaStatus]:
        sentence = f'select id, name, description, active, added_ts, modified_ts from {MediaStatus.table_name} where name="{name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(MediaStatus(
                id_         = result[0],
                name        = result[1],
                desc        = result[2],
                added_ts    = result[3],
                modified_ts = result[4]
            ))
        return results


    # INSERT
    def insert(self, obj: Union[MediaStatus, MediaType, Media, MediaGroup, MediaIssue, Platform]
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
        self.get_cur_db().execute(f'insert into "{MediaStatus.table_name}" (name, active) values (?, ?)', (obj.name, obj.active))

    def insert_media_type(self, obj: MediaType) -> None:
        self.get_cur_db().execute(f'insert into "{MediaType.table_name}" (name, groupable, active) values (?, ?, ?)', (obj.name, obj.groupable, obj.active))

    def insert_media(self, obj: Media) -> None:
        self.get_cur_db().execute(f'insert into "{Media.table_name}" (name, description, year_start, year_end, id_type, id_status, active) values (?, ?, ?, ?, ?, ?, ?)', (obj.name, obj.desc, obj.year_start, obj.year_end, obj.type_.id_, obj.status.id_, obj.active))

    def insert_media_group(self, obj: MediaGroup) -> None:
        self.get_cur_db().execute(f'insert into "{MediaGroup.table_name}" (name, description, number, year_start, year_end, id_media, active) values (?, ?, ?, ?, ?, ?, ?)', (obj.name, obj.desc, obj.number, obj.year_start, obj.year_end, obj.media.id_, obj.active))

    def insert_media_issue(self, obj: MediaGroup) -> None:
        self.get_cur_db().execute(f'insert into "{MediaIssue.table_name}" (position, name, description, date, id_media, id_media_group, active) values (?, ?, ?, ?, ?, ?, ?)', (obj.position, obj.name, obj.desc, obj.date, obj.media.id_, obj.media_group.id_, obj.active))

    def insert_platform(self, obj: Platform) -> None:
        self.get_cur_db().execute(f'insert into "{Platform.table_name}" (name, description, active) values (?, ?, ?)', (obj.name, obj.desc, obj.active))

# ------------------------------------------------------------------------------
