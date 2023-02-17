#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/15 21:03:03.989792
#+ Editado:	2023/02/17 18:22:12.094594
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, ShareSiteType
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class ShareSiteTypeName(BaseEntity):
    """Entity Object"""
    name: str
    share_site_type: ShareSiteType

    def __post_init__(self):
        self.table_name = Config().get_table_name('ShareSiteTypeName')
# ------------------------------------------------------------------------------
