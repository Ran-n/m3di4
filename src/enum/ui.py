#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/03 16:41:07.729202
#+ Editado:	2023/02/03 20:35:48.164762
# ------------------------------------------------------------------------------
from enum import Enum

#from src.view import Terminal, CustomTKinter
# ------------------------------------------------------------------------------
class UI(Enum):
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
