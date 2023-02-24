#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/23 17:25:23.700767
#+ Editado:	2023/02/24 22:03:24.314665
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, App
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class AppDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('AppDescription'))
    desc: str
    app: App
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
