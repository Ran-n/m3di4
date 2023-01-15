#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:41:48.278353
#+ Editado:	2023/01/15 23:02:27.813562
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaFasciculo:
    nome_taboa: str = field(init=False, default='Media Fascículo')
    num_total: int
    num_agrupacion: int
    nome: str
    data: str = field(default = None)
    id_media: str = field(default=None)
    id_media_agrupacion: str = field(default=None)
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
