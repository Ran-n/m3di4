#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/02 22:55:38.799230
#+ Editado:	2023/02/02 22:55:55.219602
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
# ------------------------------------------------------------------------------
@dataclass
class App:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('App'))
    name: str
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
