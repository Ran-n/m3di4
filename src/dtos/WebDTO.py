#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:08:25.622146
#+ Editado:	2023/01/05 19:12:03.207952
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaDTO:
    nome_taboa: str = field(init=False, default='_Web')
    nome: str
    siglas: str
    ligazon: str
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
