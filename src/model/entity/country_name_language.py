#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/01 21:21:01.942449
#+ Editado:	2023/02/16 22:30:50.559656
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import CountryName, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CountryNameLanguage:
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CountryNameLanguage'))
    country_name: CountryName
    language: Language
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if attr != 'table_name':
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
