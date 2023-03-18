#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 00:18:35.149777
#+ Editado:	2023/03/17 19:46:46.087752
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Type
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Warehouse(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Warehouse'))
    name: str
    type_: Type
    size: Optional[int] = field(default=None)
    filled: Optional[int] = field(default=None)
    content: Optional[str] = field(default=None)
    health: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)

    def __str__(self) -> None:
        return self.name
# ------------------------------------------------------------------------------
