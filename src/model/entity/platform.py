#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/30 23:00:23.885215
#+ Editado:	2023/02/17 18:02:21.260827
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Platform(BaseEntity):
    """Entity Object"""
    name: str
    desc: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)

    def __post_init__(self):
        self.table_name = Config().get_table_name('Platform')
# ------------------------------------------------------------------------------
