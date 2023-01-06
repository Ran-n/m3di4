#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/06 17:48:55.515052
#+ Editado:	2023/01/06 23:33:21.250873
# ------------------------------------------------------------------------------
from src.operations.info import main
from uteis.imprimir import jprint

from src.db.db import DB

from src.dtos.Media import Media
from src.dtos.MediaAgrupacion import MediaAgrupacion
# ------------------------------------------------------------------------------
# non moi ben que esta info este aqui soamente
MEDIAS_AGRUPABLES = ['serie', 'miniserie']
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
def get_media(db: DB) -> Media:
    print('> Media')
    media = Media(
            nome=input('* Nome da Media: '),
            ano_ini=validar_numero('Ano Inicio'),
            ano_fin=validar_numero('Ano Fin'),
    )
    if media.ano_fin == '=':
        media.ano_fin = media.ano_ini

    media.id_tipo = loop_variable(db, 'Tipo')
    media.id_situacion = loop_variable(db, 'Situación')

    return media

def get_agrupacion(db: DB, media: Media) -> MediaAgrupacion:
    print('> Agrupación')
    return MediaAgrupacion(
            nome=input('* Nome da Agrupación: '),
            numero=validar_numero('Número'),
            ano_ini=validar_numero('Ano Inicio'),
            ano_fin=validar_numero('Ano Fin'),
            id_media=media.id_,
    )
# ------------------------------------------------------------------------------
def insertar(db: DB):
    print('\n*** INSERTAR ***')

    info = main(input('* Path do ficheiro: '))
    jprint(info)

    media = get_media(db)
    print()
    if media.id_tipo in MEDIAS_AGRUPABLES:
        agrupacion = get_agrupacion(db, media)
        print()



    print('*** INSERTAR ***\n')
# ------------------------------------------------------------------------------
