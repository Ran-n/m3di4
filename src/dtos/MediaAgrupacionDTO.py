#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:41:42.686442
#+ Editado:	2023/01/04 23:44:32.343774
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaDTO:
    nome: str
    numero: int
    ano_ini: int
    ano_fin: int
    id_media: str
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------

