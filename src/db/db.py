#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/07 01:33:18.650809
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

    def select(self, elemento: object) -> List[object]:
        return self.db.select(elemento)
# ------------------------------------------------------------------------------
