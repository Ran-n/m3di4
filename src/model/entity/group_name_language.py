#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/18 22:05:21.388335
#+ Editado:	2023/03/16 21:03:37.409553
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, GroupName, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class GroupNameLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('GroupNameLanguage'))
    group_name: GroupName
    language: Language
# ------------------------------------------------------------------------------
