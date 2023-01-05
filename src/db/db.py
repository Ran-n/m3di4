#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/05 22:54:24.405392
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
from sqlite3 import Connection
from typing import List

import src.db.idb as idb
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

    def conectar(self) -> Connection:
        return self.db.conectar()

    def desconectar(self, commit: bool = True) -> None:
        return self.db.desconectar(commit)

    def select(self, elemento: object) -> List[object]:
        return self.db.select(elemento)
# ------------------------------------------------------------------------------
