#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 13:31:54.424384
#+ Editado:	2023/01/28 00:14:57.748973
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.entity import CodecType
# ------------------------------------------------------------------------------
@dataclass
class Codec:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('Codec'))
    name: str
    type_: CodecType
    name_long: Optional[str] = field(default=None)
    desc: Optional[str] = field(default=None)
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
