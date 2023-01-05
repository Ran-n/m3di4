#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:06:39.547649
#+ Editado:	2023/01/05 00:07:32.599309
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaWebDTO:
    nome_taboa: str = field(init=False, default='Media Web')
    id_media: str
    id_web: str
    ligazon: str
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
