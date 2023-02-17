#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 13:46:42.274532
#+ Editado:	2023/02/17 18:22:58.897720
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, WarehouseTypeName, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class WarehouseTypeNameLanguage(BaseEntity):
    """Entity Object"""
    warehouse_type_name: WarehouseTypeName
    language: Language

    def __post_init__(self):
        self.table_name = Config().get_table_name('WarehouseTypeNameLanguage')
# ------------------------------------------------------------------------------
