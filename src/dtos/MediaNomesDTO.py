#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:45:45.121317
#+ Editado:	2023/01/04 23:50:44.755906
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class MediaNomesDTO:
    nome: str
    id_media: str = field(default=None)
    id_media_agrupacion: str = field(default=None)
    id_media_fasciculo: str = field(default=None)
    id_: int = field(init=False, default=None)
# ------------------------------------------------------------------------------
