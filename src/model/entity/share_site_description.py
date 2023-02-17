#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/15 22:36:04.981766
#+ Editado:	2023/02/17 18:21:35.665349
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, ShareSite
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class ShareSiteDescription(BaseEntity):
    """Entity Object"""
    desc: str
    share_site: ShareSite

    def __post_init__(self):
        self.table_name = Config().get_table_name('ShareSiteDescription')
# ------------------------------------------------------------------------------
