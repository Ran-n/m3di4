#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/20 18:18:03.195457
#+ Editado:	2023/02/16 23:36:01.200593
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, ShareSite
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class ShareSiteSubs(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('ShareSiteSubs'))
    sub_num: int
    share_site: ShareSite
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
