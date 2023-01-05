#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:45:45.121317
#+ Editado:	2023/01/05 00:05:39.061676
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class MediaNomesDTO:
    nome_taboa: str = field(init=False, default='Media Nomes')
    nome: str
    id_media: str = None
    id_media_agrupacion: str = None
    id_media_fasciculo: str = None
    id_: int = None
# ------------------------------------------------------------------------------
