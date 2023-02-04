#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 14:52:39.247289
#+ Editado:	2023/02/04 19:52:00.895780
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import ShareSiteType, Platform
# ------------------------------------------------------------------------------
@dataclass
class ShareSite:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('ShareSite'))
    name: str
    type_: ShareSiteType
    private: Optional[int] = field(default=None)
    link: Optional[str] = field(default=None)
    platform: Optional[Platform] = field(default=None)
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
