#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:53:33.927294
#+ Editado:	2023/02/04 21:28:33.321843
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import Warehouse, FolderName, Media, MediaIssue, Extension, Encoder, AppVersion
# ------------------------------------------------------------------------------
@dataclass
class File:
    """Entity Object"""
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
    encoder: Optional[Encoder] = field(default=None)
    app_version: Optional[AppVersion] = field(default=None)
    media: Optional[Media] = field(default=None)
    media_issue: Optional[MediaIssue] = field(default=None)
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)

    # make either media or media_issue required on object creation
    def __post_init__(self) -> None:
        if not any([self.media, self.media_issue]):
            raise TypeError(f'{self.__class__.__name__}.__init__() missing 1 required positional argument: "media" or "media_issue"')

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
