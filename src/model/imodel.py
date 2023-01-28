#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/28 16:15:41.076530
# ------------------------------------------------------------------------------
#* Strategy Interface (Strategy Pattern)
# ------------------------------------------------------------------------------
from abc import ABC, abstractmethod
# ------------------------------------------------------------------------------
from sqlite3 import Connection, Cursor
from typing import List, Tuple, Union

from src.model.entity import Warehouse, WarehouseType
from src.model.entity import Media, MediaGroup, MediaIssue, MediaType, MediaStatus
from src.model.entity import Language, Codec, FolderName
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
    def get_all(self, table_name: str, alfabetic: bool = False) -> List[Union[Warehouse, WarehouseType]]:
        pass

    """
    @abstractmethod
    def get_media_status_by_name(self, name: str) -> MediaStatus:
        pass

    @abstractmethod
    def get_language_by_code(self, code: str) -> Language:
        pass

    @abstractmethod
    def get_codec_by_name(self, name: str) -> Codec:
        pass

    @abstractmethod
    def get_folder_name_by_name(self, name: str) -> FolderName:
        pass
    """

    @abstractmethod
    def get_media_type_groupables(self, id_only: bool = False) -> List[Union[MediaType, str]]:
        pass

    @abstractmethod
    def insert(self, obj: Union[Media, MediaGroup, MediaIssue]) -> Union[None, int]:
        pass
# ------------------------------------------------------------------------------
