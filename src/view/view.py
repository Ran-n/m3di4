#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:40:21.798484
#+ Editado:	2023/01/29 22:37:21.564472
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.view import iView
# ------------------------------------------------------------------------------
from src.model import iModel
# ------------------------------------------------------------------------------
from src.entity import Media
# ------------------------------------------------------------------------------
class View:
    def __init__(self, strategy: iView, model: iModel) -> None:
        # obrígase ó uso dunha instancia
        if isinstance(strategy, iView):
            self.strategy = strategy
            self.strategy.model = model
            self.model = model
        else:
            raise ValueError('Ten que herdar de ' + iView.__name__)

    def menu(self, options: dict) -> int:
        return self.strategy.menu(options)

    def exit(self) -> None:
        self.strategy.exit()

    def add_media(self) -> Media:
        return self.strategy.add_media()
# ------------------------------------------------------------------------------
