#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:13:55.315626
#+ Editado:	2023/01/20 17:27:37.858999
# ------------------------------------------------------------------------------
from secrets import token_urlsafe, randbits
from unicodedata import normalize, category

from typing import List

from src.dtos.Sequence import Sequence
# ------------------------------------------------------------------------------
def create_key(length: int = 24) -> str:
    """
    en: Returns a random string of 32(24) characters that will be used as an id.
    gz: Retorna un catex aleatorio de 32(24) caracteres que se usará como id.
    """
    return token_urlsafe(length)
# ------------------------------------------------------------------------------
def create_key_num(length: int = 32) -> str:
    """
    en: Returns a random number of "length" bits.
    gz: Retorna un número aleatorio de lonxitude bits de forma aleatoria.
    """
    return randbits(length)
# ------------------------------------------------------------------------------
def seqseg(table_name: str, sequences: List[Sequence]) -> [int, None]:
    """
    en: Given a table name returns the next value of the seq.
    gz: Dado un nome de táboa saca o seguinte valor da seq.
    """
    for seq in sequences:
        if seq.nome == table_name:
            seq.seq += 1
            return seq.seq

# ------------------------------------------------------------------------------
def strip_accents(string: str) -> str:
    """
    en: Given a string, returns the same without any accents.
    gz: Dado un catex, retorna o mesmo sen ningún acento.
    """
    return ''.join(ele for ele in normalize('NFD', string) if category(ele) != 'Mn')
# ------------------------------------------------------------------------------
