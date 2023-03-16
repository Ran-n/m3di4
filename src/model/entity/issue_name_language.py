#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/18 22:06:03.157874
#+ Editado:	2023/03/16 21:47:21.267868
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, IssueName, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class IssueNameLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('IssueNameLanguage'))
    issue_name: IssueName
    language: Language
# ------------------------------------------------------------------------------
