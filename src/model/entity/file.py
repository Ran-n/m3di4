#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:53:33.927294
#+ Editado:	2023/03/30 22:12:27.202999
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
import os
from pathlib import Path
from typing import Optional

from src.utils import Config, file_hash
from src.model.entity import BaseEntity, Warehouse, Folder, Media, Issue
from src.model.entity import Extension, Encoder, Version
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class File(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('File'))
    name: str
    extension: Extension
    warehouse: Warehouse
    folder: Folder
    hash_: Optional[str] = field(default=None)
    media: Optional[Media] = field(default=None)
    issue: Optional[Issue] = field(default=None)
    title: Optional[str] = field(default=None)
    nb_streams: Optional[int] = field(default=None)
    nb_programs: Optional[int] = field(default=None)
    start: Optional[float] = field(default=None)
    duration: Optional[float] = field(default=None)
    size: Optional[int] = field(default=None)
    bit_rate: Optional[int] = field(default=None)
    probe_score: Optional[int] = field(default=None)
    creation_ts: Optional[str] = field(default=None)
    version: Optional[Version] = field(default=None)
    encoder: Optional[Encoder] = field(default=None)
    original_name: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)

    def __post_init__(self) -> None:
        # make either media or issue required on object creation
        if not any([self.media, self.issue]):
            raise TypeError(f'{self.__class__.__name__}.__init__() missing \
                    1 required positional argument: "media" or "issue"')

        # xFCR change path in folder to Path
        if self.hash_ is None:
            self.hash_ = file_hash(
                    Path(self.folder.path)/f'{self.name}.{self.extension.name}'
            )
# ------------------------------------------------------------------------------
