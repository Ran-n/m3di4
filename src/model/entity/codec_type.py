#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/27 16:44:24.358200
#+ Editado:	2023/02/17 18:18:53.943046
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CodecType(BaseEntity):
    """Entity Object"""
    name: str

    def __post_init__(self):
        self.table_name = Config().get_table_name('CodecType')
# ------------------------------------------------------------------------------
