#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/29 23:20:04.639454
#+ Editado:	2023/02/24 21:15:59.198160
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
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('MediaTypeName'))
    name: str
    media_type: MediaType
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
