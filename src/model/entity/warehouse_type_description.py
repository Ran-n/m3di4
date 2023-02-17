#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 13:45:17.157511
#+ Editado:	2023/02/17 18:22:42.366429
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, WarehouseType
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class WarehouseTypeDescription(BaseEntity):
    """Entity Object"""
    desc: str
    warehouse_type: WarehouseType

    def __post_init__(self):
        self.table_name = Config().get_table_name('WarehouseTypeDescription')
# ------------------------------------------------------------------------------
