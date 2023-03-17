#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:53:33.927294
#+ Editado:	2023/03/17 16:32:00.388388
# ------------------------------------------------------------------------------
from src.model import iModel

from src.model.entity import File, Extension, Folder, Version, App, Encoder
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
class FileDao:
    """Data Access Object"""

    def __init__(self, model: iModel) -> None:
        self.model = model

    def __get_extension(self, extension: Extension) -> Extension:
        """Bring the full data of the object from DB or insert it."""
        if extension:
            # xFCR use nk
            found_extension = self.model.get_by_name(table_name=Extension.table_name,
                                                     name=extension.name)
            if not found_extension:
                self.model.insert(extension)
                return self.__get_extension(extension)
            return found_extension

    def __get_folder(self, folder: Folder) -> Folder:
        """Bring the full data of the object from DB or insert it."""
        if folder:
            # xFCR use nk
            found_folder = self.model.get_by_name(table_name=Folder.table_name,
                                                  name=folder.path)
            if not found_folder:
                self.model.insert(folder)
                return self.__get_folder(folder)
            return found_folder

    def __get_app(self, app: App) -> App:
        """Bring the full data of the object from DB or insert it."""
        if app:
            # xFCR use nk
            found_app = self.model.get_by_name(table_name=App.table_name,
                                                  name=app.name)
            if not found_app:
                self.model.insert(app)
                return self.__get_app(app)
            return found_app

    def __get_version(self, version: Version) -> Version:
        """Bring the full data of the object from DB or insert it."""
        if version:
            version.app=self.__get_app(version.app)
            found_version = self.model.get_by_nk(version)
            if not found_version:
                self.model.insert(version)
                return self.__get_version(version)
            return found_version

    def __get_encoder(self, encoder: Encoder) -> Encoder:
        """Bring the full data of the object from DB or insert it."""
        if encoder:
            found_encoder = self.model.get_by_nk(encoder)
            if not found_encoder:
                self.model.insert(encoder)
                return self.__get_encoder(encoder)
            return found_encoder

    def save(self, file: File) -> File:
        file.extension=self.__get_extension(file.extension)
        file.folder=self.__get_folder(file.folder)

        # at this point it can already be check if it exists
        found_file = self.model.get_by_nk(file)
        if found_file:
            return found_file

        file.version=self.__get_version(file.version)
        file.encoder=self.__get_encoder(file.encoder)

        self.model.insert(file)
        return self.model.get_by_nk(file)
# ------------------------------------------------------------------------------
