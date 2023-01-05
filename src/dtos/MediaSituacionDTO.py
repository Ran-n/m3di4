#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:38:25.313276
#+ Editado:	2023/01/05 19:09:32.906422
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaSituacionDTO:
    nome_taboa: str = field(init=False, default='_Media Situación')
    nome: str
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
