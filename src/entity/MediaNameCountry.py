#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:58:42.990911
#+ Editado:	2023/01/27 20:27:55.363703
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.entity import MediaName, Country
# ------------------------------------------------------------------------------
@dataclass
class MediaNameCountry:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('MediaNameCountry'))
    media_name: MediaName
    country: Country
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
