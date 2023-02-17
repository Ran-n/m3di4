#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:45:45.121317
#+ Editado:	2023/02/17 18:23:31.662397
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
    name: str
    media: Optional[Media] = field(default=None)
    media_group: Optional[MediaGroup] = field(default=None)
    media_issue: Optional[MediaIssue] = field(default=None)
    active: Optional[int] = field(default=1)

    def __post_init__(self) -> None:
        # make either media, media_group or media_issue required on object creation
        if not any([self.media, self.media_group, self.media_issue]):
            raise TypeError(f'{self.__class__.__name__}.__init__() missing \
                    1 required positional argument: "media", "media_group" or "media_issue"')
        self.table_name = Config().get_table_name('MediaName')

# ------------------------------------------------------------------------------
