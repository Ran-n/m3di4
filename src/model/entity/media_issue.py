#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:41:48.278353
#+ Editado:	2023/02/17 18:01:07.007669
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Media, MediaGroup
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaIssue(BaseEntity):
    """Entity Object"""
    position: int
    media: Media
    media_group: MediaGroup
    name: Optional[str] = field(default=None)
    date: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)

    def __post_init__(self):
        self.table_name = Config().get_table_name('MediaIssue')
# ------------------------------------------------------------------------------
