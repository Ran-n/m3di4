#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 18:38:56.570892
#+ Editado:	2023/02/12 15:24:39.096755
# ------------------------------------------------------------------------------
import sys
import logging

from src.model import iModel
from src.view import iView

#from src.controller.insertar import insertar
# ------------------------------------------------------------------------------
class Controller:
    def __init__(self, model: iModel, view: iView):
        self.model = model
        self.view = view
        self.view.controller = self
        self.view.strategy.controller = self

        self.view.start()


    def save(self) -> None:
        logging.info(_('Starting the saving process'))
        self.view.save()
        self.model.save_db()
        logging.info(_('The saving process was finished'))

    def exit_no_save(self) -> None:
        self.__exit(False)

    def exit_save(self) -> None:
        self.__exit(True)

    def __exit(self, commit: bool) -> None:
        logging.info(_('Starting the exit process'))
        self.model.disconnect_db(commit= commit)
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

    def add_media_group(self, id_media: int = None) -> None:
        logging.info(_('Starting the "Add Media Group" process'))
        self.model.insert(self.view.add_media_group(id_media))
        logging.info(_('The "Add Media Group" process was finished'))

    def add_media_issue(self) -> None:
        logging.info(_('Starting the "Add Media Issue" process'))
        self.model.insert(self.view.add_media_issue())
        logging.info(_('The "Add Media Issue" process was finished'))

    def add_platform(self) -> None:
        logging.info(_('Starting the "Add Platform" process'))
        self.model.insert(self.view.add_platform())
        logging.info(_('The "Add Platform" process was finished'))

# ------------------------------------------------------------------------------
