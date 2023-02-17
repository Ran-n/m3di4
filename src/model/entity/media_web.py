#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:06:39.547649
#+ Editado:	2023/02/17 18:05:22.351181
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Media, Web
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaWeb(BaseEntity):
    """Entity Object"""
    media: Media
    web: Web
    link: str
    active: Optional[str] = field(default=1)

    def __post_init__(self):
        self.table_name = Config().get_table_name('MediaWeb')
# ------------------------------------------------------------------------------
