#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/20 18:18:03.195457
#+ Editado:	2023/01/27 20:30:46.256402
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.entity import ShareSite
# ------------------------------------------------------------------------------
@dataclass
class ShareSiteSubs:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('ShareSiteSubs'))
    subs: int
    share_site: ShareSite
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
