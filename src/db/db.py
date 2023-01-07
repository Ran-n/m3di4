#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/07 14:56:03.852885
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
import src.db.idb as idb

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
class DB:
    def __init__(self, db: idb.DB):
        # obrigamos ó uso dunha instancia
        if isinstance(db, idb.DB):
            self.db = db
        else:
            raise ValueError("Ten que herdar de " + DB.__name__)

    def get_conn(self) -> Connection:
        return self.db.get_conn()

    def get_cur(self) -> Cursor:
        return self.db.get_cur()

    def conectar(self) -> tuple([Connection, Cursor]):
        return self.db.conectar()

    def desconectar(self, commit: bool = True) -> None:
        return self.db.desconectar(commit)

    def select_tipos(self) -> List[MediaTipo]:
        return self.db.select_tipos()

    def select_situacions(self) -> List[MediaSituacion]:
        return self.db.select_situacions()

    def select_almacens(self) -> List[Almacen]:
        return self.db.select_almacens()

    def select_carpetas(self) -> List[NomeCarpeta]:
        return self.db.select_carpetas()

    def select_secuencias(self) -> List[Secuencia]:
        return self.db.select_secuencias()

    def select_lugares(self) -> List[CompartirLugar]:
        return self.db.select_lugares()

    def get_lingua_by_code(self, code: str) -> Lingua:
        return self.db.get_lingua_by_code(code)

    def get_codec_by_name(self, name: str) -> Codec:
        return self.db.get_codec_by_name(name)
# ------------------------------------------------------------------------------
