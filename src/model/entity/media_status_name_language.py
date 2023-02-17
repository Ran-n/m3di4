#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/29 23:33:56.446838
#+ Editado:	2023/02/17 18:20:42.981100
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, MediaStatusName, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaStatusNameLanguage(BaseEntity):
    """Entity Object"""
    media_status_name: MediaStatusName
    language: Language

    def __post_init__(self):
        self.table_name = Config().get_table_name('MediaStatusNameLanguage')
# ------------------------------------------------------------------------------
