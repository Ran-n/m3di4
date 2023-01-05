#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:36:45.461301
#+ Editado:	2023/01/05 19:10:09.624285
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaTipoDTO:
    nome_taboa: str = field(init=False, default='_Media Tipo')
    nome: str
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
