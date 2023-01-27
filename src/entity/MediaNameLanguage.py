#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:58:36.138946
#+ Editado:	2023/01/27 20:25:19.190523
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.entity import MediaName, Language
# ------------------------------------------------------------------------------
@dataclass
class MediaNameLanguage:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('MediaNameLanguage'))
    media_name: MediaName
    language: Language
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
