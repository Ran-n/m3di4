#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:41:48.278353
#+ Editado:	2023/01/28 00:30:47.788940
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import Media, MediaGroup
# ------------------------------------------------------------------------------
@dataclass
class MediaIssue:
    table_name: str = field(init=False, default='MediaIssue')
    position: int
    id_media: Media
    id_media_group: MediaGroup
    name: Optional[str] = field(default = None)
    date: Optional[str] = field(default = None)
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
