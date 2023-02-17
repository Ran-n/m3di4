#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:41:42.686442
#+ Editado:	2023/02/17 18:00:58.374974
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Media
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaGroup(BaseEntity):
    """Entity Object"""
    number: int
    media: Media
    name: Optional[str] = field(default=None)
    year_start: Optional[int] = field(default=None)
    year_end: Optional[int] = field(default=None)
    active: Optional[int] = field(default=1)

    def __post_init__(self):
        self.table_name = Config().get_table_name('MediaGroup')
# ------------------------------------------------------------------------------
