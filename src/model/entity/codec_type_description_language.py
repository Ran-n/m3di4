#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/19 12:34:17.222611
#+ Editado:	2023/02/19 12:34:24.632871
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, Language, CodecTypeDescription
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CodecTypeDescriptionLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CodecTypeDescriptionLanguage'))
    codec_type_desc: CodecTypeDescription
    language: CodecType
# ------------------------------------------------------------------------------
