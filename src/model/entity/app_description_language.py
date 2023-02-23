#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/23 17:26:06.972853
#+ Editado:	2023/02/23 17:26:18.941749
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, Language, AppDescription
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class AppDescriptionLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('AppDescriptionLanguage'))
    app_desc: AppDescription
    language: Language
# ------------------------------------------------------------------------------
