#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/23 18:39:20.569506
#+ Editado:	2023/04/05 17:01:08.903152
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config, file_hash
from src.model.entity import BaseEntity, Media, Group, Issue, Extension
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Poster(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Poster'))
    extension: Extension
    name: str
    hash_: Optional[str] = field(default=None)
    media: Optional[Media] = field(default=None)
    group: Optional[Group] = field(default=None)
    issue: Optional[Issue] = field(default=None)

    def __post_init__(self) -> None:
        # make either media, group or issue required on object creation
        if not any([self.media, self.group, self.issue]):
            raise TypeError(f'{self.__class__.__name__}.__init__() missing \
                    1 required positional argument: "media", "group" or "issue"')

        if self.hash_ is None:
            self.hash_ = file_hash(
                    Config().poster_folder/f'{self.name}.{self.extension.name}'
            )
# ------------------------------------------------------------------------------
