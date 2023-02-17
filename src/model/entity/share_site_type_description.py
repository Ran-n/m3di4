#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/15 21:05:40.314045
#+ Editado:	2023/02/17 18:21:57.316634
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, ShareSiteType
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class ShareSiteTypeDescription(BaseEntity):
    """Entity Object"""
    desc: str
    share_site_type: ShareSiteType

    def __post_init__(self):
        self.table_name = Config().get_table_name('ShareSiteTypeDescription')
# ------------------------------------------------------------------------------
