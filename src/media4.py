#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:17:25.456829
#+ Editado:	2023/01/29 17:37:39.290277
# ------------------------------------------------------------------------------
import logging
from datetime import datetime
import gettext

from src.utils import Config

from src.model import Model, Sqlite
from src.view import View, Terminal, GUI
from src.controller import Controller
# ------------------------------------------------------------------------------
def main():
    # logging setup
    logging.basicConfig(
            filename = f"{Config().log_folder}/{datetime.now().strftime('%Y-%m-%d')}.log",
            encoding = "utf-8",
            format = "%(asctime)s - %(levelname)s - [%(filename)s:%(funcName)s:%(lineno)s]: %(message)s",
            level = logging.DEBUG
    )

    logging.info("""
                        _ _       _  _
     _ __ ___   ___  __| (_) __ _| || |
    | '_ ` _ \ / _ \/ _` | |/ _` | || |_
    | | | | | |  __| (_| | | (_| |__   _|
    |_| |_| |_|\___|\__,_|_|\__,_|  |_|
    """)

    lang = gettext.translation('media4', localedir=Config().i18n_folder, languages=[Config().language])
    lang.install()
    _ = lang.gettext

    model = Model(strategy=Sqlite(Config().file_content['db_file_location']))
    #view = View(strategy=GUI(), model=model)
    view = View(strategy=Terminal(), model=model)
    controller = Controller(model=model, view=view)

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
# ------------------------------------------------------------------------------
