#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# + Autor:  	Ran#
# + Creado: 	2023/01/04 23:45:45.121317
# + Editado:	2023/02/18 22:02:04.759287
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Media
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaName(BaseEntity):
    """Entity Object"""

    table_name: str = field(init=False, repr=False, default=Config().get_table_name("MediaName"))
    name: str
    media: Media
    active: Optional[int] = field(default=1)


# ------------------------------------------------------------------------------
