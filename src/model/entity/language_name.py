#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/21 01:24:01.546584
#+ Editado:	2023/02/17 18:20:08.893548
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class LanguageName(BaseEntity):
    """Entity Object"""
    name: str
    language: Language

    def __post_init__(self):
        self.table_name = Config().get_table_name('LanguageName')
# ------------------------------------------------------------------------------
