#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:41:57.231414
#+ Editado:	2023/01/29 20:19:19.773340
# ------------------------------------------------------------------------------
#* Concrete Strategy (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.view import iView
# ------------------------------------------------------------------------------
import logging
from src.model.entity import Media
# ------------------------------------------------------------------------------
class Terminal(iView):
    def __init__(self) -> None:
        logging.info(_('Starting Terminal view'))

        print('----------------------------------------')
        print(_('Media4 Manager'))
        print('----------------------------------------')

    def menu(self, options: dict) -> int:
        print()
        print(_('*** MENU ***'))

        for key, value in zip(options.keys(), options.values()):
            print(f'{key}. {value[0]}')

        while True:
            option = input(_('Pick: '))
            if option in options:
                break

        print(_('*** MENU ***'))
        print()

        return option

    def exit(self) -> None:
        print('----------------------------------------')

    def get_media(self) -> Media:
        pass
# ------------------------------------------------------------------------------

