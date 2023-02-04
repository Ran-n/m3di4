#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/02/04 16:56:13.405014
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
    def get_all(self, table_name: str, alfabetic: bool = False) -> List[Union[MediaType, MediaStatus]]:
        pass

    @abstractmethod
    def get_by_name(self, table_name: str, name: str) -> List[Union[MediaType, MediaStatus]]:
        pass

    @abstractmethod
    def insert(self, obj: Union[Media, MediaGroup, MediaIssue]) -> Union[None, int]:
        pass
# ------------------------------------------------------------------------------
