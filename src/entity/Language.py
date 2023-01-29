#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:01:51.038236
#+ Editado:	2023/01/24 22:10:33.170135
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config, strip_accents
# ------------------------------------------------------------------------------
@dataclass
class Language:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('Language'))
    name: str
    desc: Optional[str] = field(default=None)
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)

    """
    # xFCR
    def __repr__(self) -> str:
        return f'{self.name}\t[{self.id_}]'
    """

    def __gt__(self, other) -> bool:
        return strip_accents(self.nome) > strip_accents(other.nome)

    def __lt__(self, other) -> bool:
        return strip_accents(self.nome) < strip_accents(other.nome)
# ------------------------------------------------------------------------------
