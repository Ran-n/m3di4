#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/20 17:56:36.685554
#+ Editado:	2023/02/24 22:04:28.534809
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Encoder
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class EncoderDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('EncoderDescription'))
    desc: str
    encoder: Encoder
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
