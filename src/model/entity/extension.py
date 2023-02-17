#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/26 18:06:57.300944
#+ Editado:	2023/02/17 18:03:16.485613
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Extension(BaseEntity):
    """Entity Object"""
    name: str
    format_name: Optional[str] = field(default=None)
    format_name_long: Optional[str] = field(default=None)

    def __post_init__(self):
        self.table_name = Config().get_table_name('Extension')
# ------------------------------------------------------------------------------
