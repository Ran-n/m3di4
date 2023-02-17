#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/21 01:24:01.546584
#+ Editado:	2023/02/17 18:20:15.131758
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, Language, LanguageName
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class LanguageNameLanguage(BaseEntity):
    """Entity Object"""
    language_name: LanguageName
    language: Language

    def __post_init__(self):
        self.table_name = Config().get_table_name('LanguageNameLanguage')
# ------------------------------------------------------------------------------
