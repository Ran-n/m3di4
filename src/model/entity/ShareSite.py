#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 14:52:39.247289
#+ Editado:	2023/01/28 00:31:13.964386
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import ShareSiteType
# ------------------------------------------------------------------------------
@dataclass
class ShareSite:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('ShareSite'))
    name: str
    type_: ShareSiteType
    private: Optional[int] = field(default=None)
    link: Optional[str] = field(default=None)
    platform: Optional[str] = field(default=None)
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)

    """
    # xFCR
    def __repr__(self) -> str:
        times = 1
        if len(self.name) < 15:
            times=2
        return f'{self.name}'+times*'\t'+f'[{self.id_}]'
    """
# ------------------------------------------------------------------------------
