#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 13:45:17.157511
#+ Editado:	2023/02/16 23:36:14.469303
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Warehouse
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class WarehouseDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('WarehouseDescription'))
    desc: str
    warehouse: Warehouse
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
