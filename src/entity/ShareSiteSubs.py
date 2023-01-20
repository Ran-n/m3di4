#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/20 18:18:03.195457
#+ Editado:	2023/01/20 18:19:02.816946
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class ShareSiteSubs:
    table_name: str = field(init=False, default='_Compartir Lugar Subs')
    subs: int
    id_site: str = field(default=None)
    id_: str = field(default_factory=create_key)
# ------------------------------------------------------------------------------
