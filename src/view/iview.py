#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:41:49.401227
#+ Editado:	2023/03/16 21:01:20.084848
# ------------------------------------------------------------------------------
#* Strategy Interface (Strategy Pattern)
# ------------------------------------------------------------------------------
from abc import ABC, abstractmethod
# ------------------------------------------------------------------------------
from src.model.entity import Media, Group, MediaIssue
from src.model.entity import MediaType, MediaStatus
from src.model.entity import Platform, ShareSiteType, ShareSite
from src.model.entity import WarehouseType, Warehouse
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
    def add_media_type(self) -> MediaType:
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
    def add_media_issue(self) -> MediaIssue:
        pass

    @abstractmethod
    def add_platform(self) -> Platform:
        pass

    @abstractmethod
    def add_sharesite_type(self) -> ShareSiteType:
        """
        """

    @abstractmethod
    def add_sharesite(self) -> ShareSite:
        """
        """

    @abstractmethod
    def add_warehouse_type(self) -> WarehouseType:
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

