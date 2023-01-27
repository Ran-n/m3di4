#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:53:33.927294
#+ Editado:	2023/01/27 18:42:55.803046
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import Warehouse, FolderName, Media, MediaIssue, Extension, Encoder
# ------------------------------------------------------------------------------
@dataclass
class File:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('File'))
    name: str
    extension: Extension
    warehouse: Warehouse
    folder: FolderName
    title: str
    nb_streams: int
    nb_programs: int
    start: float
    duration: float
    size: int
    bit_rate: int
    probe_score: int
    creation_ts: str
    writing_app: str
    encoder: Encoder
    media: Optional[Media] = field(default=None)
    media_issue: Optional[MediaIssue] = field(default=None)
    id_: Optional[int] = field(default=None)

    # make either media or media_issue required on object creation
    def __post_init__(self) -> None:
        if not any([self.media, self.media_issue]):
            raise TypeError(f'{self.__class__.__name__}.__init__() missing 1 required positional argument: "media" or "media_issue"')

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
