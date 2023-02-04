#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:01:54.400579
#+ Editado:	2023/02/04 20:08:15.133191
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config, strip_accents
# ------------------------------------------------------------------------------
@dataclass
class Country:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('Country'))
    name: str
    kingdom: Optional[int] = field(default=None)
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)

    def __gt__(self, other) -> bool:
        return strip_accents(self.name) > strip_accents(other.name)

    def __lt__(self, other) -> bool:
        return strip_accents(self.name) < strip_accents(other.name)
# ------------------------------------------------------------------------------
