#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/02/09 22:36:02.822194
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
# ------------------------------------------------------------------------------
class Model:
    def __init__(self, strategy: iModel):
        # obrigamos ó uso dunha instancia
        if isinstance(strategy, iModel):
            self.model = strategy
        else:
            raise InheritException(_(f'Must inherit from {iModel.__name__}'))

    def get_conn_db(self) -> Connection:
        return self.model.get_conn_db()

    def get_cur_db(self) -> Cursor:
        return self.model.get_cur_db()

    def connect_db(self) -> tuple([Connection, Cursor]):
        logging.info(_('Connecting to the database'))
        return self.model.connect_db()

    def disconnect_db(self, commit: bool = True) -> None:
        logging.info(_('Disconnecting from the database'))
        return self.model.disconnect_db(commit)

    def save_db(self) -> None:
        logging.info(_('Saving the databse'))
        return self.model.save_db()


    # EXISTS
    def exists(self, obj: Union[MediaGroup, MediaIssue]) -> bool:
        logging.info(_(f'Checking on table "{obj.table_name}" if the information already exists'))
        if isinstance(obj, MediaGroup):
            return self.model.exists_media_group(obj)
        elif isinstance(obj, MediaIssue):
            return self.model.exists_media_issue(obj)


    # GET NUM
    def get_num(self, table_name: str) -> int:
        logging.info(_(f'Counting the number of elements saved on table "{table_name}"'))
        return self.model.get_num(table_name)

    def get_media_group_num_by_media_id(self, media_id: int) -> int:
        logging.info(_(f'Counting the number of elements saved on table "{MediaGroup.table_name}" using the media id "{media_id}"'))
        return self.model.get_media_group_num_by_media_id(media_id)


    # GET
    def get_all(self, table_name: str, limit: int = None, offset: int = 0, alfabetic: bool = False) -> List[Union[MediaType, MediaStatus]]:
        logging.info(_(f'Getting all entries of table "{table_name}" with limit "{limit}", offset "{offset}" and alfabetic order "{alfabetic}"'))
        if table_name == MediaType.table_name:
            return self.model.get_all_media_type(limit, offset, alfabetic)
        elif table_name == MediaStatus.table_name:
            return self.model.get_all_media_status(limit, offset, alfabetic)
        elif table_name == Media.table_name:
            return self.model.get_all_media(limit, offset, alfabetic)


    # GET BY X
    def get_by_id(self, table_name: str, id_: int) -> Union[MediaType, MediaStatus, Media]:
        logging.info(_(f'Searching on "{table_name}" table any entries that match the given id "{id_}"'))
        if table_name == MediaType.table_name:
            return self.model.get_media_type_by_id(id_)
        elif table_name == MediaStatus.table_name:
            return self.model.get_media_status_by_id(id_)
        elif table_name == Media.table_name:
            return self.model.get_media_by_id(id_)

    def get_media_group_by_nk(self, obj: MediaGroup) -> MediaGroup:
        logging.info(_(f'Searching on "{table_name}" table any entries that match its natural key'))
        return self.model.get_media_group_by_nk(obj)

    def get_media_group_by_media_id(self, id_: int, limit: int = None, offset: int = 0, alfabetic: bool = None) -> List[MediaGroup]:
        logging.info(_(f'Searching on "{MediaGroup.table_name}" table any entries that match its media foreign key {id_}'))
        return self.model.get_media_group_by_media_id(id_= id_, limit= limit, offset= offset, alfabetic= alfabetic)

    def get_by_name(self, table_name: str, name: str, limit: int = None, offset: int = 0, alfabetic: bool = False) -> List[Union[MediaType, MediaStatus]]:
        logging.info(_(f'Searching on "{table_name}" table any entries that match the given name "{name}"'))
        if table_name == MediaType.table_name:
            return self.model.get_by_media_type_name(name= name, limit= limit, offset= offset, alfabetic= alfabetic)
        elif table_name == MediaStatus.table_name:
            return self.model.get_by_media_status_name(name= name, limit= limit, offset= offset, alfabetic= alfabetic)


    # INSERT
    def insert(self, obj: Union[MediaStatus, MediaType, Media, MediaGroup, MediaIssue]) -> Union[None, int]:
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
# ------------------------------------------------------------------------------
