#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:45:45.121317
#+ Editado:	2023/01/11 23:13:19.934690
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class MediaNomes:
    nome_taboa: str = field(init=False, default='Media Nomes')
    nome: str
    id_media: str = None
    id_media_agrupacion: str = field(default=None)
    id_media_fasciculo: str = field(default=None)
# ------------------------------------------------------------------------------
