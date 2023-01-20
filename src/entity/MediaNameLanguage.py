#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:58:36.138946
#+ Editado:	2023/01/20 17:55:14.406209
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class MediaNameLanguage:
    table_name: str = field(init=False, default='Media Nomes Linguas')
    id_media_name: int = field(default=None)
    id_language: str = field(default=None)
# ------------------------------------------------------------------------------
