#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/02/09 22:36:33.665976
# ------------------------------------------------------------------------------
#* Strategy Interface (Strategy Pattern)
# ------------------------------------------------------------------------------
from abc import ABC, abstractmethod
# ------------------------------------------------------------------------------
from sqlite3 import Connection, Cursor
from typing import List, Union

from src.model.entity import Warehouse, WarehouseType
from src.model.entity import Media, MediaGroup, MediaIssue
from src.model.entity import MediaType, MediaStatus
# ------------------------------------------------------------------------------
class iModel(ABC):
    @abstractmethod
    def get_conn_db(self) -> Connection:
        pass

    @abstractmethod
    def get_cur_db(self) -> Cursor:
        pass

    @abstractmethod
    def connect_db(self) -> tuple([Connection, Cursor]):
        pass

    @abstractmethod
    def disconnect_db(self, commit: bool = True) -> None:
        pass

    @abstractmethod
    def save_db(self) -> None:
        pass

    @abstractmethod
    def exists(self, obj: Union[MediaGroup, MediaIssue]) -> bool:
        pass

    @abstractmethod
    def get_num(self, table_name: str) -> int:
        pass

    @abstractmethod
    def get_media_group_num_by_media_id(self, media_id: int) -> int:
        pass

    @abstractmethod
    def get_all(self, table_name: str, limit: int = None, offset: int = 0, alfabetic: bool = False) -> List[Union[MediaType, MediaStatus]]:
        pass


    @abstractmethod
    def get_by_id(self, table_name: str, id_: int) -> Union[MediaType, MediaStatus, Media]:
        pass

    @abstractmethod
    def get_media_group_by_nk(self, obj: MediaGroup) -> MediaGroup:
        pass

    @abstractmethod
    def get_media_group_by_media_id(self, id_: int, limit: int = None, offset: int = 0, alfabetic: bool = None) -> List[MediaGroup]:
        pass

    @abstractmethod
    def get_by_name(self, table_name: str, name: str, limit: int = None, offset: int = 0, alfabetic: bool = False) -> List[Union[MediaType, MediaStatus]]:
        pass


    @abstractmethod
    def insert(self, obj: Union[MediaStatus, MediaType, Media, MediaGroup, MediaIssue]) -> Union[None, int]:
        pass
# ------------------------------------------------------------------------------
