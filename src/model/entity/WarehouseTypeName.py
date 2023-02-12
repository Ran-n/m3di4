#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 13:44:15.192121
#+ Editado:	2023/02/12 13:44:50.613745
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import WarehouseType
# ------------------------------------------------------------------------------
@dataclass
class WarehouseTypeName:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('WarehouseTypeName'))
    name: str
    warehouse_type: WarehouseType
    desc: Optional[str] = field(default=None)
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
