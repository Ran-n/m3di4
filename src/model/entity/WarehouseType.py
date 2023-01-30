#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/20 18:16:02.918934
#+ Editado:	2023/01/30 22:38:26.166232
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
# ------------------------------------------------------------------------------
@dataclass
class WarehouseType:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('WarehouseType'))
    name: str
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
