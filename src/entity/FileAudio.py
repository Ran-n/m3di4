#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 19:51:12.375406
#+ Editado:	2023/01/20 17:45:48.635041
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class FileAudio:
    table_name: str = field(init=False, default='Arquivo Audio')
    channels: float
    sample_rate: int
    bit_rate: int
    name: str
    size: int
    start: float
    duration: float
    id_file: str = field(default=None)
    id_codec: str = field(default='eac3')
    id_language: str = field(default=None)
    by_default: int = field(default=0)
    forzed: int = field(default=0)
    commentary: int = field(default=0)
    #id_: int = field(init=False, default=None)
# ------------------------------------------------------------------------------
