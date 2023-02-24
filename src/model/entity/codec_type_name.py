#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/19 12:32:45.424663
#+ Editado:	2023/02/24 21:15:24.152774
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import CodecType
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CodecTypeName(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CodecTypeName'))
    name: str
    codec_type: CodecType
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
