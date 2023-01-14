#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:40:21.798484
#+ Editado:	2023/01/14 17:36:13.657081
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.view.iview import iView
# ------------------------------------------------------------------------------
from src.model.imodel import iModel
# ------------------------------------------------------------------------------
from src.dtos.Media import Media
# ------------------------------------------------------------------------------
class View:
    def __init__(self, strategy: iView, model: iModel) -> None:
        # obrígase ó uso dunha instancia
        if isinstance(strategy, iView):
            self.view = strategy
            self.model = model
        else:
            raise ValueError('Ten que herdar de ' + iView.__name__)

    def get_media(self) -> Media:
        pass
# ------------------------------------------------------------------------------
