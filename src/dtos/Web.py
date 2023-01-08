#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:08:25.622146
#+ Editado:	2023/01/08 15:43:22.483682
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class Web:
    nome_taboa: str = field(init=False, default='_Web')
    nome: str
    siglas: str
    ligazon: str
    id_: str = field(default_factory=crear_chave)

    def __repr__(self) -> str:
        repetir = 1
        if len(self.nome) < 22:
            repetir = 2
        return f'{self.nome}' + repetir*'\t' + f'[{self.id_}]'
# ------------------------------------------------------------------------------
