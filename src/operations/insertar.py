#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/06 17:48:55.515052
#+ Editado:	2023/01/06 18:04:43.191566
# ------------------------------------------------------------------------------
from src.db.db import DB

from src.dtos.Media import Media
from src.dtos.MediaAgrupacion import MediaAgrupacion
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
def get_media(db: DB) -> None:
    media = Media(
            nome=input('* Nome da Media: '),
            ano_ini=validar_numero('Ano Inicio'),
            ano_fin=validar_numero('Ano Fin'),
    )
    if media.ano_fin == '=':
        media.ano_fin = media.ano_ini

    media.id_tipo = loop_variable(db, 'Tipo')
    media.id_situacion = loop_variable(db, 'Situación')

def get_agrupacion(db: DB, media: Media) -> None:
    pass
# ------------------------------------------------------------------------------
def insertar(db: DB):
    print('\n*** INSERTAR ***')
    media = get_media(db)
    print()
    agrupacion = get_agrupacion(db, media)
    print('*** INSERTAR ***\n')
# ------------------------------------------------------------------------------
