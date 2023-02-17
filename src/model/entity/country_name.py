#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/01 21:18:34.961211
#+ Editado:	2023/02/17 18:19:15.538454
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import Country
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CountryName(BaseEntity):
    """Entity Object"""
    name: str
    country: Country

    def __post_init__(self):
        self.table_name = Config().get_table_name('CountryName')
# ------------------------------------------------------------------------------
