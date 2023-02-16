#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 14:52:39.247289
#+ Editado:	2023/02/16 23:26:42.882383
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import BaseEntity, ShareSiteType, Platform
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class ShareSite(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('ShareSite'))
    name: str
    type_: ShareSiteType
    in_platform_id: Optional[int] = field(default=None)
    private: Optional[int] = field(default=None)
    link: Optional[str] = field(default=None)
    platform: Optional[Platform] = field(default=None)
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
