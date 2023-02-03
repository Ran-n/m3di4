#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:43:24.409946
#+ Editado:	2023/02/03 18:31:50.256910
# ------------------------------------------------------------------------------
import unittest

from src.utils import Config
# ------------------------------------------------------------------------------
class TestConfig(unittest.TestCase):
    def test_creation(self):
        """
        Config is a singleton so it should only be created once
        """

        self.assertEqual(Config(), Config())
        
# ------------------------------------------------------------------------------
