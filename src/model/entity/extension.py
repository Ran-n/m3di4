#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/26 18:06:57.300944
#+ Editado:	2023/02/17 20:36:30.322167
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
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Extension'))
    name: str
    format_name: Optional[str] = field(default=None)
    format_name_long: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
