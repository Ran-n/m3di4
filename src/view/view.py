#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:40:21.798484
#+ Editado:	2023/02/10 18:01:21.790652
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

            self.model = model
            self.strategy.model = model

            self.controller = None
        else:
            raise InheritException(_(f'Must inherit from {iView.__name__}'))

    def start(self) -> None:
        return self.strategy.start()

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

    def add_media_group(self, id_media: int = None) -> MediaGroup:
        return self.strategy.add_media_group(id_media= id_media)

    def add_media_issue(self) -> MediaIssue:
        return self.strategy.add_media_issue()
# ------------------------------------------------------------------------------
