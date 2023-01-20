#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:41:42.686442
#+ Editado:	2023/01/20 18:07:14.133441
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class MediaGroup:
    table_name: str = field(init=False, default='Media Agrupación')
    name: str
    number: int
    year_start: int
    year_end: int
    id_media: str = field(default=None)
    id_: str = field(default_factory=create_key)
# ------------------------------------------------------------------------------

