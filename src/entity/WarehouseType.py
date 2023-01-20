#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/20 18:16:02.918934
#+ Editado:	2023/01/20 18:17:29.218319
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class WarehouseType:
    table_name: str = field(init=False, default='_Almacén Tipo')
    name: str
    id_: str = field(default_factory=create_key)
# ------------------------------------------------------------------------------
