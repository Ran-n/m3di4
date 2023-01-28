#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:41:57.231414
#+ Editado:	2023/01/16 22:36:12.054418
# ------------------------------------------------------------------------------
#* Concrete Strategy (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.view.iview import iView
# ------------------------------------------------------------------------------
from src.model.entity import Media
# ------------------------------------------------------------------------------
class Terminal(iView):
    def __init__(self) -> None:
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

