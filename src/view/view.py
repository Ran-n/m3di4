#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:40:21.798484
#+ Editado:	2023/02/05 13:43:52.610695
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.view import iView
# ------------------------------------------------------------------------------
from src.model import iModel
# ------------------------------------------------------------------------------
from src.exception import InheritException

from src.model.entity import Media, MediaGroup, MediaIssue
from src.model.entity import MediaType, MediaStatus
# ------------------------------------------------------------------------------
class View:
    def __init__(self, strategy: iView, model: iModel) -> None:
        # demand the use of an intance of view
        if isinstance(strategy, iView):
            self.strategy = strategy
            self.strategy.model = model
            self.model = model
        else:
            raise InheritException(_(f'Must inherit from {iView.__name__}'))

    def menu(self, options: dict) -> int:
        return self.strategy.menu(options)

    def save(self) -> None:
        return self.strategy.save()

    def exit(self) -> None:
        self.strategy.exit()

    def add_media_type(self) -> MediaType:
        return self.strategy.add_media_type()

    def add_media_status(self) -> MediaStatus:
        return self.strategy.add_media_status()

    def add_media(self) -> Media:
        return self.strategy.add_media()

    def add_media_group(self) -> MediaGroup:
        return self.strategy.add_media_group()
# ------------------------------------------------------------------------------
