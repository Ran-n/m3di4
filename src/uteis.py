#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:13:55.315626
#+ Editado:	2023/01/05 20:33:55.626932
# ------------------------------------------------------------------------------
from secrets import token_urlsafe, randbits

from typing import List

from src.dtos.Secuencia import Secuencia
# ------------------------------------------------------------------------------
def crear_chave(lonxitude: int = 24) -> str:
    """
    Retorna un catex aleatorio de 32(24) caracteres que se usará como id.
    """
    return token_urlsafe(lonxitude)
# ------------------------------------------------------------------------------
def crear_chave_num(lonxitude: int = 32) -> str:
    """
    Retorna un número aleatorio de lonxitude bits de forma aleatoria.
    """
    return randbits(lonxitude)
# ------------------------------------------------------------------------------
def seqseg(nome_taboa: str, secuencias: List[Secuencia]) -> [int, None]:
    """
    Dado un nome de táboa saca o seguinte valor da seq.
    """
    for seq in secuencias:
        if seq.nome == nome_taboa:
            seq.seq += 1
            return seq.seq

# ------------------------------------------------------------------------------
