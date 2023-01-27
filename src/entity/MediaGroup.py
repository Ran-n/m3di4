#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:41:42.686442
#+ Editado:	2023/01/24 23:06:59.517347
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.entity import Media
# ------------------------------------------------------------------------------
@dataclass
class MediaGroup:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('MediaGroup'))
    number: int
    media: Media
    name: Optional[str] = field(default=None)
    year_start: Optional[int] = field(default=None)
    year_end: Optional[int] = field(default=None)
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------

