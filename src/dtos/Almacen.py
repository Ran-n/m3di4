#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 00:18:35.149777
#+ Editado:	2023/01/07 00:45:02.310093
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class Almacen:
    nome_taboa: str = field(init=False, default='_Almacén')
    nome: str
    capacidade: int = field(default=None)
    ocupado: int = field(default=None)
    contido: str = field(default=None)
    id_tipo: str = field(default=None)
    saude: str = field(default=None)
    desc: str = field(default=None)
    id_: str = field(default_factory=crear_chave)

    def __repr__(self) -> str:
        times = 1
        if len(self.nome) < 7:
            times=2
        return f'{self.nome}'+times*'\t'+f'[{self.id_}]'
# ------------------------------------------------------------------------------
