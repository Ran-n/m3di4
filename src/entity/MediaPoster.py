#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/23 18:39:20.569506
#+ Editado:	2023/01/28 00:10:19.167913
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import create_key, Config
from src.entity import Media, Extension
# ------------------------------------------------------------------------------
@dataclass
class MediaPoster:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('MediaPoster'))
    media: Media
    extension: Extension
    name: Optional[str] = field(default_factory=create_key)
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
