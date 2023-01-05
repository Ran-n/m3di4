#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:06:39.547649
#+ Editado:	2023/01/05 21:10:10.425105
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaWeb:
    nome_taboa: str = field(init=False, default='Media Web')
    id_media: str = field(default=None)
    id_web: str = field(default=None)
    ligazon: str
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
