#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:13:55.315626
#+ Editado:	2023/02/10 23:21:31.527955
# ------------------------------------------------------------------------------
from unicodedata import normalize, category

#from src.entity import Sequence
# ------------------------------------------------------------------------------
#def seqseg(table_name: str, sequences: List[Sequence]) -> [int, None]:
    #"""
    #en: Given a table name returns the next value of the seq.
    #gz: Dado un nome de táboa saca o seguinte valor da seq.
    #"""
#    for seq in sequences:
#        if seq.nome == table_name:
#            seq.seq += 1
#            return seq.seq
# ------------------------------------------------------------------------------
def strip_accents(string: str) -> str:
    """
    eng: Given a string, returns the same without any accents.
    glg: Dado un catex, retorna o mesmo sen ningún acento.

    @ Input:
    ╚═  * string    -   str
        └ The text that will be stripped of accents.

    @ Output:
    ╚═  str -   The un accentuated string.
    """

    return ''.join(ele for ele in normalize('NFD', string) if category(ele) != 'Mn')
# ------------------------------------------------------------------------------
def center(string: str, length: int, padder: str = ' ') -> str:
    """
    Given a string and a length return a string said string centered and padded.

    @ Input:
    ╠═  * string    -   str
    ║   └ The text that will be centered.
    ║
    ╠═  * length    -   int
    ║   └ The final text length.
    ║
    ╚═  · padder    -   str -   ' '
        └ Character that the padding will be filled with.

    @ Output:
    ╚═  str -   The centered string.
    """

    l_padding = (length - len(string)) // 2
    r_padding = length - len(string) - l_padding

    return (padder * (l_padding-1)) + ' ' + string + ' ' + (padder * (r_padding-1))
# ------------------------------------------------------------------------------
