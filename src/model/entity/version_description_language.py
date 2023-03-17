#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/23 17:18:02.441467
#+ Editado:	2023/03/17 16:27:07.656820
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, Language, VersionDescription
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class VersionDescriptionLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('VersionDescriptionLanguage'))
    version_desc: VersionDescription
    language: Language
# ------------------------------------------------------------------------------
