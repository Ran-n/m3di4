#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 18:57:18.314541
#+ Editado:	2023/01/20 17:49:34.349617
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class FileVideo:
    table_name: str = field(init=False, default='Arquivo Vídeo')
    quality: str
    resolution: str
    sample_aspect_ratio: str
    display_aspect_ratio: str
    pixel_format: str
    sample_rate: int
    bit_rate: int
    frame_rate: float
    size: int
    start: float
    duration: float
    name: str
    color: int = field(default=1)
    id_codec: str = field(default=None)
    id_file: str = field(default=None)
    id_language: str = field(default=None)
    #id_: str = field(default=None)
# ------------------------------------------------------------------------------
