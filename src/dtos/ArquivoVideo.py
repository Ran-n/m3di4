#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:57:18.314541
#+ Editado:	2023/01/07 13:38:14.407277
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
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
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
