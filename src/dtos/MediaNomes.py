#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:45:45.121317
#+ Editado:	2023/01/15 23:02:04.056472
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaNomes:
    nome_taboa: str = field(init=False, default='Media Nomes')
    nome: str
    id_media: str = field(default=None)
    id_media_agrupacion: str = field(default=None)
    id_media_fasciculo: str = field(default=None)
    id_: int = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
