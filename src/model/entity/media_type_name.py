#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/29 23:20:04.639454
#+ Editado:	2023/02/17 18:05:19.214945
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, MediaType
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaTypeName(BaseEntity):
    """Entity Object"""
    name: str
    media_type: MediaType
    desc: Optional[str] = field(default=None)

    def __post_init__(self):
        self.table_name = Config().get_table_name('MediaTypeName')
# ------------------------------------------------------------------------------
