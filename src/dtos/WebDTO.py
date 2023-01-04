#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:08:25.622146
#+ Editado:	2023/01/05 00:08:49.934530
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaDTO:
    nome: str
    siglas: str
    ligazon: str
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
