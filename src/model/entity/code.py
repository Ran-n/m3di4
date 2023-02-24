#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/21 01:19:35.116684
#+ Editado:	2023/02/24 20:15:22.428738
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Code(BaseEntity):
    """Code Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Code'))
    name: str
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
