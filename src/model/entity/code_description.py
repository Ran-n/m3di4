#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/20 18:28:37.599281
#+ Editado:	2023/02/24 22:03:48.057810
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Code
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CodeDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CodeDescription'))
    desc: str
    code: Code
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
