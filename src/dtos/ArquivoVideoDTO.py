#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:57:18.314541
#+ Editado:	2023/01/05 19:06:42.053319
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class ArquivoVideoDTO:
    nome_taboa: str = field(init=False, default='Arquivo Vídeo')
    id_arquivo: str = None
    id_lingua: str = None
    calidade: str
    resolucion: str
    id_codec: str
    aspecto_sample: str
    aspecto_display: str
    formato_pixel: str
    sample_rate: int
    bit_rate: int
    fps: float
    tamanho: int
    inicio: float
    duracion: float
    cor: int = 1
    nome: str
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
