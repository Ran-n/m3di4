#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:06:39.547649
#+ Editado:	2023/01/28 00:31:09.206988
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import Media, Web
# ------------------------------------------------------------------------------
@dataclass
class MediaWeb:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('MediaWeb'))
    media: Media
    web: Web
    link: str
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
