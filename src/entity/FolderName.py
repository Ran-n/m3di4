#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:04:14.716403
#+ Editado:	2023/01/20 18:00:28.889322
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class FolderName:
    table_name: str = field(init=False, default='Nome Carpeta')
    name: str
    id_: int = field(default_factory=create_key)

    # xFCR
    def __repr__(self) -> str:
        return f'{self.name}\t[{self.id_}]'
# ------------------------------------------------------------------------------
