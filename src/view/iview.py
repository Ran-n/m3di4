#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:41:49.401227
#+ Editado:	2023/03/17 19:48:09.004445
# ------------------------------------------------------------------------------
#* Strategy Interface (Strategy Pattern)
# ------------------------------------------------------------------------------
from abc import ABC, abstractmethod
# ------------------------------------------------------------------------------
from src.model.entity import Media, Group, Issue
from src.model.entity import Type, MediaStatus
from src.model.entity import Platform, ShareSite
from src.model.entity import Warehouse
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
    def add_media_status(self) -> MediaStatus:
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
    def add_file(self) -> str:
        """
        """
# ------------------------------------------------------------------------------

