#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/03/13 17:22:48.547002
#+ Editado:	2023/03/16 18:55:54.500638
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Track, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class TrackLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('TrackLanguage'))
    track: Track
    language: Language
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
