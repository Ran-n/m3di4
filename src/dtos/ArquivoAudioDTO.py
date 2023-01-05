#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 19:51:12.375406
#+ Editado:	2023/01/05 19:51:12.375406
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class ArquivoAudioDTO:
    id_arquivo: str = field(default=None)
    id_codec: str = field(default='eac3')
    canles: float
    sample_rate: int
    bit_rate: int
    id_lingua: str = field(default=None)
    xdefecto: int = field(default=0)
    forzado: int = field(default=0)
    comentario: int = field(default=0)
    nome: str
    tamanho: int
    inicio: float
    duracion: float
    id_: int = field(default=None)
# ------------------------------------------------------------------------------
