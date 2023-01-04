#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:41:48.278353
#+ Editado:	2023/01/04 23:44:06.217809
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaFasciculoDTO:
    num_total: int
    num_agrupacion: int
    nome: str
    data: str
    id_media: str
    id_media_agrupacion: str
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
