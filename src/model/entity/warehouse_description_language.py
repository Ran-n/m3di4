#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 13:48:04.701991
#+ Editado:	2023/02/17 18:22:33.275935
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, WarehouseDescription, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class WarehouseDescriptionLanguage(BaseEntity):
    """Entity Object"""
    warehouse_desc: WarehouseDescription
    language: Language

    def __post_init__(self):
        self.table_name = Config().get_table_name('WarehouseDescriptionLanguage')
# ------------------------------------------------------------------------------
