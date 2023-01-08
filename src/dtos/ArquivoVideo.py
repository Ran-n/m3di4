#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:57:18.314541
#+ Editado:	2023/01/08 15:30:53.297033
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class ArquivoVideo:
    nome_taboa: str = field(init=False, default='Arquivo Vídeo')
    calidade: str
    resolucion: str
    aspecto_sample: str
    aspecto_display: str
    formato_pixel: str
    sample_rate: int
    bit_rate: int
    fps: float
    tamanho: int
    inicio: float
    duracion: float
    nome: str
    cor: int = field(default=1)
    id_codec: str = field(default=None)
    id_arquivo: str = field(default=None)
    id_lingua: str = field(default=None)
    #id_: str = field(default=None)
# ------------------------------------------------------------------------------
