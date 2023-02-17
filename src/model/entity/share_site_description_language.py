#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/15 22:39:09.782944
#+ Editado:	2023/02/17 18:21:42.150029
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, ShareSiteDescription, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class ShareSiteDescriptionLanguage(BaseEntity):
    """Entity Object"""
    share_site_desc: ShareSiteDescription
    language: Language

    def __post_init__(self):
        self.table_name = Config().get_table_name('ShareSiteDescriptionLanguage')
# ------------------------------------------------------------------------------
