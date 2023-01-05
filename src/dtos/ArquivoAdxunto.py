#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 19:48:30.957751
#+ Editado:	2023/01/05 20:49:22.032491
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class ArquivoAdxunto:
    nome_taboa: str = field(init=False, default='Arquivo Adxunto')
    id_arquivo: str = field(default=None)
    id_codec: str = field(default='ttf')
    nome: str
    inicio: float
    duracion: float
    id_: int = field(init=False, default=None)
# ------------------------------------------------------------------------------
