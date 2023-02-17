#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 13:48:04.701991
#+ Editado:	2023/02/17 18:22:47.433177
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, WarehouseTypeDescription, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class WarehouseTypeDescriptionLanguage(BaseEntity):
    """Entity Object"""
    warehouse_type_desc: WarehouseTypeDescription
    language: Language

    def __post_init__(self):
        self.table_name = Config().get_table_name('WarehouseTypeDescriptionLanguage')
# ------------------------------------------------------------------------------
