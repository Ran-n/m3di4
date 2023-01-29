#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/16 23:05:21.520132
#+ Editado:	2023/01/29 23:10:52.923823
# ------------------------------------------------------------------------------
from src.view import iView
# ------------------------------------------------------------------------------
import logging
import customtkinter

from src.model.entity import Media
# ------------------------------------------------------------------------------
class GUI(iView):
    def __init__(self) -> None:
        logging.info(_('Starting GUI view'))
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk()
        self.root.geometry('800x500')
        self.root.mainloop()

    def menu(self, options: dict) -> int:
        pass

    def exit(self) -> None:
        # nothing need to be done here
        pass

    def add_media(self) -> Media:
        pass
# ------------------------------------------------------------------------------
