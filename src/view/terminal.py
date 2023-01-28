#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:41:57.231414
#+ Editado:	2023/01/28 22:16:15.412456
# ------------------------------------------------------------------------------
#* Concrete Strategy (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.view.iview import iView
# ------------------------------------------------------------------------------
import logging
from src.model.entity import Media
# ------------------------------------------------------------------------------
class Terminal(iView):
    def __init__(self) -> None:
        logging.info('Starting Terminal view')

        print('----------------------------------------')
        print('Media3 Manager')
        print('----------------------------------------')

    def menu(self, options: dict) -> int:
        print('\n*** MENÚ ***')

        for key, value in zip(options.keys(), options.values()):
            print(f'{key}. {value[0]}')

        while True:
            option = input('Escolla: ')
            if option in options:
                break

        print('*** MENÚ ***\n')

        return option

    def exit(self) -> None:
        print('----------------------------------------')

    def get_media(self) -> Media:
        pass
# ------------------------------------------------------------------------------

