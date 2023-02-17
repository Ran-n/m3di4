#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 13:45:17.157511
#+ Editado:	2023/02/17 18:22:28.233860
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, Warehouse
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class WarehouseDescription(BaseEntity):
    """Entity Object"""
    desc: str
    warehouse: Warehouse

    def __post_init__(self):
        self.table_name = Config().get_table_name('WarehouseDescription')
# ------------------------------------------------------------------------------
