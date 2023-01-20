#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/08 00:36:14.914271
#+ Editado:	2023/01/20 17:50:18.942967
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class Shared:
    table_name: str = field(init=False, default='Compartido')
    link: str
    id_site: str = field(default=None)
    id_file: str = field(default=None)
    #id_: int = field(default=None)
# ------------------------------------------------------------------------------
