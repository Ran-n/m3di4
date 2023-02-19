#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/19 13:13:58.457148
#+ Editado:	2023/02/19 14:19:25.723511
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, Language, CodecDescription
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CodecDescriptionLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CodecDescriptionLanguage'))
    codec_desc: CodecDescription
    language: Language
# ------------------------------------------------------------------------------
