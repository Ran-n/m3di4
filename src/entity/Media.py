#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:09:59.330936
#+ Editado:	2023/01/20 18:06:35.426173
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class Media:
    table_name: str = field(init=False, default='Media')
    name: str
    year_start: int
    year_end: int
    id_type: str = field(default=None)
    id_estatus: str = field(default=None)
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
