#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 18:38:56.570892
#+ Editado:	2023/01/16 22:34:24.161828
# ------------------------------------------------------------------------------
import sys

from src.model.imodel import iModel
from src.view.iview import iView
from src.view.terminal import Terminal

#from src.controller.sair import sair
#from src.controller.insertar import insertar
# ------------------------------------------------------------------------------
class Controller:
    def __init__(self, model: iModel, view: iView):
        self.model = model
        self.view = view

        if isinstance(self.view.strategy, Terminal):
            while True:
                self.__terminal_menu()


    def __terminal_menu(self) -> None:
        opcions = {
                '0': ['Sair', self.sair],
                '1': ['Insertar', self.insertar],
        }

        opcions[self.view.menu(opcions)][1]()

    def sair(self) -> None:
        #sair(model=self.model, view=self.view)
        self.model.disconnect_db(commit=True)
        self.view.exit()
        sys.exit()

    def insertar(self) -> None:
        #insertar(self.model)
        print('insertar')
# ------------------------------------------------------------------------------
