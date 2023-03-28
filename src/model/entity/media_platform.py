#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:06:39.547649
#+ Editado:	2023/03/28 19:32:02.717343
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Media, Platform
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaPlatform(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('MediaPlatform'))
    media: Media
    platform: Platform
    link: str
    in_platform_id: Optional[str] = field(default=None)
    active: Optional[str] = field(default=1)

    def __post_init__(self) -> None
        if self.link is not None and not self.link.endswith('/'):
            self.link += '/'
# ------------------------------------------------------------------------------
