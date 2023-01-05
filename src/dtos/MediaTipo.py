#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:36:45.461301
#+ Editado:	2023/01/05 21:09:46.480260
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaTipo:
    nome_taboa: str = field(init=False, default='_Media Tipo')
    nome: str
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
