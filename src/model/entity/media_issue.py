#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:41:48.278353
#+ Editado:	2023/02/16 23:25:02.891297
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import BaseEntity, Media, MediaGroup
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaIssue(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('MediaIssue'))
    position: int
    media: Media
    media_group: MediaGroup
    name: Optional[str] = field(default=None)
    date: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
