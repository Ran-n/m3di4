#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/21 01:23:38.362620
#+ Editado:	2023/02/16 23:30:41.534604
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Language, Code
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class LanguageCode(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('LanguageCode'))
    language: Language
    code: Code
    codename: str
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
