#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:58:42.990911
#+ Editado:	2023/01/20 17:59:28.978905
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class MediaNameCountry:
    table_name: str = field(init=False, default='Media Nomes Países')
    id_media_name: int = field(default=None)
    id_country: str = field(default=None)
# ------------------------------------------------------------------------------
