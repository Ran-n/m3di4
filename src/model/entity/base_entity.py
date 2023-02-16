#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/02 22:55:38.799230
#+ Editado:	2023/02/17 00:37:10.999200
# ------------------------------------------------------------------------------
from dataclasses import dataclass
from typing import Union
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class BaseEntity:
    """Base class"""

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if attr != 'table_name':
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
