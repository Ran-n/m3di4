#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/29 23:17:57.682598
#+ Editado:	2023/02/16 23:25:44.058632
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import BaseEntity, MediaStatus
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaStatusName(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('MediaStatusName'))
    name: str
    media_status: MediaStatus
    desc: Optional[str] = field(default=None)
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
