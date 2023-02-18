#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/18 22:00:58.056263
#+ Editado:	2023/02/18 22:09:38.973859
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, MediaGroup
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaGroupName(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('MediaGroupName'))
    name: str
    media_group: MediaGroup
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
