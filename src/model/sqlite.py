#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/03/21 16:22:57.316952
# ------------------------------------------------------------------------------
#* Concrete Strategy (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.model import iModel
# ------------------------------------------------------------------------------
import sqlite3
from sqlite3 import Connection, Cursor, IntegrityError
from uteis.ficheiro import cargarFich as load_file
import logging
from typing import List, Union, Tuple

from src.utils import Config

from src.model.entity import Media, Group, Issue
from src.model.entity import Type, Status
from src.model.entity import Platform, ShareSite, ShareSiteSubs
from src.model.entity import Warehouse
from src.model.entity import Extension, Folder, App, Version, Encoder, File
from src.model.entity import Codec, Language, Track, TrackLanguage
from src.model.entity import LanguageCode, CodeName
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
            logging.info(_('Adding language information to the sqlite database'))
            self.cur.executescript(''.join(load_file('./src/model/db_scripts/sqlite/Media4.db.insert.languages.sql')))
            if Config().populate_db:
                logging.info(_('Populating the sqlite database with extra data'))
                self.cur.executescript(''.join(load_file('./src/model/db_scripts/sqlite/Media4.db.insert.extra.sql')))

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
    def exists(self, obj: Union[Group, Issue, Platform,
            Type, ShareSite, Warehouse,
            Extension, LanguageCode]) -> bool:
        """ Checks if a element is saved in the DB.
        @ Input:
        ╚═  · obj   -   Any Entity Object   -   True
            └ Object to check if it exists in the DB.

        @ Output:
        ╚═  bool    -   Indicating if the object exists or not.
        """
        pass

    def exists_group(self, obj: Group) -> bool:
        sql_result = self.get_cur_db().execute(f'select id from "{Group.table_name}" where id_media="{obj.media.id_}" and number="{obj.number}"').fetchall()
        if len(sql_result) > 0:
            return True
        return False

    def exists_issue(self, obj: Issue) -> bool:
        sql_result = self.get_cur_db().execute(f'select id from "{Issue.table_name}" where id_media="{obj.media.id_}" and id_group="{obj.group.id_}" and position="{obj.position}"').fetchall()
        if len(sql_result) > 0:
            return True
        return False

    def exists_platform(self, obj: Platform) -> bool:
        sql_result = self.get_cur_db().execute(f'select id from "{Platform.table_name}" where name like "{obj.name}"').fetchall()
        if len(sql_result) > 0:
            return True
        return False

    def exists_type(self, obj: Type) -> bool:
        sql_result = self.get_cur_db().execute(f'select id from "{Type.table_name}" where name like "{obj.name}"').fetchall()
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

    def exists_language_code(self, obj: LanguageCode) -> bool:
        """
        """
        sql_result = self.get_cur_db().execute(f'select id from "{LanguageCode.table_name}" \
                where codename like "{obj.codename}"').fetchall()
        if len(sql_result) > 0:
            return True
        return False
    # EXISTS #

    # GET NUM
    def get_num(self, table_name: str) -> int:
        """ Returns the number of elements in a table.
        @ Input:
        ╚═  · table_name    -   str, Tuple[str]
            └ Name/s of the table to query.
        @ Output:
        ╚═  int - Number of entries on the table/s.
        """
        return self.get_cur_db().execute(f'select count(*) from "{table_name}"').fetchone()[0]

    def get_num_type_of_x(self, table_name: str) -> int:
        """ Returns the number of elements in a table.
        @ Input:
        ╚═  · table_name    -   str
            └ Name of the table to query.
        @ Output:
        ╚═  int - Number of entries on the table.
        """
        return self.get_cur_db().execute(f'select count(distinct t.id) from "{Type.table_name}" t \
                right join {table_name} x on x.id_type=t.id').fetchone()[0]

    def get_group_num_by_media_id(self, media_id: int) -> int:
        """Returns the number of group elements discriminating by media id.
        @ Input:
        ╚═  · media_id  -   int
            └ Id of the media to use as a discriminator.
        @ Output:
        ╚═  int - Number of entries on the table that meet the criteria.
        """
        return self.get_cur_db().execute(f'select count(*) from "{Group.table_name}" where id_media = "{media_id}"').fetchone()[0]
    # GET NUM #

    # GET ALL
    def get_all(self, table_name: Union[str, Tuple[str, str]], limit: int = None,
                offset: int = 0, alfabetic: bool = False) -> List[Union[
                    Type, Status, Media, Platform, ShareSite, Issue, Warehouse]]:
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

    def get_all_type(self, table_name: Union[None, str], limit: int, offset: int, alfabetic: bool) -> List[Type]:
        if table_name is not None:
            sentence = f'select distinct t.id, t.active, t.name, t.groupable, t.added_ts, t.modified_ts \
                    from "{Type.table_name}" t right join "{table_name}" x on x.id_type=t.id'
        else:
            sentence = f'select distinct id, active, name, groupable, added_ts, modified_ts \
                    from "{Type.table_name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(Type(
                id_         = result[0],
                active      = result[1],
                name        = result[2],
                groupable   = result[3],
                added_ts    = result[4],
                modified_ts = result[5]
            ))
        return results

    def get_all_status(self, limit: int, offset: int, alfabetic: bool) -> List[Status]:
        sentence = f'select id, active, name, added_ts, modified_ts from "{Status.table_name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(Status(
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
                    type_       = self.get_type_by_id(result[5]),
                    status      = self.get_status_by_id(result[6]),
                    added_ts    = result[7],
                    modified_ts = result[8]
            ))
        return results

    def get_all_platform(self, limit: int, offset: int, alfabetic: bool) -> List[Platform]:
        """
        """
        sentence = f'select id, active, acronym, name, name_long, link, id_type, added_ts,\
                modified_ts from "{Platform.table_name}"'
        if alfabetic: sentence += ' order by name asc'
        if limit != None and offset != None: sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(Platform(
                    id_         = result[0],
                    active      = result[1],
                    acronym     = result[2],
                    name        = result[3],
                    name_long   = result[4],
                    link        = result[5],
                    type_       = self.get_type_by_id(result[6]),
                    added_ts    = result[7],
                    modified_ts = result[8]
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
                    type_           = self.get_type_by_id(result[6]),
                    platform        = self.get_platform_by_id(result[7]),
                    added_ts        = result[8],
                    modified_ts     = result[9]
            ))
        return results

    def get_all_issue(self, limit: int, offset: int, alfabetic: bool) -> List[Issue]:
        """
        """
        sentence = f'select id, active, position, name, date, id_media, id_group, added_ts, modified_ts from "{Issue.table_name}"'
        if alfabetic: sentence += ' order by name asc'
        if limit != None and offset != None: sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(Issue(
                    id_             = result[0],
                    active          = result[1],
                    position        = result[2],
                    name            = result[3],
                    date            = result[4],
                    media           = self.get_media_by_id(result[5]),
                    group     = self.get_group_by_id(result[6]),
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
                    type_       = self.get_type_by_id(result[6]),
                    health      = result[7],
                    added_ts    = result[8],
                    modified_ts = result[9]
            ))
        return results
    # GET ALL #

    # GET BY ID
    def get_by_id(self, table_name: str, id_: int) ->\
            Union[Type, Status, Media,
                  Platform, Group, App,
                  Extension, Warehouse, Folder, Issue,
                  Version, Encoder, File, Codec,
                  Track, Language]:
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

    def get_type_by_id(self, id_: int) -> Union[None, Type]:
        sql_result = self.get_cur_db().execute(f'select id, active, name, groupable, added_ts, \
                modified_ts from "{Type.table_name}" where id={id_}').fetchone()
        if sql_result:
            return Type(
                id_         = sql_result[0],
                active      = sql_result[1],
                name        = sql_result[2],
                groupable   = sql_result[3],
                added_ts    = sql_result[4],
                modified_ts = sql_result[5]
            )

    def get_status_by_id(self, id_: int) -> Union[None, Status]:
        sql_result = self.get_cur_db().execute(f'select id, active, name, added_ts, modified_ts from "{Status.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return Status(
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
                    type_       = self.get_type_by_id(sql_result[5]),
                    status      = self.get_status_by_id(sql_result[6]),
                    added_ts    = sql_result[7],
                    modified_ts = sql_result[8]
            )

    def get_platform_by_id(self, id_: int) -> Union[None, Platform]:
        """"""
        sql_result = self.get_cur_db().execute(f'select id, active, acronym, name, \
                name_long, link, id_type, added_ts, modified_ts from \
                "{Platform.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return Platform(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    acronym     = sql_result[2],
                    name        = sql_result[3],
                    name_long   = sql_result[4],
                    link        = sql_result[5],
                    type_       = self.get_type_by_id(sql_result[6]),
                    added_ts    = sql_result[7],
                    modified_ts = sql_result[8]
            )

    def get_group_by_id(self, id_: int) -> Union[None, Group]:
        sql_result = self.get_cur_db().execute(f'select id, active, number, name, year_start, \
                year_end, id_media, added_ts, modified_ts from "{Group.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return Group(
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
                    type_       = self.get_type_by_id(sql_result[6]),
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

    def get_issue_by_id(self, id_: int) -> Issue:
        sql_result = self.get_cur_db().execute(f'select id, active, position, \
                name, date, id_media, id_group, added_ts, modified_ts \
                from "{Issue.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return Issue(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    position    = sql_result[2],
                    name        = sql_result[3],
                    date        = sql_result[4],
                    media       = self.get_media_by_id(sql_result[5]),
                    group = self.get_group_by_id(sql_result[6]),
                    added_ts    = sql_result[7],
                    modified_ts = sql_result[8]
            )

    def get_version_by_id(self, id_: int) -> Version:
        sql_result = self.get_cur_db().execute(f'select id, active, number, name, \
                num_bit_processor, added_ts, modified_ts from "{Version.table_name}" \
                where id="{id_}"').fetchone()
        if sql_result:
            return Version(
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

    def get_file_by_id(self, id_: int) -> File:
        sql_result = self.get_cur_db().execute(f'select id, active, hash, name, id_extension, \
                id_warehouse, id_folder, id_media, id_issue, title, nb_streams, \
                nb_programs, start, duration, size, bit_rate, probe_score, creation_ts, \
                id_version, id_encoder, original_name, added_ts, modified_ts \
                from "{File.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return File(
                    id_             = sql_result[0],
                    active          = sql_result[1],
                    hash_           = sql_result[2],
                    name            = sql_result[3],
                    extension       = self.get_extension_by_id(sql_result[4]),
                    warehouse       = self.get_warehouse_by_id(sql_result[5]),
                    folder          = self.get_folder_by_id(sql_result[6]),
                    media           = self.get_media_by_id(sql_result[7]),
                    issue     = self.get_issue_by_id(sql_result[8]),
                    title           = sql_result[9],
                    nb_streams      = sql_result[10],
                    start           = sql_result[11],
                    duration        = sql_result[12],
                    size            = sql_result[13],
                    bit_rate        = sql_result[14],
                    probe_score     = sql_result[15],
                    creation_ts     = sql_result[16],
                    version     = self.get_version_by_id(sql_result[17]),
                    encoder         = self.get_encoder_by_id(sql_result[18]),
                    original_name   = sql_result[19],
                    added_ts        = sql_result[20],
                    modified_ts     = sql_result[21]
            )

    def get_codec_by_id(self, id_: int) -> Codec:
        sql_result = self.get_cur_db().execute(f'select id, active, name, name_long, \
                id_type, added_ts, modified_ts from "{Codec.table_name}" \
                where id="{id_}"').fetchone()
        if sql_result:
            return Codec(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    name        = sql_result[2],
                    name_long   = sql_result[3],
                    type_       = self.get_type_by_id(sql_result[4]),
                    added_ts    = sql_result[5],
                    modified_ts = sql_result[6]
            )

    def get_track_by_id(self, id_: int) -> Track:
        sql_result = self.get_cur_db().execute(f'select id, active, id_file, id_codec, index_, title, profile, \
                quality, width, height, coded_width, coded_height, closed_captions, film_grain, has_b_frames, \
                sample_aspect_ratio, display_aspect_ratio, pixel_format, level, color, color_range, color_space, \
                color_transfer, color_primaries, chroma_location, field_order, refs, is_avc, nal_length_size, \
                r_frame_rate, avg_frame_rate, time_base, start_pts, bits_per_raw_sample, bits_per_sample, \
                extradata_size, default_, dub, original, comment, lyrics, karaoke, forced, hearing_impaired, \
                visual_impaired, clean_effects, attached_pic, timed_thumbnails, captions, descriptions, metadata, \
                dependent, still_image, start, duration, size, bit_rate, sample_rate, sample_format, channels, \
                channel_layout, bps, frame_number, dmix_mode, text_subtitle, added_ts, modified_ts \
                from "{Track.table_name}" where id="{id_}"').fetchone()
        if sql_result:
            return Track(
                    id_                     = sql_result[0],
                    active                  = sql_result[1],
                    file                    = self.get_file_by_id(sql_result[2]),
                    codec                   = self.get_codec_by_id(sql_result[3]),
                    index                   = sql_result[4],
                    title                   = sql_result[5],
                    profile                 = sql_result[6],
                    quality                 = sql_result[7],
                    width                   = sql_result[8],
                    height                  = sql_result[9],
                    coded_width             = sql_result[10],
                    coded_height            = sql_result[11],
                    closed_captions         = sql_result[12],
                    film_grain              = sql_result[13],
                    has_b_frames            = sql_result[14],
                    sample_aspect_ratio     = sql_result[15],
                    display_aspect_ratio    = sql_result[16],
                    pixel_format            = sql_result[17],
                    level                   = sql_result[18],
                    color                   = sql_result[19],
                    color_range             = sql_result[20],
                    color_space             = sql_result[21],
                    color_transfer          = sql_result[22],
                    color_primaries         = sql_result[23],
                    chroma_location         = sql_result[24],
                    field_order             = sql_result[25],
                    refs                    = sql_result[26],
                    is_avc                  = sql_result[27],
                    nal_length_size         = sql_result[28],
                    r_frame_rate            = sql_result[29],
                    avg_frame_rate          = sql_result[30],
                    time_base               = sql_result[31],
                    start_pts               = sql_result[32],
                    bits_per_raw_sample     = sql_result[33],
                    bits_per_sample         = sql_result[34],
                    extradata_size          = sql_result[35],
                    default                 = sql_result[36],
                    dub                     = sql_result[37],
                    original                = sql_result[38],
                    comment                 = sql_result[39],
                    lyrics                  = sql_result[40],
                    karaoke                 = sql_result[41],
                    forced                  = sql_result[42],
                    hearing_impaired        = sql_result[43],
                    visual_impaired         = sql_result[44],
                    clean_effects           = sql_result[45],
                    attached_pic            = sql_result[46],
                    timed_thumbnails        = sql_result[47],
                    captions                = sql_result[48],
                    descriptions            = sql_result[49],
                    metadata                = sql_result[50],
                    dependent               = sql_result[51],
                    still_image             = sql_result[52],
                    start                   = sql_result[53],
                    duration                = sql_result[54],
                    size                    = sql_result[55],
                    bit_rate                = sql_result[56],
                    sample_rate             = sql_result[57],
                    sample_format           = sql_result[58],
                    channels                = sql_result[59],
                    channel_layout          = sql_result[60],
                    bps                     = sql_result[61],
                    frame_number            = sql_result[62],
                    dmix_mode               = sql_result[63],
                    text_subtitle           = sql_result[64],
                    added_ts                = sql_result[65],
                    modified_ts             = sql_result[66]
            )

    def get_language_by_id(self, id_: int) -> Language:
        sql_result = self.get_cur_db().execute(f'select id, active, name, \
                id_language, added_ts, modified_ts from "{Language.table_name}" \
                where id="{id_}"').fetchone()
        if sql_result:
            return Language(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    name        = sql_result[2],
                    language    = self.get_language_by_id(sql_result[3]),
                    added_ts    = sql_result[4],
                    modified_ts = sql_result[5]
            )
    # GET BY ID

    # GET BY NK
    def get_by_nk(self, obj: Union[Group, Version, Encoder, File, Type, Codec]) -> \
            Union[None, Group, Version, Encoder, File, Type, Codec, Track,
                  Language, TrackLanguage]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   Entity
            └ The Entity object to use in the search.
        @ Output:
        ╠═  Any Entity  -   The element of the table discriminated by natural key.
        ╚═  None        -   If no matches exists.
        """
        pass

    def get_group_by_nk(self, obj: Group) -> Union[None, Group]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   Group
            └ The Group object to use in the search.
        @ Output:
        ╠═  Group   -   The element of the table discriminated by natural key.
        ╚═  None         -   If no matches exists.
        """
        sql_result = self.get_cur_db().execute(f'select id, active, name, number, year_start, year_end, id_media, added_ts, modified_ts from "{Group.table_name}" where number="{obj.number}" and id_media="{obj.media.id_}"').fetchone()
        if sql_result:
            return Group(
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

    def get_version_by_nk(self, obj: Version) -> Union[None, Version]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   Version
            └ The Version object to use in the search.
        @ Output:
        ╠═  Version  -   The element of the table discriminated by natural key.
        ╚═  None        -   If no matches exists.
        """
        sql_result = self.get_cur_db().execute(f'select id, active, id_app, number, name, num_bit_processor, \
                added_ts, modified_ts from "{Version.table_name}" where id_app="{obj.app.id_}"\
                and number="{obj.number}"').fetchone()
        if sql_result:
            return Version(
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
        sql_result = self.get_cur_db().execute(f'select id, active, hash, name, id_extension, \
                id_warehouse, id_folder, id_media, id_issue, title, nb_streams, \
                nb_programs, start, duration, size, bit_rate, probe_score, creation_ts, \
                id_version, id_encoder, original_name, added_ts, modified_ts \
                from "{File.table_name}" where name="{obj.name}" and \
                id_extension="{obj.extension.id_}" and id_folder="{obj.folder.id_}" and \
                id_warehouse="{obj.warehouse.id_}"').fetchone()
        if sql_result:
            return File(
                    id_             = sql_result[0],
                    active          = sql_result[1],
                    hash_           = sql_result[2],
                    name            = sql_result[3],
                    extension       = self.get_extension_by_id(sql_result[4]),
                    warehouse       = self.get_warehouse_by_id(sql_result[5]),
                    folder          = self.get_folder_by_id(sql_result[6]),
                    media           = self.get_media_by_id(sql_result[7]),
                    issue     = self.get_issue_by_id(sql_result[8]),
                    title           = sql_result[9],
                    nb_streams      = sql_result[10],
                    start           = sql_result[11],
                    duration        = sql_result[12],
                    size            = sql_result[13],
                    bit_rate        = sql_result[14],
                    probe_score     = sql_result[15],
                    creation_ts     = sql_result[16],
                    version     = self.get_version_by_id(sql_result[17]),
                    encoder         = self.get_encoder_by_id(sql_result[18]),
                    original_name   = sql_result[19],
                    added_ts        = sql_result[20],
                    modified_ts     = sql_result[21]
            )

    def get_type_by_nk(self, obj: Type) -> Union[None, Type]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   Type
            └ The Version object to use in the search.
        @ Output:
        ╠═  Type    -   The element of the table discriminated by natural key.
        ╚═  None    -   If no matches exists.
        """
        sql_result = self.get_cur_db().execute(f'select id, active, name, added_ts, \
                modified_ts from "{Type.table_name}" where name="{obj.name}"').fetchone()
        if sql_result:
            return Type(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    name        = sql_result[2],
                    added_ts    = sql_result[3],
                    modified_ts = sql_result[4]
            )

    def get_codec_by_nk(self, obj: Codec) -> Union[None, Codec]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   Codec
            └ The Version object to use in the search.
        @ Output:
        ╠═  Codec   -   The element of the table discriminated by natural key.
        ╚═  None    -   If no matches exists.
        """
        sql_result = self.get_cur_db().execute(f'select id, active, name, name_long, \
                id_type, added_ts, modified_ts from "{Codec.table_name}" \
                where name="{obj.name}" or name_long="{obj.name_long}"').fetchone()
        if sql_result:
            return Codec(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    name        = sql_result[2],
                    name_long   = sql_result[3],
                    type_       = self.get_type_by_id(sql_result[4]),
                    added_ts    = sql_result[5],
                    modified_ts = sql_result[6]
            )

    def get_track_by_nk(self, obj: Track) -> Union[None, Track]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   Track
            └ The Version object to use in the search.
        @ Output:
        ╠═  Track  -   The element of the table discriminated by natural key.
        ╚═  None        -   If no matches exists.
        """
        sql_result = self.get_cur_db().execute(f'select id, active, id_file, id_codec, index_, title, profile, \
                quality, width, height, coded_width, coded_height, closed_captions, film_grain, has_b_frames, \
                sample_aspect_ratio, display_aspect_ratio, pixel_format, level, color, color_range, color_space, \
                color_transfer, color_primaries, chroma_location, field_order, refs, is_avc, nal_length_size, \
                r_frame_rate, avg_frame_rate, time_base, start_pts, bits_per_raw_sample, bits_per_sample, \
                extradata_size, default_, dub, original, comment, lyrics, karaoke, forced, hearing_impaired, \
                visual_impaired, clean_effects, attached_pic, timed_thumbnails, captions, descriptions, metadata, \
                dependent, still_image, start, duration, size, bit_rate, sample_rate, sample_format, channels, \
                channel_layout, bps, frame_number, dmix_mode, text_subtitle, added_ts, modified_ts \
                from "{Track.table_name}" where id_file="{obj.file.id_}" and index_="{obj.index}"').fetchone()
        if sql_result:
            return Track(
                    id_                     = sql_result[0],
                    active                  = sql_result[1],
                    file                    = self.get_file_by_id(sql_result[2]),
                    codec                   = self.get_codec_by_id(sql_result[3]),
                    index                   = sql_result[4],
                    title                   = sql_result[5],
                    profile                 = sql_result[6],
                    quality                 = sql_result[7],
                    width                   = sql_result[8],
                    height                  = sql_result[9],
                    coded_width             = sql_result[10],
                    coded_height            = sql_result[11],
                    closed_captions         = sql_result[12],
                    film_grain              = sql_result[13],
                    has_b_frames            = sql_result[14],
                    sample_aspect_ratio     = sql_result[15],
                    display_aspect_ratio    = sql_result[16],
                    pixel_format            = sql_result[17],
                    level                   = sql_result[18],
                    color                   = sql_result[19],
                    color_range             = sql_result[20],
                    color_space             = sql_result[21],
                    color_transfer          = sql_result[22],
                    color_primaries         = sql_result[23],
                    chroma_location         = sql_result[24],
                    field_order             = sql_result[25],
                    refs                    = sql_result[26],
                    is_avc                  = sql_result[27],
                    nal_length_size         = sql_result[28],
                    r_frame_rate            = sql_result[29],
                    avg_frame_rate          = sql_result[30],
                    time_base               = sql_result[31],
                    start_pts               = sql_result[32],
                    bits_per_raw_sample     = sql_result[33],
                    bits_per_sample         = sql_result[34],
                    extradata_size          = sql_result[35],
                    default                 = sql_result[36],
                    dub                     = sql_result[37],
                    original                = sql_result[38],
                    comment                 = sql_result[39],
                    lyrics                  = sql_result[40],
                    karaoke                 = sql_result[41],
                    forced                  = sql_result[42],
                    hearing_impaired        = sql_result[43],
                    visual_impaired         = sql_result[44],
                    clean_effects           = sql_result[45],
                    attached_pic            = sql_result[46],
                    timed_thumbnails        = sql_result[47],
                    captions                = sql_result[48],
                    descriptions            = sql_result[49],
                    metadata                = sql_result[50],
                    dependent               = sql_result[51],
                    still_image             = sql_result[52],
                    start                   = sql_result[53],
                    duration                = sql_result[54],
                    size                    = sql_result[55],
                    bit_rate                = sql_result[56],
                    sample_rate             = sql_result[57],
                    sample_format           = sql_result[58],
                    channels                = sql_result[59],
                    channel_layout          = sql_result[60],
                    bps                     = sql_result[61],
                    frame_number            = sql_result[62],
                    dmix_mode               = sql_result[63],
                    text_subtitle           = sql_result[64],
                    added_ts                = sql_result[65],
                    modified_ts             = sql_result[66]
            )

    # xFCR ??
    def get_language_by_nk(self, obj: Language) -> Union[None, Language]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   Language
            └ The Version object to use in the search.
        @ Output:
        ╠═  Language    -   The element of the table discriminated by natural key.
        ╚═  None        -   If no matches exists.
        """
        sql_result = self.get_cur_db().execute(f'select id, active, name, \
                id_language, added_ts, modified_ts from "{Language.table_name}" \
                where name="{obj.name}"').fetchone()
        if sql_result:
            return Language(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    name        = sql_result[2],
                    id_language = self.get_language_by_id(sql_result[3]),
                    added_ts    = sql_result[4],
                    modified_ts = sql_result[5]
            )

    def get_track_language_by_nk(self, obj: TrackLanguage) -> Union[None, TrackLanguage]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   TrackLanguage
            └ The TrackLanguage to use in the search.
        @ Output:
        ╠═  TrackLanguage      -   The element of the table discriminated by natural key.
        ╚═  None                    -   If no matches exists.
        """
        sql_result = self.get_cur_db().execute(f'select id, active, id_track, \
                id_language, added_ts, modified_ts from "{TrackLanguage.table_name}"\
                where id_track="{obj.track.id_}" and id_language="{obj.language.id_}"').fetchone()
        if sql_result:
            return TrackLanguage(
                    id_         = sql_result[0],
                    active      = sql_result[1],
                    track = self.get_track_by_id(sql_result[2]),
                    language    = self.get_language_by_id(sql_result[3]),
                    added_ts    = sql_result[4],
                    modified_ts = sql_result[5]
            )
    # GET BY NK #

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
        sentence = f'select id, active, name, number, year_start, year_end, id_media, added_ts, modified_ts from "{Group.table_name}" where id_media="{id_}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(Group(
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

    def get_language_by_codename(self, codename: str) -> Union[None, Language]:
        """ Returns a language discriminated by the given codename.
        If a new code is added that makes it so codenames are reused
        for different languages this function must be rewritten.
        @ Input:
        ╠═  · codename  -   str
        ║   └ Code that identifies the language in some system.
        ╠═  · bcp47     -   bool    -   False
        ║   └ Identifies the codename as a bcp47 value.
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
        # This should only return one result even without the bcp47 modifier
        sentence = f'select distinct l.id, l.active, l.name, l.id_language, l.added_ts, l.modified_ts \
                from "{Language.table_name}" l left join "{LanguageCode.table_name}" lc on lc.id_language=l.id \
                where lc.codename=?'
        sentence_bcp47 = sentence + f' and lc.id_code=(select code_id from "{CodeName.table_name}" where name=?)'

        sql_result_bcp47 = self.get_cur_db().execute(sentence_bcp47, (codename, 'BCP 47')).fetchone()

        if sql_result_bcp47:
            sql_result = sql_result_bcp47
        else:
            sql_result = self.get_cur_db().execute(sentence, (codename,)).fetchone()

        # ^ that logic means that first it looks for the bcp47 code and if it doesnt exist
        # looks for any code that matches.

        if sql_result:
            return Language(
                    id_         =   sql_result[0],
                    active      =   sql_result[1],
                    name        =   sql_result[2],
                    language    =   self.get_language_by_id(sql_result[3]),
                    added_ts    =   sql_result[4],
                    modified_ts =   sql_result[5]
            )
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
        pass

    # xfcr
    def get_by_type_name(self, name: str, limit: int, offset: int, alfabetic: bool) -> List[Type]:
        sentence = f'select id, active, name, groupable, added_ts, modified_ts from {Type.table_name} where name="{name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(Type(
                id_         = result[0],
                active      = result[1],
                name        = result[2],
                groupable   = result[3],
                added_ts    = result[4],
                modified_ts = result[5]
            ))
        return results

    # xfcr
    def get_by_status_name(self, name: str, limit: int, offset: int, alfabetic: bool) -> List[Status]:
        sentence = f'select id, active, name, added_ts, modified_ts from {Status.table_name} where name="{name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_results = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for result in sql_results:
            results.append(Status(
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

    def get_language_by_name(self, name: str, limit: int, offset: int, alfabetic: bool) -> Union[None, List[Language]]:
        sentence = f'select distinct id_language from {LanguageName.table_name} where name like "{name}"'
        if alfabetic:
            sentence += ' order by name asc'
        if limit != None and offset != None:
            sentence += f' LIMIT {limit} OFFSET {offset}'

        sql_language_names = self.get_cur_db().execute(sentence).fetchall()

        results = []
        for language_name in sql_language_names:
            results.append(self.get_language_by_id(language_name[0]))
        if results: return results
    # GET BY NAME #

    # INSERT
    def insert(self, obj: Union[Status, Type, Media, Group,
                                Issue, Platform, ShareSite,
                                Warehouse, Extension, Folder, App,
                                Version, Encoder, Codec, Track,
                                TrackLanguage]
               ) -> None:
        """ Adds an element to a DB table.
        @ Input:
        ╚═  · obj   -   Any Entity Type
            └ Entity to insert in the DB.
        @ Output:
        ╚═  None
        """
        pass

    def insert_status(self, obj: Status) -> None:
        self.get_cur_db().execute(f'insert into "{Status.table_name}" (active, name) values (?, ?)', (obj.active, obj.name))

    def insert_type(self, obj: Type) -> None:
        self.get_cur_db().execute(f'insert into "{Type.table_name}" (active, name, groupable) values (?, ?, ?)', (obj.active, obj.name, obj.groupable))

    def insert_media(self, obj: Media) -> None:
        self.get_cur_db().execute(f'insert into "{Media.table_name}" (active, name, year_start, year_end, id_type, id_status) values (?, ?, ?, ?, ?, ?)', (obj.active, obj.name, obj.year_start, obj.year_end, obj.type_.id_, obj.status.id_))

    def insert_group(self, obj: Group) -> None:
        self.get_cur_db().execute(f'insert into "{Group.table_name}" (active, name, number, year_start, year_end, id_media) values (?, ?, ?, ?, ?, ?)', (obj.active, obj.name, obj.number, obj.year_start, obj.year_end, obj.media.id_))

    def insert_issue(self, obj: Group) -> None:
        self.get_cur_db().execute(f'insert into "{Issue.table_name}" (active, position, name, date, id_media, id_group) values (?, ?, ?, ?, ?, ?)', (obj.active, obj.position, obj.name, obj.date, obj.media.id_, obj.group.id_))

    def insert_platform(self, obj: Platform) -> None:
        self.get_cur_db().execute(f'insert into "{Platform.table_name}" \
                (active, acronym, name, name_long, link, id_type) values \
                (?, ?, ?, ?, ?, ?)', (obj.active, obj.acronym, obj.name,
                                      obj.name_long, obj.link, obj.type_.id_))

    def insert_sharesite(self, obj: ShareSite) -> None:
        self.get_cur_db().execute(f'insert into "{ShareSite.table_name}" (active, in_platform_id, name, private, link, id_type, id_platform) values (?, ?, ?, ?, ?, ?, ?)', (obj.active, obj.in_platform_id, obj.name, obj.private, obj.link, obj.type_.id_, obj.platform.id_))

    def insert_sharesite_subs(self, obj: ShareSiteSubs) -> None:
        self.get_cur_db().execute(f'insert into "{ShareSiteSubs.table_name}" (id_share_site, sub_num) values (?, ?)', (obj.share_site.id_, obj.sub_num))

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

    def insert_version(self, obj: Version) -> None:
        self.get_cur_db().execute(f'insert into "{Version.table_name}" \
                (active, id_app, number, name, num_bit_processor) \
                values (?, ?, ?, ?, ?)', (obj.active, obj.app.id_, obj.number,
                                          obj.name, obj.num_bit_processor))

    def insert_encoder(self, obj: Encoder) -> None:
        self.get_cur_db().execute(f'insert into "{Encoder.table_name}" \
                (active, name) values (?, ?)', (obj.active, obj.name))

    def insert_file(self, obj: File) -> None:
        id_media=None
        if obj.media: id_media=obj.media.id_
        id_issue=None
        if obj.issue: id_issue=obj.issue.id_
        id_version=None
        if obj.version: id_version=obj.version.id_
        id_encoder=None
        if obj.encoder: id_encoder=obj.encoder.id_

        self.get_cur_db().execute(f'insert into "{File.table_name}" \
                (active, hash, name, id_extension, id_warehouse, id_folder, id_media, \
                id_issue, title, nb_streams, nb_programs, start, duration, \
                size, bit_rate, probe_score, creation_ts, id_version, id_encoder, \
                original_name) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
                ?, ?, ?, ?, ?, ?, ?)', (obj.active, obj.hash_, obj.name, obj.extension.id_,
                                     obj.warehouse.id_, obj.folder.id_, id_media,
                                     id_issue, obj.title, obj.nb_streams,
                                     obj.nb_programs, obj.start, obj.duration, obj.size,
                                     obj.bit_rate, obj.probe_score, obj.creation_ts,
                                     id_version, id_encoder, obj.original_name))

    def insert_codec(self, obj: Codec) -> None:
        self.get_cur_db().execute(f'insert into "{Codec.table_name}" \
                (active, name, name_long, id_type) values (?, ?, ?, ?)',
                                  (obj.active, obj.name, obj.name_long, obj.type_.id_))

    def insert_track(self, obj: Track) -> None:
        self.get_cur_db().execute(f'insert into "{Track.table_name}" (active, \
                id_file, id_codec, index_, title, profile, quality, width, height, \
                coded_width, coded_height, closed_captions, film_grain, has_b_frames, \
                sample_aspect_ratio, display_aspect_ratio, pixel_format, level, color, \
                color_range, color_space, color_transfer, color_primaries, chroma_location, \
                field_order, refs, is_avc, nal_length_size, r_frame_rate, avg_frame_rate, \
                time_base, start_pts, bits_per_raw_sample, bits_per_sample, extradata_size, \
                default_, dub, original, comment, lyrics, karaoke, forced, hearing_impaired, \
                visual_impaired, clean_effects, attached_pic, timed_thumbnails, captions, \
                descriptions, metadata, dependent, still_image, start, duration, size, \
                bit_rate, sample_rate, sample_format, channels, channel_layout, bps, \
                frame_number, dmix_mode, text_subtitle) values (?, ?, ?, ?, ?, ?, ?, ?, ?\
                , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?\
                , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?\
                , ?, ?, ?, ?, ?)', (obj.active, obj.file.id_, obj.codec.id_, obj.index,
                                    obj.title, obj.profile, obj.quality, obj.width, obj.height,
                                    obj.coded_width, obj.coded_height, obj.closed_captions, obj.film_grain,
                                    obj.has_b_frames, obj.sample_aspect_ratio, obj.display_aspect_ratio,
                                    obj.pixel_format, obj.level, obj.color, obj.color_range, obj.color_space,
                                    obj.color_transfer, obj.color_primaries, obj.chroma_location,
                                    obj.field_order, obj.refs, obj.is_avc, obj.nal_length_size,
                                    obj.r_frame_rate, obj.avg_frame_rate, obj.time_base, obj.start_pts,
                                    obj.bits_per_raw_sample, obj.bits_per_sample, obj.extradata_size,
                                    obj.default, obj.dub, obj.original, obj.comment, obj.lyrics,
                                    obj.karaoke, obj.forced, obj.hearing_impaired, obj.visual_impaired,
                                    obj.clean_effects, obj.attached_pic, obj.timed_thumbnails, obj.captions,
                                    obj.descriptions, obj.metadata, obj.dependent, obj.still_image,
                                    obj.start, obj.duration, obj.size, obj.bit_rate, obj.sample_rate,
                                    obj.sample_format, obj.channels, obj.channel_layout, obj.bps,
                                    obj.frame_number, obj.dmix_mode, obj.text_subtitle))

    def insert_track_language(self, obj: TrackLanguage) -> None:
        self.get_cur_db().execute(f'insert into "{TrackLanguage.table_name}" \
                (active, id_track, id_language) values (?, ?, ?)',
                                  (obj.active, obj.track.id_, obj.language.id_))
    # INSERT #
# ------------------------------------------------------------------------------
