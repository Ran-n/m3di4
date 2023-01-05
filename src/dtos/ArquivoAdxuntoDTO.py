#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 19:48:30.957751
#+ Editado:	2023/01/05 19:50:37.546484
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class ArquivoAdxuntoDTO:
    id_arquivo: str = field(default=None)
    id_codec: str = field(default='ttf')
    nome: str
    inicio: float
    duracion: float
    id_: int = field(default=None)
# ------------------------------------------------------------------------------
