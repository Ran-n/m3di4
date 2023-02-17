#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/29 23:20:04.639454
#+ Editado:	2023/02/17 18:20:52.498529
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, MediaTypeName, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaTypeNameLanguage(BaseEntity):
    """Entity Object"""
    media_type_name: MediaTypeName
    language: Language

    def __post_init__(self):
        self.table_name = Config().get_table_name('MediaTypeNameLanguage')
# ------------------------------------------------------------------------------
