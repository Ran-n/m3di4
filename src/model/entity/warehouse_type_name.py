#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 13:44:15.192121
#+ Editado:	2023/02/17 18:22:53.694464
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, WarehouseType
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class WarehouseTypeName(BaseEntity):
    """Entity Object"""
    name: str
    warehouse_type: WarehouseType

    def __post_init__(self):
        self.table_name = Config().get_table_name('WarehouseTypeName')
# ------------------------------------------------------------------------------
