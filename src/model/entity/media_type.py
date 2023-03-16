#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:36:45.461301
#+ Editado:	2023/03/16 21:25:35.215816
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaType(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('MediaType'))
    name: str
    groupable: Optional[int] = field(default=0)
    active: Optional[int] = field(default=1)

    def __str__(self) -> str:
        output =  f'{self.name} ['

        if self.groupable == 1:
            output += _('Groupable')
        else:
            output += _('Non Groupable')

        if self.active == 0:
            output += '| '+_('Dormant')+']'
        else:
            output += ']'

        return output
# ------------------------------------------------------------------------------
