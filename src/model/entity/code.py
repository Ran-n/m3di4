#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/21 01:19:35.116684
#+ Editado:	2023/02/16 23:15:48.498755
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import BaseTable
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Code(BaseEntity):
    """Code Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Code'))
    name: str
    desc: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
