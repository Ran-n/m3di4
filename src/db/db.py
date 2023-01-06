#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/06 16:51:43.833134
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
import src.db.idb as idb

from sqlite3 import Connection, Cursor
from typing import List, Tuple, Union

from src.dtos.MediaTipo import MediaTipo
from src.dtos.MediaSituacion import MediaSituacion
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
        return self.db.select_taboa_id_nome('_Media Tipo')

    def select_situacions(self) -> List[MediaSituacion]:
        return self.db.select_taboa_id_nome('_Media Situación')

    def select(self, elemento: object) -> List[object]:
        return self.db.select(elemento)
# ------------------------------------------------------------------------------
