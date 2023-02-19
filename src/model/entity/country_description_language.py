#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/19 00:54:27.296381
#+ Editado:	2023/02/19 14:18:50.090338
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, Language, CountryDescription
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CountryDescriptionLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CountryDescriptionLanguage'))
    country_desc: CountryDescription
    language: Language
# ------------------------------------------------------------------------------
