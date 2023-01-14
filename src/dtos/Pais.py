#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:01:54.400579
#+ Editado:	2023/01/14 16:17:48.202762
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave, strip_accents
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
        return strip_accents(self.nome) > strip_accents(other.nome)

    def __lt__(self, other) -> bool:
        return strip_accents(self.nome) < strip_accents(other.nome)
# ------------------------------------------------------------------------------
