#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 13:31:54.424384
#+ Editado:	2023/01/07 13:32:56.928382
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class Codec:
    nome_taboa: str = field(init=False, default='_Codec')
    nome: str
    nome_longo: str = field(default=None)
    desc: str = field(default=None)
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
