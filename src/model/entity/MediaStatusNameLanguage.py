#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/29 23:33:56.446838
#+ Editado:	2023/02/04 21:29:06.096984
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import MediaStatusName, Language
# ------------------------------------------------------------------------------
@dataclass
class MediaStatusNameLanguage:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('MediaStatusNameLanguage'))
    media_status_name: MediaStatusName
    language: Language
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
