#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/18 22:07:43.678965
#+ Editado:	2023/02/18 22:07:52.272407
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Media
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('MediaDescription'))
    name: str
    media: Media
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
