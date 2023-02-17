#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/15 21:06:27.183606
#+ Editado:	2023/02/17 18:22:02.994423
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from src.utils import Config
from src.model.entity import BaseEntity, ShareSiteTypeDescription, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class ShareSiteTypeDescriptionLanguage(BaseEntity):
    """Entity Object"""
    share_site_type_desc: ShareSiteTypeDescription
    language: Language

    def __post_init__(self):
        self.table_name = Config().get_table_name('ShareSiteTypeDescriptionLanguage')
# ------------------------------------------------------------------------------
