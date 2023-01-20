#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 19:48:30.957751
#+ Editado:	2023/01/20 17:44:31.728629
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class FileAttachment:
    table_name: str = field(init=False, default='Arquivo Adxunto')
    name: str
    size: int
    start: float
    duration: float
    id_file: str = field(default=None)
    id_codec: str = field(default='ttf')
    #id_: int = field(init=False, default=None)
# ------------------------------------------------------------------------------
