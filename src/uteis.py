#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:13:55.315626
#+ Editado:	2023/01/05 00:14:15.948485
# ------------------------------------------------------------------------------
from secrets import token_urlsafe, randbits
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
