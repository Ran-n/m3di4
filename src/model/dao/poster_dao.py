#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/04/05 15:22:15.926557
#+ Editado:	2023/04/05 17:29:46.271475
# ------------------------------------------------------------------------------
from src.model import iModel

from src.model.entity import Poster
from src.model.dao import ExtensionDAO
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
class PosterDAO:
    """Data Access Object"""

    def __new__(self, model: iModel):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
            self.instance.model = model
        return self.instance

    def save(self, poster: Poster) -> Poster:
        """Saving an DAO object"""
        poster.extension = ExtensionDAO(self.model).save(poster.extension)
        if not self.model.exists(poster):
            self.model.insert(poster)
        return self.model.get_by_nk(poster)
# ------------------------------------------------------------------------------
