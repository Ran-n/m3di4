#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:45:45.121317
#+ Editado:	2023/01/20 18:07:29.752600
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class MediaName:
    table_name: str = field(init=False, default='Media Nomes')
    name: str
    id_media: str = field(default=None)
    id_media_group: str = field(default=None)
    id_media_issue: str = field(default=None)
    id_: int = field(default_factory=create_key)
# ------------------------------------------------------------------------------
