#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/27 16:44:24.358200
#+ Editado:	2023/02/24 20:15:03.454248
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CodecType(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CodecType'))
    name: str
# ------------------------------------------------------------------------------
