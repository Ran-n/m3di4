#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:43:24.409946
#+ Editado:	2023/02/11 00:10:33.619711
# ------------------------------------------------------------------------------
import unittest

from src.utils import strip_accents, center
# ------------------------------------------------------------------------------
class TestStrings(unittest.TestCase):

    def test_strip_accents(self):
        """
        eng: Normal use test.
        glg: Proba de uso normal.
        """

        tests = zip(
                ['tést', 'í', 'Ü', 'ñ', 'Ñ'],
                ['test', 'i', 'U', 'n', 'N']
        )

        for accent, no_accent in tests:
            self.assertEqual(strip_accents(accent), no_accent)

    def test_center(self):
        """
        Normal use test.
        When:
            text    -   odd
            number  -   even
                                One more space on the left side.
            text    -   even
            number  -   odd
                                One more space on the right side.
        """

        tests = zip(
                ['a', 'b', 'c', 'dd', 'ee', 'ff', 'g', 'hh', 'i', 'jj', 'kkk', 'llll', 'mmmmm', 'nnnnnn', 'ññññññññññ', 'oooooo'],
                [ 3,   1,   2,   3,    1,    2,    5,   5,    4,   4,    9,     8,      10,      11,       21,           5],
                [' a ', 'b', 'c ', 'dd ', 'e', 'ff', '  g  ', ' hh  ', ' i  ', ' jj ', '   kkk   ', '  llll  ', '  mmmmm   ', '  nnnnnn   ', '     ññññññññññ      ', 'ooooo']
        )

        for text, length, result in tests:
            self.assertEqual(center(text, length), result)

# ------------------------------------------------------------------------------
