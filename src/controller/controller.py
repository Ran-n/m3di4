#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 18:38:56.570892
#+ Editado:	2023/01/29 17:08:17.158290
# ------------------------------------------------------------------------------
import sys
import logging

from src.model.imodel import iModel
from src.view.iview import iView
from src.view.terminal import Terminal

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
        options = {
                '0': [_('Exit'), self.exit],
                '1': [_('Insert'), self.insert],
        }

        options[self.view.menu(options)][1]()

    def exit(self) -> None:
        logging.info(_('Starting the exit process'))
        self.model.disconnect_db(commit=True)
        self.view.exit()
        logging.info(_('Exiting the program'))
        sys.exit()

    def insert(self) -> None:
        logging.info(_('Starting the insert process'))
        #insertar(self.model)
        print('insert')
# ------------------------------------------------------------------------------
