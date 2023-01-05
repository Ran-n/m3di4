#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:58:36.138946
#+ Editado:	2023/01/05 00:00:32.678918
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class MediaNomesLinguasDTO:
    nome_taboa: str = field(init=False, default='Media Nomes Linguas')
    id_media_nomes: int
    id_lingua: str
# ------------------------------------------------------------------------------
