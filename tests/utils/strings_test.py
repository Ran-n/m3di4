#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:43:24.409946
#+ Editado:	2023/02/03 18:31:50.256910
# ------------------------------------------------------------------------------
import unittest

from src.utils import strip_accents
# ------------------------------------------------------------------------------
class TestStrings(unittest.TestCase):

    def test_strip_accents(self):
        """
        eng: Normal use test
        glg: Proba de uso normal
        """

        tests = zip(
                ['tést', 'í', 'Ü', 'ñ', 'Ñ'],
                ['test', 'i', 'U', 'n', 'N']
        )

        for accent, no_accent in tests:
            self.assertEqual(strip_accents(accent), no_accent)

# ------------------------------------------------------------------------------
