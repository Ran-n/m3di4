#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:58:36.138946
#+ Editado:	2023/02/17 18:20:32.544733
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, MediaName, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaNameLanguage(BaseEntity):
    """Entity Object"""
    media_name: MediaName
    language: Language

    def __post_init__(self):
        self.table_name = Config().get_table_name('MediaNameLanguage')
# ------------------------------------------------------------------------------
