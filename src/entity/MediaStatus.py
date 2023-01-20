#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:38:25.313276
#+ Editado:	2023/01/20 18:04:32.299792
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class MediaStatus:
    table_name: str = field(init=False, default='_Media Situación')
    name: str
    id_: str = field(default_factory=create_key)

    def __repr__(self) -> str:
        return f'{self.name}\t[{self.id_}]'
# ------------------------------------------------------------------------------
