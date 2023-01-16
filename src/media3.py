#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:17:25.456829
#+ Editado:	2023/01/16 23:40:44.369616
# ------------------------------------------------------------------------------
from uteis.ficheiro import cargarJson

from src.model.model import Model
from src.model.sqlite import Sqlite
from src.controller.controller import Controller
from src.view.view import View
from src.view.terminal import Terminal
from src.view.gui import GUI
# ------------------------------------------------------------------------------
def main():
    cnf = cargarJson('.cnf')

    model = Model(strategy=Sqlite(cnf['db']))
    view = View(strategy=Terminal(), model=model)
    controller = Controller(model=model, view=view)

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
# ------------------------------------------------------------------------------
