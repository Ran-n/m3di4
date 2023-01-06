#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:17:25.456829
#+ Editado:	2023/01/06 01:26:41.984745
# ------------------------------------------------------------------------------
from src.db.db import DB
from src.db.sqlite import Sqlite

from src.dtos.Media import Media
# ------------------------------------------------------------------------------
def print_inicio():
    print('----------------------------------------')
    print('Media3 Manager')
    print('----------------------------------------')

def print_fin():
    print('----------------------------------------')
# ------------------------------------------------------------------------------
def loop_variable(db: DB, variable: str) -> str:
    if variable == 'Tipo':
        posibilidades = db.select_tipos()
    elif variable == 'Situación':
        posibilidades = db.select_situacions()

    posibilidades_ids = []
    for ele in posibilidades:
        posibilidades_ids.append(ele.id_)

    while True:
        resul = input(f'* {variable}: ')
        if resul == '?':
            print()
            for ele in posibilidades:
                print(f'\t {ele}')
            print()
        elif resul in posibilidades_ids:
            break
    return resul

def validar_numero(variable: str) -> str:
    while True:
        numero = input(f'* {variable}: ')
        if numero.isdigit() or (variable == 'Ano Fin' and numero == '='):
            break
    return numero

# ------------------------------------------------------------------------------
def main():
    db = DB(Sqlite('./media/db/Media32.db'))
    #print(db.select('a'))

    print_inicio()

    media = Media(
            input('* Nome da Media: '),
            validar_numero('Ano Inicio'),
            validar_numero('Ano Fin')
    )

    if media.ano_fin == '=':
        media.ano_fin = media.ano_ini

    tipo = loop_variable(db, 'Tipo')
    situacion = loop_variable(db, 'Situación')

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
# ------------------------------------------------------------------------------
