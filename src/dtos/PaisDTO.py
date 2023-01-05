#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:01:54.400579
#+ Editado:	2023/01/05 19:11:24.123225
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaDTO:
    nome_taboa: str = field(init=False, default='País')
    nome: str
    reino: int = 0
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
