#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:41:48.278353
#+ Editado:	2023/01/20 17:57:39.108749
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class MediaIssue:
    table_name: str = field(init=False, default='Media Fascículo')
    media_number: int
    group_number: int
    name: str
    date: str = field(default = None)
    id_media: str = field(default=None)
    id_media_group: str = field(default=None)
    id_: str = field(default_factory=create_key)
# ------------------------------------------------------------------------------
