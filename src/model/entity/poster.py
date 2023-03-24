#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/23 18:39:20.569506
#+ Editado:	2023/03/24 19:11:47.086003
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config, calculate_hash
from src.model.entity import BaseEntity, Media, Group, Issue, Extension
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Poster(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Poster'))
    extension: Extension
    name: Optional[str] = field(init=False, default_factory=None)
    media: Optional[Media] = field(default_factory=None)
    group: Optional[Group] = field(default_factory=None)
    issue: Optional[Issue] = field(default_factory=None)

    def __post_init__(self) -> None:
        # make either media, group or issue required on object creation
        if not any([self.media, self.group, self.issue]):
            raise TypeError(f'{self.__class__.__name__}.__init__() missing \
                    1 required positional argument: "media", "group" or "issue"')
        if self.name is None:
            self.name = calculate_hash(f'{self.name}.{self.extension.name}')
# ------------------------------------------------------------------------------
