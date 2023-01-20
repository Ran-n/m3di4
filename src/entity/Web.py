#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:08:25.622146
#+ Editado:	2023/01/20 18:09:08.831365
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class Web:
    table_name: str = field(init=False, default='_Web')
    name: str
    acronym: str
    link: str
    id_: str = field(default_factory=create_key)

    # xFCR
    def __repr__(self) -> str:
        repeat = 1
        if len(self.name) < 22:
            repeat = 2
        return f'{self.name}' + repeat*'\t' + f'[{self.id_}]'
# ------------------------------------------------------------------------------
