#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:43:24.409946
#+ Editado:	2023/02/03 18:31:50.256910
# ------------------------------------------------------------------------------
import unittest

from src.utils import create_key, create_key_num
# ------------------------------------------------------------------------------
class TestKeys(unittest.TestCase):

    def test_create_key_type(self):
        """
        eng: Test of the created type
        glg: Proba sobre o tipo creado
        """
        self.assertEqual(type(create_key()), str)

    def test_create_key_length(self):
        """
        eng: Test of the length of the created key
        glg: Proba sobre a lonxitude da chave creada
        """
        self.assertEqual(len(create_key()), 43)
        #self.assertNotEqual(len(create_key(24)), 24)

    def test_create_key_num(self):
        """
        eng: Test of the created type
        glg: Proba sobre o tipo creado
        """
        self.assertEqual(type(create_key_num()), int)

# ------------------------------------------------------------------------------
