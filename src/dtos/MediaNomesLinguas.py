#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:58:36.138946
#+ Editado:	2023/01/11 23:13:24.778332
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class MediaNomesLinguas:
    nome_taboa: str = field(init=False, default='Media Nomes Linguas')
    id_media_nomes: int = field(default=None)
    id_lingua: str = field(default=None)
# ------------------------------------------------------------------------------
