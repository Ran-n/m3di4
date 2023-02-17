#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/29 23:17:57.682598
#+ Editado:	2023/02/17 18:05:08.969021
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, MediaStatus
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaStatusName(BaseEntity):
    """Entity Object"""
    name: str
    media_status: MediaStatus
    desc: Optional[str] = field(default=None)

    def __post_init__(self):
        self.table_name = Config().get_table_name('MediaStatusName')
# ------------------------------------------------------------------------------
