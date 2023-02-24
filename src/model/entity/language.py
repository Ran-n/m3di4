#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:01:51.038236
#+ Editado:	2023/02/24 20:14:12.453858
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config, strip_accents
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Language(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Language'))
    name: str

    def __gt__(self, other) -> bool:
        return strip_accents(self.name) > strip_accents(other.name)

    def __lt__(self, other) -> bool:
        return strip_accents(self.name) < strip_accents(other.name)
# ------------------------------------------------------------------------------
