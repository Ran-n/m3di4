#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/06 01:36:37.818333
# ------------------------------------------------------------------------------
#* Strategy Interface (Strategy Pattern)
# ------------------------------------------------------------------------------
from abc import ABC, abstractmethod

from sqlite3 import Connection, Cursor
from typing import List, Tuple, Union

from src.dtos.MediaTipo import MediaTipo
from src.dtos.MediaSituacion import MediaSituacion
# ------------------------------------------------------------------------------
class DB(ABC):
    @abstractmethod
    def get_conn(self) -> Connection:
        pass

    @abstractmethod
    def get_cur(self) -> Cursor:
        pass

    @abstractmethod
    def conectar(self) -> tuple([Connection, Cursor]):
        pass

    @abstractmethod
    def desconectar(self, commit: bool = True) -> None:
        pass

    @abstractmethod
    def select_tipos(self) -> List[MediaTipo]:
        pass

    @abstractmethod
    def select_situacions(self) -> List[MediaSituacion]:
        pass

    @abstractmethod
    def select(elemento: object) -> List[object]:
        pass
# ------------------------------------------------------------------------------
