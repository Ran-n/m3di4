#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:58:42.990911
#+ Editado:	2023/02/17 18:20:24.356284
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, MediaName, Country
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaNameCountry(BaseEntity):
    """Entity Object"""
    media_name: MediaName
    country: Country

    def __post_init__(self):
        self.table_name = Config().get_table_name('MediaNameCountry')
# ------------------------------------------------------------------------------
