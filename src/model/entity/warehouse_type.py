#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/20 18:16:02.918934
#+ Editado:	2023/02/24 20:14:49.209581
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class WarehouseType(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('WarehouseType'))
    name: str
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
