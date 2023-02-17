#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/20 18:18:03.195457
#+ Editado:	2023/02/17 18:21:49.131600
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, ShareSite
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class ShareSiteSubs(BaseEntity):
    """Entity Object"""
    sub_num: int
    share_site: ShareSite

    def __post_init__(self):
        self.table_name = Config().get_table_name('ShareSiteSubs')
# ------------------------------------------------------------------------------
