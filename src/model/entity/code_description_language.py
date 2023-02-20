#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/20 18:29:18.726059
#+ Editado:	2023/02/20 18:29:26.225921
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, Language, CodeDescription
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CodeDescriptionLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CodeDescriptionLanguage'))
    code_desc: CodeDescription
    language: Language
# ------------------------------------------------------------------------------
