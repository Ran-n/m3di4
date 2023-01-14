#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 18:38:56.570892
#+ Editado:	2023/01/14 17:41:52.198100
# ------------------------------------------------------------------------------
from src.model.imodel import iModel
from src.view.iview import iView

from src.controller.sair import sair
from src.controller.insertar import insertar
# ------------------------------------------------------------------------------
class Controller:
    def __init__(self, model: iModel, view: iView):
        self.model = model
        self.view = view

    def sair(self) -> None:
        sair(self.model)

    def insertar(self) -> None:
        insertar(self.model)
# ------------------------------------------------------------------------------
