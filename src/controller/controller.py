#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 18:38:56.570892
#+ Editado:	2023/02/04 13:21:15.592699
# ------------------------------------------------------------------------------
import sys
import logging

from src.model import iModel
from src.view import iView, Terminal

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
                '1': [_('Add Media'), self.add_media],
        }

        try:
            options[self.view.menu(options)][1]()
        except KeyboardInterrupt:
            pass

    def exit(self) -> None:
        logging.info(_('Starting the exit process'))
        self.model.disconnect_db(commit=True)
        self.view.exit()
        logging.info(_('Exiting the program'))
        sys.exit()

    def add_media(self) -> None:
        logging.info(_('Starting the "Add Media" process'))
        self.model.insert(self.view.add_media())
# ------------------------------------------------------------------------------
