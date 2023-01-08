#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/06 17:48:47.889120
#+ Editado:	2023/01/08 01:08:22.889008
# ------------------------------------------------------------------------------
import sys

from src.db.db import DB
from src.uteis import print_fin
# ------------------------------------------------------------------------------
def sair(db: DB):
    db.desconectar(commit=True)
    print_fin()
    sys.exit()
# ------------------------------------------------------------------------------
