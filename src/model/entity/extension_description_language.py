#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/22 21:53:23.005026
#+ Editado:	2023/02/22 21:53:32.862553
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, Language, ExtensionDescription
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class ExtensionDescriptionLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('ExtensionDescriptionLanguage'))
    extension_desc: ExtensionDescription
    language: Language
# ------------------------------------------------------------------------------
