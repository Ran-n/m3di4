#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 20:59:37.407686
#+ Editado:	2023/02/12 20:59:57.232593
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import Language
# ------------------------------------------------------------------------------
@dataclass
class LanguageDescription:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('LanguageDescription'))
    description: str
    language: Language
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
