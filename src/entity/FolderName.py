#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:04:14.716403
#+ Editado:	2023/01/24 22:07:26.905358
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
# ------------------------------------------------------------------------------
@dataclass
class FolderName:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('FolderName'))
    name: str
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)

    """
    # xFCR
    def __repr__(self) -> str:
        return f'{self.name}\t[{self.id_}]'
    """
# ------------------------------------------------------------------------------
