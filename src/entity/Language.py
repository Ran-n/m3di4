#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:01:51.038236
#+ Editado:	2023/01/20 18:05:53.500104
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key, strip_accents
# ------------------------------------------------------------------------------
@dataclass
class Lingua:
    table_name: str = field(init=False, default='_Lingua')
    name: str
    desc: str
    id_: str = field(default_factory=create_key)

    # xFCR
    def __repr__(self) -> str:
        return f'{self.name}\t[{self.id_}]'

    def __gt__(self, other) -> bool:
        return strip_accents(self.nome) > strip_accents(other.nome)

    def __lt__(self, other) -> bool:
        return strip_accents(self.nome) < strip_accents(other.nome)
# ------------------------------------------------------------------------------
