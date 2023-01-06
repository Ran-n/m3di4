#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:38:25.313276
#+ Editado:	2023/01/06 01:31:50.772605
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class MediaSituacion:
    nome_taboa: str = field(init=False, default='_Media Situación')
    nome: str
    id_: str = field(default_factory=crear_chave)

    def __repr__(self) -> str:
        return f'{self.nome}\t[{self.id_}]'
# ------------------------------------------------------------------------------
