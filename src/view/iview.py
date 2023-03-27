#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:41:49.401227
#+ Editado:	2023/03/27 15:34:03.206269
# ------------------------------------------------------------------------------
#* Strategy Interface (Strategy Pattern)
# ------------------------------------------------------------------------------
from abc import ABC, abstractmethod
# ------------------------------------------------------------------------------
from src.utils import AddFileTerminalViewOutput

from src.model.entity import Media, Group, Issue
from src.model.entity import Type, Status
from src.model.entity import Platform, ShareSite
from src.model.entity import Warehouse, MediaPlatform
# ------------------------------------------------------------------------------
class iView(ABC):
    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def save(self) -> None:
        pass

    @abstractmethod
    def exit(self) -> None:
        pass

    @abstractmethod
    def update_member_count(self) -> None:
        """
        """

    @abstractmethod
    def add_type(self) -> Type:
        pass

    @abstractmethod
    def add_status(self) -> Status:
        pass

    @abstractmethod
    def add_media(self) -> Media:
        pass

    @abstractmethod
    def add_group(self, id_media: int = None) -> Group:
        pass

    @abstractmethod
    def add_issue(self) -> Issue:
        pass

    @abstractmethod
    def add_platform(self) -> Platform:
        pass

    @abstractmethod
    def add_sharesite(self) -> ShareSite:
        """
        """

    @abstractmethod
    def add_warehouse(self) -> Warehouse:
        """
        """

    @abstractmethod
    def add_file(self) -> AddFileTerminalViewOutput:
        """
        """
    @abstractmethod

    def add_media_platform(self) -> MediaPlatform:
        """
        """
# ------------------------------------------------------------------------------

