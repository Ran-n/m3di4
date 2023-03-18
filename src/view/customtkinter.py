#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/16 23:05:21.520132
#+ Editado:	2023/03/17 23:35:55.417554
# ------------------------------------------------------------------------------
from src.view import iView
# ------------------------------------------------------------------------------
import logging
import customtkinter

from src.model.entity import Media, Group, Issue
from src.model.entity import Type, MediaStatus
from src.model.entity import Platform, ShareSite
from src.model.entity import Warehouse
# ------------------------------------------------------------------------------
class CustomTKinter(iView):
    def __init__(self) -> None:
        logging.info(_('Starting GUI view'))
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk()

    def start(self) -> None:
        self.root.geometry('800x500')
        self.root.mainloop()

    def save(self) -> None:
        pass

    def exit(self) -> None:
        # nothing need to be done here
        pass

    def update_member_count(self) -> None:
        """
        """
        pass

    def add_type(self) -> Type:
        pass

    def add_media_status(self) -> MediaStatus:
        pass

    def add_media(self) -> Media:
        pass

    def add_group(self) -> Group:
        pass

    def add_issue(self) -> Issue:
        pass

    def add_platform(self) -> Platform:
        pass

    def add_sharesite(self) -> ShareSite:
        """
        """
        pass

    def add_warehouse(self) -> Warehouse:
        """
        """
        pass

    def add_file(self) -> str:
        """
        """
        pass

# ------------------------------------------------------------------------------
