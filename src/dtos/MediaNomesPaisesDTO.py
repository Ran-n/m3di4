#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:58:42.990911
#+ Editado:	2023/01/05 00:01:25.346608
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class MediaNomesPaisesDTO:
    nome_taboa: str = field(init=False, default='Media Nomes Países')
    id_media_nomes: int
    id_pais: str
# ------------------------------------------------------------------------------
