#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/23 17:17:21.124687
#+ Editado:	2023/03/17 16:26:46.926773
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Version
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class VersionDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('VersionDescription'))
    desc: str
    version: Version
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
