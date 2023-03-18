#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 13:45:17.157511
#+ Editado:	2023/03/17 19:44:29.025003
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Type
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class TypeDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('TypeDescription'))
    desc: str
    type_: Type
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
