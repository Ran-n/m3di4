#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/16 23:05:21.520132
#+ Editado:	2023/01/16 23:40:10.262970
# ------------------------------------------------------------------------------
from src.view.iview import iView
# ------------------------------------------------------------------------------
import customtkinter

from src.dtos.Media import Media
# ------------------------------------------------------------------------------
class GUI(iView):
    def __init__(self) -> None:
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk()
        self.root.geometry('500x350')
        self.root.mainloop()

    def menu(self, options: dict) -> int:
        pass

    def exit(self) -> None:
        pass

    def get_media(self) -> Media:
        pass
# ------------------------------------------------------------------------------
