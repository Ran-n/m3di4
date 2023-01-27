#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:13:55.315626
#+ Editado:	2023/01/23 23:19:39.153586
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
    en: Given a string, returns the same without any accents.
    gz: Dado un catex, retorna o mesmo sen ningún acento.
    """
    return ''.join(ele for ele in normalize('NFD', string) if category(ele) != 'Mn')
# ------------------------------------------------------------------------------
