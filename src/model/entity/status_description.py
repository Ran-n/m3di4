#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/19 14:16:04.980216
#+ Editado:	2023/03/18 12:39:40.386233
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Status
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class StatusDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('StatusDescription'))
    desc: str
    status: Status
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
