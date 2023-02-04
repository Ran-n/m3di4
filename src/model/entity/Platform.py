#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/30 23:00:23.885215
#+ Editado:	2023/02/04 18:12:32.737318
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
# ------------------------------------------------------------------------------
@dataclass
class Platform:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('Platform'))
    name: str
    desc: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
