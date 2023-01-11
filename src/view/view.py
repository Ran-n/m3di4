#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:40:21.798484
#+ Editado:	2023/01/11 22:52:16.116049
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.view.iview import iView
# ------------------------------------------------------------------------------
class View:
    def __init__(self, view: iView) -> None:
        # obrígase ó uso dunha instancia
        if isinstance(view, iView):
            self.view = view
        else:
            raise ValueError('Ten que herdar de ' + iView.__name__)
# ------------------------------------------------------------------------------
