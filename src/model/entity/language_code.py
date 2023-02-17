#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/21 01:23:38.362620
#+ Editado:	2023/02/17 18:19:48.755235
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, Language, Code
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class LanguageCode(BaseEntity):
    """Entity Object"""
    language: Language
    code: Code
    codename: str

    def __post_init__(self):
        self.table_name = Config().get_table_name('LanguageCode')
# ------------------------------------------------------------------------------
