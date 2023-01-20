#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:06:39.547649
#+ Editado:	2023/01/20 18:08:16.052941
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class MediaWeb:
    table_name: str = field(init=False, default='Media Web')
    link: str
    id_media: str = field(default=None)
    id_web: str = field(default=None)
    id_: str = field(default_factory=create_key)
# ------------------------------------------------------------------------------
