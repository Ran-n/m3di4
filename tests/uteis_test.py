#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:43:24.409946
#+ Editado:	2023/01/05 18:50:30.678404
# ------------------------------------------------------------------------------
import unittest

from src.uteis import *
# ------------------------------------------------------------------------------
class TestUteis(unittest.TestCase):

    def test_crear_chave_tipo(self):
        """
        Proba sobre o tipo creado
        """
        self.assertEqual(type(crear_chave()), str)

    def test_crear_chave_lonxitude(self):
        """
        Proba sobre  a lonxitude da chave creada
        """
        self.assertEqual(len(crear_chave()), 32)
        self.assertNotEqual(len(crear_chave(24)), 24)

    def test_crear_chave_num(self):
        """
        Proba sobre o tipo creado.
        """
        self.assertEqual(type(crear_chave_num()), int)

# ------------------------------------------------------------------------------
