#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/19 13:12:35.072093
#+ Editado:	2023/02/19 13:12:39.762154
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, Codec
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CodecDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CodecDescription'))
    desc: str
    codec: Codec
# ------------------------------------------------------------------------------
