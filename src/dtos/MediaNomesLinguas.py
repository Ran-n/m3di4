#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:58:36.138946
#+ Editado:	2023/01/05 21:08:47.507963
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class MediaNomesLinguas:
    nome_taboa: str = field(init=False, default='Media Nomes Linguas')
    id_media_nomes: int = field(default=None)
    id_lingua: str = field(default=None)
    id_: int = field(init=False, default=None)
# ------------------------------------------------------------------------------
