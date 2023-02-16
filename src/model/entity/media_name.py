#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:45:45.121317
#+ Editado:	2023/02/16 23:35:24.442657
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Media, MediaGroup, MediaIssue
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaName(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('MediaName'))
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
            raise TypeError(f'{self.__class__.__name__}.__init__() missing \
                    1 required positional argument: "media", "media_group" or "media_issue"')

# ------------------------------------------------------------------------------
