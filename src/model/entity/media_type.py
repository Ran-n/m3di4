#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:36:45.461301
#+ Editado:	2023/02/17 18:01:43.157359
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaType(BaseEntity):
    """Entity Object"""
    name: str
    desc: Optional[str] = field(default=None)
    groupable: Optional[int] = field(default=0)
    active: Optional[int] = field(default=1)

    def __post_init__(self):
        self.table_name = Config().get_table_name('MediaType')
# ------------------------------------------------------------------------------
