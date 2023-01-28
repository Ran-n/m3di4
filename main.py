#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:17:25.456829
#+ Editado:	2023/01/28 21:41:56.336636
# ------------------------------------------------------------------------------
import logging
from datetime import datetime

from src.utils import Config
from src.media4 import main
# ------------------------------------------------------------------------------
if __name__ == "__main__":
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

    main()
# ------------------------------------------------------------------------------
