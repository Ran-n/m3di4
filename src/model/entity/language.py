#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:01:51.038236
#+ Editado:	2023/02/16 23:23:55.466024
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

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
    desc: Optional[str] = field(default=None)
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)

    def __gt__(self, other) -> bool:
        return strip_accents(self.name) > strip_accents(other.name)

    def __lt__(self, other) -> bool:
        return strip_accents(self.name) < strip_accents(other.name)
# ------------------------------------------------------------------------------
