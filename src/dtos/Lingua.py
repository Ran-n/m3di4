#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:01:51.038236
#+ Editado:	2023/01/07 13:37:34.337609
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class Lingua:
    nome_taboa: str = field(init=False, default='Lingua')
    nome: str
    desc: str
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
