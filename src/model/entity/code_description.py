#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/20 18:28:37.599281
#+ Editado:	2023/02/20 18:28:57.838195
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

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
# ------------------------------------------------------------------------------
