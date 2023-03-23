#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:08:25.622146
#+ Editado:	2023/03/23 22:13:09.521202
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Type
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Platform(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Platform'))
    name: str
    acronym: Optional[str] = field(default=None)
    name_long: Optional[str] = field(default=None)
    link: Optional[str] = field(default=None)
    type_: Optional[Type] = field(default=None)
    active: Optional[int] = field(default=1)

    def __str__(self) -> str:
        string = self.name
        if self.acronym:
            string += f' ({self.acronym})'
        if self.type_:
            string += f' - {self.type_}'
        return string
# ------------------------------------------------------------------------------
