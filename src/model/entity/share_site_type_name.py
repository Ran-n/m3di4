#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/15 21:03:03.989792
#+ Editado:	2023/02/15 21:03:30.016766
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import ShareSiteType
# ------------------------------------------------------------------------------
@dataclass
class ShareSiteTypeName:
    """Entity Object"""
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('ShareSiteTypeName'))
    name: str
    share_site_type: ShareSiteType
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
