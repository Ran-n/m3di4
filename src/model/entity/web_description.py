#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/19 15:26:10.629501
#+ Editado:	2023/02/19 15:26:19.595322
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, Web
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class WebDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('WebDescription'))
    desc: str
    web: Web
# ------------------------------------------------------------------------------
