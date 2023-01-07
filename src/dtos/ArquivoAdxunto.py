#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 19:48:30.957751
#+ Editado:	2023/01/07 14:47:20.678911
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class ArquivoAdxunto:
    nome_taboa: str = field(init=False, default='Arquivo Adxunto')
    nome: str
    tamanho: int
    inicio: float
    duracion: float
    id_arquivo: str = field(default=None)
    id_codec: str = field(default='ttf')
    id_: int = field(init=False, default=None)
# ------------------------------------------------------------------------------
