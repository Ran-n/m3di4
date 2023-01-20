#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:01:54.400579
#+ Editado:	2023/01/20 18:01:35.500012
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key, strip_accents
# ------------------------------------------------------------------------------
@dataclass
class Country:
    table_name: str = field(init=False, default='_País')
    name: str
    kingdom: int = field(default=None)
    id_: str = field(default_factory=create_key)

    # xFCR
    def __repr__(self) -> str:
        return f'{self.name}\t[{self.id_}]'

    def __gt__(self, other: Country) -> bool:
        return strip_accents(self.name) > strip_accents(other.name)

    def __lt__(self, other: Country) -> bool:
        return strip_accents(self.name) < strip_accents(other.name)
# ------------------------------------------------------------------------------
