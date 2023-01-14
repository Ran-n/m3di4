#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:43:24.409946
#+ Editado:	2023/01/14 16:29:00.429458
# ------------------------------------------------------------------------------
import unittest

from src.uteis import *
from src.dtos.Secuencia import Secuencia
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

    def test_seqseg(self):
        """
        Proba do funcionamento.
        """
        seqs = [
            Secuencia(nome='a', seq=1),
            Secuencia(nome='b', seq=10),
            Secuencia(nome='c', seq=-1),
            Secuencia(nome='d', seq=-6),
        ]

        self.assertEqual(seqseg('a', seqs), 2)
        self.assertEqual(seqseg('b', seqs), 11)
        self.assertEqual(seqseg('c', seqs), 0)
        self.assertEqual(seqseg('d', seqs), -5)
        self.assertEqual(seqseg('e', seqs), None)

    def test_strip_accents(self):
        """
        Normal use test.
        """

        tests = zip(
                ['tést', 'í', 'Ü', 'ñ', 'Ñ'],
                ['test', 'i', 'U', 'n', 'N']
        )

        for accent, no_accent in tests:
            self.assertEqual(strip_accents(accent), no_accent)

# ------------------------------------------------------------------------------
