#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:01:51.038236
#+ Editado:	2023/02/17 18:02:04.201659
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config, strip_accents
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Language(BaseEntity):
    """Entity Object"""
    name: str
    desc: Optional[str] = field(default=None)

    def __post_init__(self):
        self.table_name = Config().get_table_name('Language')

    def __gt__(self, other) -> bool:
        return strip_accents(self.name) > strip_accents(other.name)

    def __lt__(self, other) -> bool:
        return strip_accents(self.name) < strip_accents(other.name)
# ------------------------------------------------------------------------------
