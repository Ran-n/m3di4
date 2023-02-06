#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/02/05 21:33:30.470100
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
# ------------------------------------------------------------------------------
class Sqlite(iModel):
    def __init__(self, ficheiro: str) -> None:
        logging.info(_('Starting the sqlite db'))
        self.ficheiro = ficheiro
        self.conn = None
        self.cur = None

        # if the DB doesnt have all the number of supposed tables, run the creation script.
        if(self.__get_num_tables_db() < Config().get_num_entities()):
            logging.info(_('Creating the sqlite db'))
            self.cur.executescript(''.join(load_file('./src/model/db_creation/sqlite/Media4.db.sql')))

    def __get_num_tables_db(self) -> int:
        self.connect_db()
        return self.cur.execute('select count(*) from sqlite_master where type="table"').fetchone()[0];

    def get_conn_db(self) -> Connection:
        if self.conn == None:
            return self.connect_db()[0]
        return self.conn

    def get_cur_db(self) -> Cursor:
        if self.cur == None:
            return self.connect_db()[1]
        return self.cur

    def connect_db(self) -> tuple([Connection, Cursor]):
        self.conn = sqlite3.connect(self.ficheiro)
        self.cur = self.conn.cursor()
        logging.info(_('Creating connection and cursor to the sqlite db'))
        return (self.conn, self.cur)

    def disconnect_db(self, commit: bool = True) -> None:
        if self.conn:
            if commit:
                self.conn.commit()
            self.conn.close()
            self.conn = None
            self.cur = None
        logging.info(_('Disconnecting from the sqlite db'))

    def save_db(self) -> None:
        if self.conn:
            self.conn.commit()
            logging.info(_('Saving the sqlite db'))


    # EXISTS
    def exists(self, obj: MediaGroup) -> bool:
        pass

    def exists_media_group(self, obj: MediaGroup) -> bool:
        sql_result = self.get_cur_db().execute(f'select id from "{MediaGroup.table_name}" where id_media="{obj.media.id_}" and number="{obj.number}"').fetchall()
        if len(sql_result) > 0:
            return True
        return False

    # GET NUM
    def get_num(self, table_name: str) -> int:
        return self.get_cur_db().execute(f'select count(*) from "{table_name}"').fetchone()[0]

    # GET
    def get_all(self, table_name: str, limit: int = None, offset: int = 0, alfabetic: bool = False) -> List[Union[MediaType, MediaStatus]]:
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
        sentence = f'select id, name, year_start, year_end, id_type, id_status, active, added_ts, modified_ts from "{Media.table_name}"'
        if alfabetic: sentence += ' order by name asc'
        if limit != None and offset != None: sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(Media(
                    id_         = result[0],
                    name        = result[1],
                    year_start  = result[2],
                    year_end    = result[3],
                    type_       = self.get_by_media_type_id(result[4]),
                    status      = self.get_by_media_status_id(result[5]),
                    active      = result[6],
                    added_ts    = result[7],
                    modified_ts = result[8]
            ))
        return results


    # GET BY X
    def get_by_id(self, table_name: str, id_: int) -> Media:
        pass

    def get_by_media_type_id(self, id_: int) -> MediaType:
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

    def get_by_media_status_id(self, id_: int) -> MediaStatus:
        sql_result = self.get_cur_db().execute(f'select id, name, description, active, added_ts, modified_ts from "{MediaStatus.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return MediaStatus(
                id_         = sql_result[0],
                name        = sql_result[1],
                desc        = sql_result[2],
                added_ts    = sql_result[3],
                modified_ts = sql_result[4]
            )

    def get_by_media_id(self, id_: int) -> Media:
        sql_result = self.get_cur_db().execute(f'select id, name, year_start, year_end, id_type, id_status, active, added_ts, modified_ts from "{Media.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return Media(
                    id_         = sql_result[0],
                    name        = sql_result[1],
                    year_start  = sql_result[2],
                    year_end    = sql_result[3],
                    type_       = self.get_by_media_type_id(sql_result[4]),
                    status      = self.get_by_media_status_id(sql_result[5]),
                    active      = sql_result[6],
                    added_ts    = sql_result[7],
                    modified_ts = sql_result[8]
            )

    def get_by_media_group_nk(self, obj: MediaGroup) -> MediaGroup:
        sql_result = self.get_cur_db().execute(f'select id, name, number, year_start, year_end, id_media, active, added_ts, modified_ts from "{MediaGroup.table_name}" where number="{obj.number}" and id_media="{obj.media.id_}"').fetchone()
        if sql_result:
            return MediaGroup(
                    id_         =   sql_result[0],
                    name        =   sql_result[1],
                    number      =   sql_result[2],
                    year_start  =   sql_result[3],
                    year_end    =   sql_result[4],
                    media       =   self.get_by_media_id(sql_result[5]),
                    active      =   sql_result[6],
                    added_ts    =   sql_result[7],
                    modified_ts =   sql_result[8]
            )


    def get_by_name(self, table_name: str, name: str, alfabetic: bool = False) -> List[Union[MediaType, MediaStatus]]:
        pass

    def get_by_media_type_name(self, name: str, alfabetic: bool) -> List[MediaType]:
        sentence = f'select id, name, description, groupable, active, added_ts, modified_ts from {MediaType.table_name} where name="{name}"'
        if alfabetic:
            sentence += ' order by name asc'
        db_results = self.get_cur_db().execute(sentence).fetchall()
        results = []
        for result in db_results:
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

    def get_by_media_status_name(self, name: str, alfabetic: bool) -> List[MediaStatus]:
        sentence = f'select id, name, description, active, added_ts, modified_ts from {MediaStatus.table_name} where name="{name}"'
        if alfabetic:
            sentence += ' order by name asc'
        db_results = self.get_cur_db().execute(sentence).fetchall()
        results = []
        for ele in db_results:
            results.append(MediaStatus(
                id_         = result[0],
                name        = result[1],
                desc        = result[2],
                added_ts    = result[3],
                modified_ts = result[4]
            ))
        return results


    # INSERT
    def insert(self, obj: Union[MediaStatus, MediaType, Media, MediaGroup, MediaIssue]) -> Union[None, int]:
        pass

    def insert_media_status(self, obj: MediaStatus) -> None:
        self.get_cur_db().execute(f'insert into "{MediaStatus.table_name}" (name, active) values (?, ?)', (obj.name, obj.active))

    def insert_media_type(self, obj: MediaType) -> None:
        self.get_cur_db().execute(f'insert into "{MediaType.table_name}" (name, groupable, active) values (?, ?, ?)', (obj.name, obj.groupable, obj.active))

    def insert_media(self, obj: Media) -> None:
        self.get_cur_db().execute(f'insert into "{Media.table_name}" (name, year_start, year_end, id_type, id_status, active) values (?, ?, ?, ?, ?, ?)', (obj.name, obj.year_start, obj.year_end, obj.type_.id_, obj.status.id_, obj.active))

    def insert_media_group(self, obj: MediaGroup) -> None:
        self.get_cur_db().execute(f'insert into "{MediaGroup.table_name}" (id, name, number, year_start, year_end, id_media, active) values (?, ?, ?, ?, ?, ?, ?)', (obj.id_, obj.name, obj.number, obj.year_start, obj.year_end, obj.media.id_, obj.active))

# ------------------------------------------------------------------------------
