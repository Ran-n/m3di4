#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/06 01:38:53.668080
# ------------------------------------------------------------------------------
#* Concrete Strategy (Strategy Pattern)
# ------------------------------------------------------------------------------
import src.db.idb as idb

import sqlite3
from sqlite3 import Connection, Cursor

from typing import List, Tuple, Union

from src.dtos.MediaTipo import MediaTipo
from src.dtos.MediaSituacion import MediaSituacion
# ------------------------------------------------------------------------------
class Sqlite(idb.DB):
    def __init__(self, ficheiro: str) -> None:
        self.ficheiro = ficheiro
        self.conn = None
        self.cur = None

    def get_conn(self) -> Connection:
        if self.conn == None:
            return self.conectar()[0]
        return self.con

    def get_cur(self) -> Cursor:
        if self.cur == None:
            return self.conectar()[1]
        return self.cur

    def conectar(self) -> tuple([Connection, Cursor]):
        self.conn = sqlite3.connect(self.ficheiro)
        self.cur = self.conn.cursor()
        return (self.conn, self.cur)

    def desconectar(self, commit: bool = True) -> None:
        if commit:
            self.conn.commit()
        self.conn.close()
        self.conn = None
        self.cur = None

    def select_taboa(self, taboa: str) -> List[Union[MediaTipo, MediaSituacion]]:
        results = self.get_cur().execute(f'select ID, Nome from "{taboa}"').fetchall()
        valores = []
        for result in results:
            valores.append(MediaTipo(id_=result[0], nome=result[1]))
        return valores

    def select_tipos(self) -> List[MediaTipo]:
        results = self.get_cur().execute('select ID, Nome from "_Media Tipo"').fetchall()
        valores = []
        for result in results:
            valores.append(MediaTipo(id_=result[0], nome=result[1]))
        return valores

    def select_situacions(self) -> List[MediaSituacion]:
        results = self.get_cur().execute('select ID, Nome from "_Media Situación"').fetchall()
        valores = []
        for result in results:
            valores.append(MediaSituacion(id_=result[0], nome=result[1]))
        return valores

    def select(self, elemento: object) -> List[object]:
        return ['a', 'b']
# ------------------------------------------------------------------------------
