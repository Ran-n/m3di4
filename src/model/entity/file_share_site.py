#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/08 00:36:14.914271
#+ Editado:	2023/02/04 21:28:35.053558
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import ShareSite, File
# ------------------------------------------------------------------------------
@dataclass
class FileShareSite:
    """Entity Object"""
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('FileShareSite'))
    link: str
    share_site: ShareSite
    file: File
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
