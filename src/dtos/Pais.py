#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:01:54.400579
#+ Editado:	2023/01/13 23:00:12.073364
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class Pais:
    nome_taboa: str = field(init=False, default='_País')
    nome: str
    reino: int = field(default=None)
    id_: str = field(default_factory=crear_chave)

    def __repr__(self) -> str:
        return f'{self.nome}\t[{self.id_}]'

    def __gt__(self, other) -> bool:
        return self.nome > other.nome

    def __lt__(self, other) -> bool:
        return self.nome < other.nome
# ------------------------------------------------------------------------------
