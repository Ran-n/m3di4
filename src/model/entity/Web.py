#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:08:25.622146
#+ Editado:	2023/02/04 19:22:27.195973
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
# ------------------------------------------------------------------------------
@dataclass
class Web:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('Web'))
    name: str
    acronym: Optional[str] = field(default=None)
    link: Optional[str] = field(default=None)
    desc: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)

    """
    # xFCR
    def __repr__(self) -> str:
        repeat = 1
        if len(self.name) < 22:
            repeat = 2
        return f'{self.name}' + repeat*'\t' + f'[{self.id_}]'
    """
# ------------------------------------------------------------------------------
