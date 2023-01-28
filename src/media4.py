#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:17:25.456829
#+ Editado:	2023/01/28 01:31:28.543046
# ------------------------------------------------------------------------------
from src.utils import Config

from src.model import Model, Sqlite
from src.view import View, Terminal, GUI
from src.controller import Controller
# ------------------------------------------------------------------------------
def main():

    model = Model(strategy=Sqlite(Config().file_content['db_file_location']))
    #view = View(strategy=GUI(), model=model)
    view = View(strategy=Terminal(), model=model)
    controller = Controller(model=model, view=view)

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
# ------------------------------------------------------------------------------
