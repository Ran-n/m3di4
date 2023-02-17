#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 20:59:37.407686
#+ Editado:	2023/02/17 18:19:55.468712
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class LanguageDescription(BaseEntity):
    """Entity Object"""
    desc: str
    language: Language

    def __post_init__(self):
        self.table_name = Config().get_table_name('LanguageDescription')
# ------------------------------------------------------------------------------
