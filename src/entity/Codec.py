#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 13:31:54.424384
#+ Editado:	2023/01/20 17:40:11.298499
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class Codec:
    table_name: str = field(init=False, default='_Codec')
    name: str
    name_long: str = field(default=None)
    desc: str = field(default=None)
    id_: str = field(default_factory=create_key)
# ------------------------------------------------------------------------------
