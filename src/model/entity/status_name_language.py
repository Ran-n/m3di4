#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/29 23:33:56.446838
#+ Editado:	2023/03/18 12:41:03.734636
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, StatusName, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class StatusNameLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('StatusNameLanguage'))
    status_name: StatusName
    language: Language
# ------------------------------------------------------------------------------
