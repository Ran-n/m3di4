#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 13:31:54.424384
#+ Editado:	2023/02/16 23:16:07.812802
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import BaseTable, CodecType
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Codec(BaseEntity):
    """Codec Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Codec'))
    name: str
    type_: CodecType
    name_long: Optional[str] = field(default=None)
    desc: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
