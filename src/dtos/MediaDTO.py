#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:09:59.330936
#+ Editado:	2023/01/04 23:17:07.739163
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaDTO:
    nome: str
    ano_ini: int
    ano_fin: int
    id_tipo: str
    id_situacion: str
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
