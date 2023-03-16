#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/18 22:10:05.616205
#+ Editado:	2023/03/16 21:03:19.966581
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, GroupDescription, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class GroupDescriptionLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('GroupDescriptionLanguage'))
    group_name: GroupDescription
    language: Language
# ------------------------------------------------------------------------------
