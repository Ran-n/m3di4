#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:53:33.927294
#+ Editado:	2023/03/16 21:52:03.505303
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional
from blake3 import blake3

from src.utils import Config
from src.model.entity import BaseEntity, Warehouse, Folder, Media, Issue
from src.model.entity import Extension, Encoder, AppVersion
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
    app_version: Optional[AppVersion] = field(default=None)
    encoder: Optional[Encoder] = field(default=None)
    original_name: Optional[str] = field(default=None)
    active: Optional[int] = field(default=1)

    def __post_init__(self) -> None:
        # make either media or issue required on object creation
        if not any([self.media, self.issue]):
            raise TypeError(f'{self.__class__.__name__}.__init__() missing \
                    1 required positional argument: "media" or "issue"')
        self.__calculate_hash()

    def __calculate_hash(self) -> None:
        self.hash_ = blake3(
                open(self.folder.path+'/'+self.name+'.'+self.extension.name, 'rb').read()
                ).hexdigest()
# ------------------------------------------------------------------------------
