#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 21:00:51.700970
#+ Editado:	2023/02/16 23:35:09.863979
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Language, LanguageDescription
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class LanguageDescriptionLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('LanguageDescriptionLanguage'))
    language_desc: LanguageDescription
    language: Language
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
