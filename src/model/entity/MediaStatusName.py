#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/29 23:17:57.682598
#+ Editado:	2023/01/29 23:34:39.768878
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import MediaStatus
# ------------------------------------------------------------------------------
@dataclass
class MediaStatusName:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('MediaStatusName'))
    name: str
    media_status: MediaStatus
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
