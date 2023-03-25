#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:09:59.330936
#+ Editado:	2023/03/25 12:27:41.282587
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Type, Status
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Media(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Media'))
    name: str
    type_: Type
    status: Status
    date_start: int
    date_end: Optional[int] = field(default=None)
    active: Optional[int] = field(default=1)

    def __str__(self) -> str:
        string = f'{self.name}'
        if self.date_start:
            string += f' ({self.date_start}'
            if self.date_end:
                string += f'-{self.date_end}'
            elif self.type_.groupable == 1:
                string += '-'
            string += ')'
        return string
# ------------------------------------------------------------------------------
