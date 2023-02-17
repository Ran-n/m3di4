#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 13:31:54.424384
#+ Editado:	2023/02/17 20:36:09.911920
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
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Codec'))
    name: str
    type_: CodecType
    name_long: Optional[str] = field(default=None)
    desc: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
