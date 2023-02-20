#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/20 17:57:03.153922
#+ Editado:	2023/02/20 17:57:18.134455
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, Language, EncoderDescription
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class EncoderDescriptionLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('EncoderDescriptionLanguage'))
    encoder_desc: EncoderDescription
    language: Language
# ------------------------------------------------------------------------------
