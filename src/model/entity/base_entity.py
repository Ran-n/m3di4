#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/02 22:55:38.799230
#+ Editado:	2023/02/17 20:32:17.543819
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Union, Optional
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass(kw_only=True)
class BaseEntity:
    """Base class"""
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name') or (self.table_name is None):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
