#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/08 00:36:14.914271
#+ Editado:	2023/02/17 20:37:41.685426
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
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('FileShareSite'))
    link: str
    share_site: ShareSite
    file: File
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
