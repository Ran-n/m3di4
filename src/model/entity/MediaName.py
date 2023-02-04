#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:45:45.121317
#+ Editado:	2023/02/04 21:28:53.806216
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import Media, MediaGroup, MediaIssue
# ------------------------------------------------------------------------------
@dataclass
class MediaName:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('MediaName'))
    name: str
    media: Optional[Media] = field(default=None)
    media_group: Optional[MediaGroup] = field(default=None)
    media_issue: Optional[MediaIssue] = field(default=None)
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)

    # make either media, media_group or media_issue required on object creation
    def __post_init__(self) -> None:
        if not any([self.media, self.media_group, self.media_issue]):
            raise TypeError(f'{self.__class__.__name__}.__init__() missing 1 required positional argument: "media", "media_group" or "media_issue"')

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)

# ------------------------------------------------------------------------------
