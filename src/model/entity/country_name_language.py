#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/01 21:21:01.942449
#+ Editado:	2023/02/17 18:03:10.694650
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, CountryName, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CountryNameLanguage(BaseEntity):
    """Entity Object"""
    country_name: CountryName
    language: Language

    def __post_init__(self):
        self.table_name = Config().get_table_name('CountryNameLanguage')
# ------------------------------------------------------------------------------
