#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:04:14.716403
#+ Editado:	2023/01/07 01:42:57.183765
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class NomeCarpeta:
    nome_taboa: str = field(init=False, default='Nome Carpeta')
    nome: str
    id_: int = field(default_factory=crear_chave)

    def __repr__(self) -> str:
        return f'{self.nome}\t[{self.id_}]'
# ------------------------------------------------------------------------------
