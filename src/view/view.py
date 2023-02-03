#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:40:21.798484
#+ Editado:	2023/02/03 20:40:14.731102
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.view import iView
# ------------------------------------------------------------------------------
from src.model import iModel
# ------------------------------------------------------------------------------
from src.model.entity import Media
# ------------------------------------------------------------------------------
class View:
    def __init__(self, strategy: iView, model: iModel) -> None:
        # demand the use of an intance of view
        if isinstance(strategy, iView):
            self.strategy = strategy
            self.strategy.model = model
            self.model = model
        else:
            raise ValueError(f'Must inherit from {iView.__name__}')

    def menu(self, options: dict) -> int:
        return self.strategy.menu(options)

    def exit(self) -> None:
        self.strategy.exit()

    def add_media(self) -> Media:
        return self.strategy.add_media()
# ------------------------------------------------------------------------------
