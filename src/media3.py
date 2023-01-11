#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:17:25.456829
#+ Editado:	2023/01/11 22:58:01.593798
# ------------------------------------------------------------------------------
from uteis.ficheiro import cargarJson

from src.model.model import Model
from src.model.sqlite import Sqlite
from src.controller.controller import Controller
from src.view.view import View
from src.view.terminal import Terminal

from src.uteis import print_fin

from src.dtos.Media import Media
from src.dtos.MediaAgrupacion import MediaAgrupacion
# ------------------------------------------------------------------------------
def opcions_menu(opcions: dict) -> int:
    print('\n*** MENÚ ***')

    for chave, valor in zip(opcions.keys(), opcions.values()):
        print(f'{chave}. {valor[0]}')

    while True:
        opcion = input('Escolla: ')
        if opcion in opcions:
            break
    print('*** MENÚ ***\n')
    return opcion

def menu(model: Model, controller: Controller):
    opcions = {
            '0': ['Sair', controller.sair],
            '1': ['Insertar', controller.insertar],
    }

    opcions[opcions_menu(opcions)][1](model)
# ------------------------------------------------------------------------------
def main():
    cnf = cargarJson('.cnf')

    model = Model(Sqlite(cnf['db']))
    view = View(Terminal())
    controller = Controller()

    while True:
        menu(model, controller)

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
# ------------------------------------------------------------------------------
