#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/18 22:10:25.573955
#+ Editado:	2023/03/16 21:46:36.952911
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Issue
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class IssueDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('IssueDescription'))
    name: str
    issue: Issue
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
