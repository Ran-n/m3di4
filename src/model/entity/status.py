#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:38:25.313276
#+ Editado:	2023/03/18 12:39:21.557924
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Status(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Status'))
    name: str
    active: Optional[int] = field(default=1)

    def __str__(self) -> str:
        output =  self.name

        if self.active == 0:
            output += '['+_('Dormant')+']'

        return output
# ------------------------------------------------------------------------------
