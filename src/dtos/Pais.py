#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:01:54.400579
#+ Editado:	2023/01/08 16:48:58.589253
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class Pais:
    nome_taboa: str = field(init=False, default='País')
    nome: str
    reino: int = field(default=None)
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
