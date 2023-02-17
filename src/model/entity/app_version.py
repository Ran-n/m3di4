#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/02 22:59:18.477529
#+ Editado:	2023/02/17 20:34:46.885118
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, App
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class AppVersion(BaseEntity):
    """AppVersion Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('AppVersion'))
    app: App
    number: int
    name: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)
    num_bit_processor: Optional[int] = field(default=None)
# ------------------------------------------------------------------------------
