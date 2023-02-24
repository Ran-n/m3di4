#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/19 00:53:10.705486
#+ Editado:	2023/02/24 22:04:21.999160
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Country
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CountryDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CountryDescription'))
    desc: str
    country: Country
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
