#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:36:45.461301
#+ Editado:	2023/01/20 18:05:34.866813
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
import math

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class MediaType:
    table_name: str = field(init=False, default='_Media Tipo')
    name: str
    groupable: int
    id_: str = field(default_factory=create_key)

    def __repr__(self) -> str:
        repeat = 1
        if len(self.name) < 6:
            repeat = 2
        return f'{self.name}' + repeat*'\t' + f'[{self.id_}]'
# ------------------------------------------------------------------------------
