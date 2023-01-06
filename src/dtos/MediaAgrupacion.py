#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:41:42.686442
#+ Editado:	2023/01/06 17:23:13.900259
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaAgrupacion:
    nome_taboa: str = field(init=False, default='Media Agrupación')
    nome: str
    numero: int
    ano_ini: int
    ano_fin: int
    id_media: str = field(default=None)
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------

