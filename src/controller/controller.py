#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 18:38:56.570892
#+ Editado:	2023/02/05 15:02:27.956879
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
        self.view.controller = self
        self.view.strategy.controller = self

        if isinstance(self.view.strategy, Terminal):
            while True:
                self.__terminal_menu()


    def __terminal_menu(self) -> None:
        options = {
                '+': [_('Save'), self.save],
                '0': [_('Exit'), self.exit],
                '1': [_('Add Media Type'), self.add_media_type],
                '2': [_('Add Media Status'), self.add_media_status],
                '3': [_('Add Media'), self.add_media],
                '4': [_('Add Media Group'), self.add_media_group],
        }

        try:
            options[self.view.menu(options)][1]()
        except KeyboardInterrupt:
            pass

    def save(self) -> None:
        logging.info(_('Starting the saving process'))
        self.view.save()
        self.model.save_db()
        logging.info(_('The saving process was finished'))

    def exit(self) -> None:
        logging.info(_('Starting the exit process'))
        self.model.disconnect_db(commit=True)
        self.view.exit()
        logging.info(_('Exiting the program'))
        sys.exit()

    def add_media_type(self) -> None:
        logging.info(_('Starting the "Add Media Type" process'))
        self.model.insert(self.view.add_media_type())
        logging.info(_('The "Add Media Type" process was finished'))

    def add_media_status(self) -> None:
        logging.info(_('Starting the "Add Media Status" process'))
        self.model.insert(self.view.add_media_status())
        logging.info(_('The "Add Media Status" process was finished'))

    def add_media(self) -> None:
        logging.info(_('Starting the "Add Media" process'))
        self.model.insert(self.view.add_media())
        logging.info(_('The "Add Media" process was finished'))

    def add_media_group(self) -> None:
        logging.info(_('Starting the "Add Media Group" process'))
        self.model.insert(self.view.add_media_group())
        logging.info(_('The "Add Media Group" process was finished'))
# ------------------------------------------------------------------------------
