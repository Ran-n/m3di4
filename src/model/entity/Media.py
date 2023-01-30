#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:09:59.330936
#+ Editado:	2023/01/30 22:41:28.466344
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import MediaType, MediaStatus
# ------------------------------------------------------------------------------
@dataclass
class Media:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('Media'))
    name: str
    type_: MediaType
    status: MediaStatus
    year_start: int
    year_end: Optional[int] = field(default=None)
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
