#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 13:48:04.701991
#+ Editado:	2023/02/16 23:35:53.000034
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, PlatformDescription, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class PlatformDescriptionLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('PlatformDescriptionLanguage'))
    platform_desc: PlatformDescription
    language: Language
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
