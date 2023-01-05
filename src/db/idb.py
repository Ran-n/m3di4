#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/05 22:50:26.743195
# ------------------------------------------------------------------------------
#* Strategy Interface (Strategy Pattern)
# ------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from typing import List
from sqlite3 import Connection
# ------------------------------------------------------------------------------
class DB(ABC):
    @abstractmethod
    def get_conn(self) -> Connection:
        pass

    @abstractmethod
    def conectar(self) -> Connection:
        pass

    @abstractmethod
    def desconectar(self, commit: bool = True) -> None:
        pass

    @abstractmethod
    def select(elemento: object) -> List[object]:
        pass
# ------------------------------------------------------------------------------
