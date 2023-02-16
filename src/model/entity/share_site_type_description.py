#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/15 21:05:40.314045
#+ Editado:	2023/02/16 23:36:04.346724
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, ShareSiteType
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class ShareSiteTypeDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('ShareSiteTypeDescription'))
    desc: str
    share_site_type: ShareSiteType
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
