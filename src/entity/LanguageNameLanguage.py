#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/21 01:24:01.546584
#+ Editado:	2023/01/24 22:48:42.835476
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.entity import Language, LanguageName
# ------------------------------------------------------------------------------
@dataclass
class LanguageNameLanguage:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('LanguageNameLanguage'))
    language_name: LanguageName
    language: Language
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
