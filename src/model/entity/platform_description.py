#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/13 22:20:32.532650
#+ Editado:	2023/02/17 18:20:59.401358
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, Platform
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class PlatformDescription(BaseEntity):
    """Entity Object"""
    desc: str
    platform: Platform

    def __post_init__(self):
        self.table_name = Config().get_table_name('PlatformDescription')
# ------------------------------------------------------------------------------
