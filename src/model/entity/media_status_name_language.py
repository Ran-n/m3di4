#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/29 23:33:56.446838
#+ Editado:	2023/02/16 23:35:37.124060
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, MediaStatusName, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaStatusNameLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('MediaStatusNameLanguage'))
    media_status_name: MediaStatusName
    language: Language
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
