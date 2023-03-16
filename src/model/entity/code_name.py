#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/03/12 20:14:44.691424
#+ Editado:	2023/03/12 20:17:20.151625
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Code
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CodeName(BaseEntity):
    """Code Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CodeName'))
    name: str
    code: Code
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
