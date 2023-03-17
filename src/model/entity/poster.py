#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/23 18:39:20.569506
#+ Editado:	2023/03/17 16:31:08.639367
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import create_key, Config
from src.model.entity import BaseEntity, Media, Extension
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Poster(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Poster'))
    media: Media
    extension: Extension
    name: Optional[str] = field(default_factory=create_key)
# ------------------------------------------------------------------------------
