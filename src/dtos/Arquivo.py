#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:53:33.927294
#+ Editado:	2023/01/07 13:11:42.701763
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class Arquivo:
    nome_taboa: str = field(init=False, default='Arquivo')
    nome: str
    extension: str
    tamanho: int
    duracion: float
    bit_rate: int
    titulo: str
    data_creacion: str
    id_almacen: str = field(default=None)
    id_carpeta: str = field(default=None)
    id_media: str = field(default=None)
    id_media_fasciculo: str = field(default=None)
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
