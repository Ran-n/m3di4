#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/05 22:53:43.906003
# ------------------------------------------------------------------------------
#* Concrete Strategy (Strategy Pattern)
# ------------------------------------------------------------------------------
import sqlite3
from sqlite3 import Connection, Cursor

from typing import List

import src.db.idb as idb
# ------------------------------------------------------------------------------
class Sqlite(idb.DB):
    def __init__(self, ficheiro: str) -> None:
        self.ficheiro = ficheiro
        self.conn = None

    def get_conn(self) -> Connection:
        return self.conn

    def conectar(self) -> Connection:
        self.conn = sqlite3.connect(self.ficheiro)
        return self.conn

    def desconectar(self, commit: bool = True) -> None:
        if commit:
            self.conn.commit()
        self.conn.close()
        self.conn = None

    def select(self, elemento: object) -> List[object]:
        return ['a', 'b']
# ------------------------------------------------------------------------------
