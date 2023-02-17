#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:58:42.990911
#+ Editado:	2023/02/17 20:40:46.749848
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, MediaName, Country
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaNameCountry(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('MediaNameCountry'))
    media_name: MediaName
    country: Country
# ------------------------------------------------------------------------------
