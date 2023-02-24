#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/02 22:55:38.799230
#+ Editado:	2023/02/24 20:16:23.682969
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class App(BaseEntity):
    """App Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('App'))
    name: str
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
