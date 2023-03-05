#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/03/03 18:55:32.956618
#+ Editado:	2023/03/03 20:39:09.767554
# ------------------------------------------------------------------------------
import re

from src.model.entity import AppVersion, App
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
def get_app_version(writting_app: str) -> AppVersion:
    """
    """
    pattern = r"^(\w+)\s+v([\d\.]+)\s+\('([\w\s]+)'\)\s+(\d+)(\D*)$"
    match = re.match(pattern, writting_app)

    return AppVersion(app=App(name=match.group(1)), number=match.group(2),
                      name=match.group(3), num_bit_processor=match.group(4))
# ------------------------------------------------------------------------------
