#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/06 17:48:47.889120
#+ Editado:	2023/01/14 19:58:06.308363
# ------------------------------------------------------------------------------
import sys

from src.model.imodel import iModel
from src.view.iview import iView
# ------------------------------------------------------------------------------
def sair(model: iModel, view: iView) -> None:
    model.disconnect_db(commit=True)
    view.exit()
    sys.exit()
# ------------------------------------------------------------------------------
