#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/02/04 17:14:16.349883
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.model import iModel
# ------------------------------------------------------------------------------
from sqlite3 import Connection, Cursor
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
        return self.model.connect_db()

    def disconnect_db(self, commit: bool = True) -> None:
        return self.model.disconnect_db(commit)

    def save_db(self) -> None:
        return self.model.save_db()


    # GET
    def get_all(self, table_name: str, alfabetic: bool = False) -> List[Union[MediaType, MediaStatus]]:
        if table_name == MediaType.table_name:
            return self.model.get_all_media_type(alfabetic)
        elif table_name == MediaStatus.table_name:
            return self.model.get_all_media_status(alfabetic)


    # GET BY X
    def get_by_name(self, table_name: str, name: str) -> List[Union[MediaType, MediaStatus]]:
        if table_name == MediaType.table_name:
            return self.model.get_by_media_type_name(name)
        elif table_name == MediaStatus.table_name:
            return self.model.get_by_media_status_name(name)


    # INSERT
    def insert(self, obj: Union[MediaStatus, MediaType, Media, MediaGroup, MediaIssue]) -> Union[None, int]:
        if isinstance(obj, MediaStatus):
            return self.model.insert_media_status(obj)
        elif isinstance(obj, MediaType):
            return self.model.insert_media_type(obj)
        elif isinstance(obj, Media):
            return self.model.insert_media(obj)
        elif isinstance(obj, MediaGroup):
            return self.model.insert_media_group(obj)
# ------------------------------------------------------------------------------
