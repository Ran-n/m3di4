#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 21:00:51.700970
#+ Editado:	2023/02/17 18:20:03.595759
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, Language, LanguageDescription
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class LanguageDescriptionLanguage(BaseEntity):
    """Entity Object"""
    language_desc: LanguageDescription
    language: Language

    def __post_init__(self):
        self.table_name = Config().get_table_name('LanguageDescriptionLanguage')
# ------------------------------------------------------------------------------
