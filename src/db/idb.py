#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/07 14:55:58.788999
# ------------------------------------------------------------------------------
#* Strategy Interface (Strategy Pattern)
# ------------------------------------------------------------------------------
from abc import ABC, abstractmethod

from sqlite3 import Connection, Cursor
from typing import List, Tuple, Union

from src.dtos.MediaTipo import MediaTipo
from src.dtos.MediaSituacion import MediaSituacion
from src.dtos.Almacen import Almacen
from src.dtos.NomeCarpeta import NomeCarpeta
from src.dtos.Secuencia import Secuencia
from src.dtos.Lingua import Lingua
from src.dtos.Codec import Codec
from src.dtos.CompartirLugar import CompartirLugar
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
    def select_almacens(self) -> List[Almacen]:
        pass

    @abstractmethod
    def select_carpetas(self) -> List[NomeCarpeta]:
        pass

    @abstractmethod
    def select_secuencias(self) -> List[Secuencia]:
        pass

    @abstractmethod
    def select_lugares(self) -> List[CompartirLugar]:
        pass

    @abstractmethod
    def get_lingua_by_code(self, code: str) -> Lingua:
        pass

    @abstractmethod
    def get_codec_by_name(self, name: str) -> Codec:
        pass
# ------------------------------------------------------------------------------
