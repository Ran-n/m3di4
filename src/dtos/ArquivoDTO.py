#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:53:33.927294
#+ Editado:	2023/01/05 19:06:21.315117
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class ArquivoDTO:
    nome_taboa: str = field(init=False, default='Arquivo')
    nome: str
    extension: str = '.mkv'
    tamanho: int
    duracion: float
    bit_rate: int
    titulo: str
    data_creacion: str
    mudo: int = 0
    cor: int = 1
    id_almacen: str = None
    id_carpeta: str = None
    id_media: str = None
    id_media_fasciculo: str = None
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
