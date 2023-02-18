#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:41:42.686442
#+ Editado:	2023/02/18 15:18:05.356005
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
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('MediaGroup'))
    number: int
    media: Media
    name: Optional[str] = field(default=None)
    desc: Optional[str] = field(default=None)
    year_start: Optional[int] = field(default=None)
    year_end: Optional[int] = field(default=None)
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
