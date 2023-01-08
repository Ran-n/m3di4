#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/08 01:37:49.185205
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
from src.dtos.Web import Web
from src.dtos.Media import Media
from src.dtos.MediaWeb import MediaWeb
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
    def select(self, nome_taboa: str) -> List[Union[MediaTipo, MediaSituacion, Almacen, NomeCarpeta, Secuencia, CompartirLugar, Web]]:
        pass

    @abstractmethod
    def get_lingua_by_code(self, code: str) -> Lingua:
        pass

    @abstractmethod
    def get_codec_by_name(self, name: str) -> Codec:
        pass

    @abstractmethod
    def insert(self, obj: Union[Media, MediaWeb]) -> None:
        pass
# ------------------------------------------------------------------------------
