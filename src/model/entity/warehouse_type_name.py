#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 13:44:15.192121
#+ Editado:	2023/02/16 23:36:24.583964
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, WarehouseType
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class WarehouseTypeName(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('WarehouseTypeName'))
    name: str
    warehouse_type: WarehouseType
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
