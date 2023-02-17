#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/21 01:24:01.546584
#+ Editado:	2023/02/17 20:40:42.354084
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, Language, LanguageName
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class LanguageNameLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('LanguageNameLanguage'))
    language_name: LanguageName
    language: Language
# ------------------------------------------------------------------------------
