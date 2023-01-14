#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:36:45.461301
#+ Editado:	2023/01/14 18:22:28.896300
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
import math

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaTipo:
    nome_taboa: str = field(init=False, default='_Media Tipo')
    nome: str
    agrupable: int
    id_: str = field(default_factory=crear_chave)

    def __repr__(self) -> str:
        repetir = 1
        if len(self.nome) < 6:
            repetir = 2
        return f'{self.nome}' + repetir*'\t' + f'[{self.id_}]'
# ------------------------------------------------------------------------------
