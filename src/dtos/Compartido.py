#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/08 00:36:14.914271
#+ Editado:	2023/01/08 00:39:15.860725
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class Compartido:
    nome_taboa: str = field(init=False, default='Compartido')
    ligazon: str
    id_lugar: str = field(default=None)
    id_arquivo: str = field(default=None)
    #id_: int = field(default=None)
# ------------------------------------------------------------------------------
