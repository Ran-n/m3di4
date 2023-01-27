#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:13:55.315626
#+ Editado:	2023/01/24 18:38:42.367228
# ------------------------------------------------------------------------------
from secrets import token_urlsafe, randbits

from typing import List
# ------------------------------------------------------------------------------
def create_key(length: int = 32) -> str:
    """
    en: Returns a random string of 43(32) characters that will be used as an id.
    gz: Retorna un catex aleatorio de 43(32) caracteres que se usará como id.
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
