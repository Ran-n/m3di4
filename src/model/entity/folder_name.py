#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:04:14.716403
#+ Editado:	2023/02/16 23:34:53.328517
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class FolderName(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('FolderName'))
    name: str
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
