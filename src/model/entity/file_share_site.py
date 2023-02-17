#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/08 00:36:14.914271
#+ Editado:	2023/02/17 18:03:57.909282
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, ShareSite, File
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class FileShareSite(BaseEntity):
    """Entity Object"""
    link: str
    share_site: ShareSite
    file: File
    active: Optional[int] = field(default=1)

    def __post_init__(self):
        self.table_name = Config().get_table_name('FileShareSite')
# ------------------------------------------------------------------------------
