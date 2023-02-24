#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 20:59:37.407686
#+ Editado:	2023/02/24 21:19:32.942681
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class LanguageDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('LanguageDescription'))
    desc: str
    language: Language
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
