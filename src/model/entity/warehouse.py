#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 00:18:35.149777
#+ Editado:	2023/02/17 17:59:20.439117
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, WarehouseType
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Warehouse(BaseEntity):
    """Entity Object"""
    name: str
    type_: WarehouseType
    desc: Optional[str] = field(default=None)
    size: Optional[int] = field(default=None)
    filled: Optional[int] = field(default=None)
    content: Optional[str] = field(default=None)
    health: Optional[str] = field(default=None)
    desc: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)

    def __post_init__(self):
        self.table_name = Config().get_table_name('Warehouse')
# ------------------------------------------------------------------------------
