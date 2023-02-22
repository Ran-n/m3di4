#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/22 21:52:39.818083
#+ Editado:	2023/02/22 21:53:07.422821
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, Extension
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class ExtensionDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('ExtensionDescription'))
    desc: str
    extension: Extension
# ------------------------------------------------------------------------------
