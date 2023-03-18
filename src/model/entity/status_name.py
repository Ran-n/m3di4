#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/29 23:17:57.682598
#+ Editado:	2023/03/18 12:40:50.867786
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Status
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class StatusName(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('StatusName'))
    name: str
    status: Status
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
