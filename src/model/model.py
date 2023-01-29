#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/29 20:58:36.135423
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.model import iModel
# ------------------------------------------------------------------------------
from sqlite3 import Connection, Cursor
from typing import List, Tuple, Union


from src.entity import Warehouse, WarehouseType
from src.entity import Media, MediaGroup, MediaIssue
from src.entity import MediaType, MediaStatus
# ------------------------------------------------------------------------------
class Model:
    def __init__(self, strategy: iModel):
        # obrigamos ó uso dunha instancia
        if isinstance(strategy, iModel):
            self.model = strategy
        else:
            raise ValueError("Ten que herdar de " + iModel.__name__)

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
            return self.model.get_all_media_type(table_name, alfabetic)
        elif table_name == MediaStaus.table_name:
            return self.model.get_all_media_status(table_name, alfabetic)

    """
    def get_media_status_by_name(self, name: str) -> MediaStatus:
        return self.model.get_situacion_by_name(name)

    def get_lingua_by_code(self, code: str) -> Lingua:
        return self.model.get_lingua_by_code(code)

    def get_codec_by_name(self, name: str) -> Codec:
        return self.model.get_codec_by_name(name)

    def get_nomecarpeta_by_name(self, name: str) -> NomeCarpeta:
        return self.model.get_nomecarpeta_by_name(name)
    """

    def get_media_type_groupables(self, id_only: bool = False) -> List[Union[MediaType, str]]:
        return self.model.get_mediatipo_agrupables(id_only)

    # INSERT
    def insert(self, obj: Union[Media, MediaGroup, MediaIssue]) -> Union[None, int]:
        if type(obj) == Media:
            return self.model.insert_media(obj)
        elif type(obj) == MediaGroup:
            return self.model.insert_media_group(obj)
# ------------------------------------------------------------------------------
