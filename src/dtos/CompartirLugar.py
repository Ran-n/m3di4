#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 14:52:39.247289
#+ Editado:	2023/01/08 00:30:53.997750
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.uteis import crear_chave
# ------------------------------------------------------------------------------
@dataclass
class CompartirLugar:
    nome_taboa: str = field(init=False, default='_Compartir Lugar')
    nome: str
    privado: int
    ligazon: str
    tipo: str
    plataforma: str
    id_: str = field(default_factory=crear_chave)

    def __repr__(self) -> str:
        times = 1
        if len(self.nome) < 15:
            times=2
        return f'{self.nome}'+times*'\t'+f'[{self.id_}]'
# ------------------------------------------------------------------------------
