#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/21 01:24:01.546584
#+ Editado:	2023/02/24 21:14:36.001503
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optinal

from src.utils import Config
from src.model.entity import BaseEntity, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class LanguageName(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('LanguageName'))
    name: str
    language: Language
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
