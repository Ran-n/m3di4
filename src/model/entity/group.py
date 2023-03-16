#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:41:42.686442
#+ Editado:	2023/03/16 22:00:41.013364
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Media
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Group(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Group'))
    number: int
    media: Media
    name: Optional[str] = field(default=None)
    year_start: Optional[int] = field(default=None)
    year_end: Optional[int] = field(default=None)
    active: Optional[int] = field(default=1)

    def __str__(self) -> str:
        return f'{self.media} - {self.number}'
# ------------------------------------------------------------------------------
