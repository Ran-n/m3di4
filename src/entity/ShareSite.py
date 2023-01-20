#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/07 14:52:39.247289
#+ Editado:	2023/01/20 17:51:23.840025
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import create_key
# ------------------------------------------------------------------------------
@dataclass
class ShareSite:
    table_name: str = field(init=False, default='_Compartir Lugar')
    name: str
    private: int
    link: str
    type_: str
    platform: str
    id_: str = field(default_factory=create_key)

    # xFCR
    def __repr__(self) -> str:
        times = 1
        if len(self.name) < 15:
            times=2
        return f'{self.name}'+times*'\t'+f'[{self.id_}]'
# ------------------------------------------------------------------------------
