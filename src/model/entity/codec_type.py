#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/27 16:44:24.358200
#+ Editado:	2023/02/16 23:16:45.924253
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import BaseTable
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CodecType(BaseEntity):
    """CodecType Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CodecType'))
    name: str
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
