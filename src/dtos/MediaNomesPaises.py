#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:58:42.990911
#+ Editado:	2023/01/11 23:13:34.373599
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class MediaNomesPaises:
    nome_taboa: str = field(init=False, default='Media Nomes Países')
    id_media_nomes: int = field(default=None)
    id_pais: str = field(default=None)
# ------------------------------------------------------------------------------
