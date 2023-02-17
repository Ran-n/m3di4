#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/23 18:39:20.569506
#+ Editado:	2023/02/17 18:05:02.250544
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import create_key, Config
from src.model.entity import BaseEntity, Media, Extension
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaPoster(BaseEntity):
    """Entity Object"""
    media: Media
    extension: Extension
    name: Optional[str] = field(default_factory=create_key)

    def __post_init__(self):
        self.table_name = Config().get_table_name('MediaPoster')
# ------------------------------------------------------------------------------
