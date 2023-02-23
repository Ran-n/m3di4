#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/23 17:18:02.441467
#+ Editado:	2023/02/23 17:18:11.481485
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, Language, AppVersionDescription
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class AppVersionDescriptionLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('AppVersionDescriptionLanguage'))
    app_version_desc: AppVersionDescription
    language: Language
# ------------------------------------------------------------------------------
