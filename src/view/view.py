#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:40:21.798484
#+ Editado:	2023/03/28 22:18:37.152236
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.view import iView
# ------------------------------------------------------------------------------
from src.model import iModel
# ------------------------------------------------------------------------------
from src.exception import InheritException
from src.utils import AddFileTerminalViewOutput

from src.model.entity import Media, Group, Issue
from src.model.entity import Type, Status
from src.model.entity import Platform, ShareSite
from src.model.entity import Warehouse, MediaPlatform
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

    def update_member_count(self) -> None:
        """"""
        self.strategy.update_member_count()

    def download_posters(self) -> None:
        """"""
        self.strategy.download_posters()


    def add_type(self) -> Type:
        return self.strategy.add_type()

    def add_status(self) -> Status:
        return self.strategy.add_status()

    def add_media(self) -> Media:
        return self.strategy.add_media()

    def add_group(self, id_media: int = None) -> Group:
        return self.strategy.add_group(id_media=id_media)

    def add_issue(self) -> Issue:
        return self.strategy.add_issue()

    def add_platform(self) -> Platform:
        return self.strategy.add_platform()

    def add_sharesite(self) -> ShareSite:
        return self.strategy.add_sharesite()

    def add_warehouse(self) -> Warehouse:
        return self.strategy.add_warehouse()

    def add_file(self) -> AddFileTerminalViewOutput:
        return self.strategy.add_file()

    def add_media_platform(self) -> MediaPlatform:
        return self.strategy.add_media_platform()

# ------------------------------------------------------------------------------
