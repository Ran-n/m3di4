#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/02 22:59:18.477529
#+ Editado:	2023/02/02 23:06:38.902157
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import App
# ------------------------------------------------------------------------------
@dataclass
class AppVersion:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('AppVersion'))
    id_app: App
    number: int
    name: Optional[str] = field(default=None)
    num_bit_processor: Optional[int] = field(default=None)
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
