#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 00:18:35.149777
#+ Editado:	2023/01/20 17:29:44.812318
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class Warehouse:
    table_name: str = field(init=False, default='_Almacén')
    name: str
    capacity: int = field(default=None)
    occupied: int = field(default=None)
    content: str = field(default=None)
    id_type: str = field(default=None)
    health: str = field(default=None)
    desc: str = field(default=None)
    id_: str = field(default_factory=create_key)

    # xFCR
    def __repr__(self) -> str:
        times = 1
        if len(self.name) < 7:
            times=2
        return f'{self.name}'+times*'\t'+f'[{self.id_}]'
# ------------------------------------------------------------------------------
