#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/20 18:16:02.918934
#+ Editado:	2023/03/18 12:34:14.408678
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Type(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Type'))
    name: str
    groupable: Optional[int] = field(default=None)
    active: Optional[int] = field(default=1)

    def __str__(self) -> str:
        output =  f'{self.name}'

        if self.groupable is not None:
            output += ' ['
            if self.groupable == 0:
                output += _('Non ')
            output += _('Groupable') + ']'

        # xFCR? dormant symbol identifier
        if self.active == 0:
            output += ' ['+_('Dormant')+']'

        return output
# ------------------------------------------------------------------------------
