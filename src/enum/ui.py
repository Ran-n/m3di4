#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/03 16:41:07.729202
#+ Editado:	2023/02/05 22:48:56.602214
# ------------------------------------------------------------------------------
from enum import Enum

#from src.view import Terminal, CustomTKinter
# ------------------------------------------------------------------------------
class UIEnum(Enum):
    TERMINAL = 'terminal'
    CUSTOM_TKINTER = 'customtkinter'

    """
    def get_view(self):
        views = {
                self.TERMINAL: Terminal,
                self.CUSTOM_TKINTER: CustomTKinter
        }

        return views[self]()
    """
# ------------------------------------------------------------------------------
