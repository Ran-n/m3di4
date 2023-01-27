#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 00:18:35.149777
#+ Editado:	2023/01/25 23:03:48.994631
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.entity import WarehouseType
# ------------------------------------------------------------------------------
@dataclass
class Warehouse:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('Warehouse'))
    name: str
    type_: WarehouseType
    size: Optional[int] = field(default=None)
    filled: Optional[int] = field(default=None)
    content: Optional[str] = field(default=None)
    health: Optional[str] = field(default=None)
    desc: Optional[str] = field(default=None)
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)

    """
    # xFCR
    def __repr__(self) -> str:
        times = 1
        if len(self.name) < 7:
            times=2
        return f'{self.name}'+times*'\t'+f'[{self.id_}]'
    """
# ------------------------------------------------------------------------------
