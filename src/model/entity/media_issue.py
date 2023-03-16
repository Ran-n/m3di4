#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:41:48.278353
#+ Editado:	2023/03/16 21:07:05.467011
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Media, Group
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaIssue(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('MediaIssue'))
    position: int
    media: Media
    group: Optional[Group]
    name: Optional[str] = field(default=None)
    date: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)

    def __str__(self) -> str:
        string = f'{self.media} - '

        if self.group:
            string += f'{self.group.number}x{self.position:0{2}}'
        else:
            string += f'{self.position}'
        return string
# ------------------------------------------------------------------------------
