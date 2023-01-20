#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:53:33.927294
#+ Editado:	2023/01/20 17:58:04.497161
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class File:
    table_name: str = field(init=False, default='Arquivo')
    name: str
    extension: str
    size: int
    duration: float
    bit_rate: int
    title: str
    creation_ts: str
    id_warehouse: str = field(default=None)
    id_folder: str = field(default=None)
    id_media: str = field(default=None)
    id_media_issue: str = field(default=None)
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
