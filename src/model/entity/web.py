#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:08:25.622146
#+ Editado:	2023/02/17 18:06:04.160590
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Web(BaseEntity):
    """Entity Object"""
    name: str
    acronym: Optional[str] = field(default=None)
    link: Optional[str] = field(default=None)
    desc: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)

    def __post_init__(self):
        self.table_name = Config().get_table_name('Web')
# ------------------------------------------------------------------------------
