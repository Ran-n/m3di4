#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/19 12:33:53.667862
#+ Editado:	2023/02/19 12:34:04.199933
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, CodecType
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CodecTypeDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CodecTypeDescription'))
    desc: str
    codec_type: CodecType
# ------------------------------------------------------------------------------
