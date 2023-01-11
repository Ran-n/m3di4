#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 18:38:56.570892
#+ Editado:	2023/01/11 22:17:39.243715
# ------------------------------------------------------------------------------
from src.controller.sair import sair
from src.controller.insertar import insertar

from src.model.model import Model
# ------------------------------------------------------------------------------
class Controller:
    def __init__(self):
        pass

    def sair(self, model: Model) -> None:
        sair(model)

    def insertar(self, model: Model) -> None:
        insertar(model)
# ------------------------------------------------------------------------------
