#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/15 21:04:16.341950
#+ Editado:	2023/02/17 18:22:19.571525
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, ShareSiteTypeName, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class ShareSiteTypeNameLanguage(BaseEntity):
    """Entity Object"""
    share_site_type_name: ShareSiteTypeName
    language: Language

    def __post_init__(self):
        self.table_name = Config().get_table_name('ShareSiteTypeNameLanguage')
# ------------------------------------------------------------------------------
