#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 19:51:12.375406
#+ Editado:	2023/01/20 17:46:41.532058
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class FileSubtitle:
    table_name: str = field(init=False, default='Arquivo Subtítulo')
    name: str
    size: int
    start: float
    duration: float
    id_file: str = field(default=None)
    id_codec: str = field(default=None)
    id_language: str = field(default=None)
    by_default: int = field(default=0)
    forzed: int = field(default=0)
    text: int = field(default=0)
    #id_: int = field(default=None)
# ------------------------------------------------------------------------------
