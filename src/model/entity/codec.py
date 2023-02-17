#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 13:31:54.424384
#+ Editado:	2023/02/17 18:02:57.048962
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, CodecType
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Codec(BaseEntity):
    """Codec Entity Object"""
    name: str
    type_: CodecType
    name_long: Optional[str] = field(default=None)
    desc: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)

    def __post_init__(self):
        self.table_name = Config().get_table_name('Codec')
# ------------------------------------------------------------------------------
