#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:53:33.927294
#+ Editado:	2023/01/05 20:51:01.879925
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
    mudo: int = field(default=0)
    cor: int = field(default=1)
    id_almacen: str = field(default=None)
    id_carpeta: str = field(default=None)
    id_media: str = field(default=None)
    id_media_fasciculo: str = field(default=None)
    id_: str = field(default_factory=crear_chave)
# ------------------------------------------------------------------------------
