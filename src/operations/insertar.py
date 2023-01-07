#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/06 17:48:55.515052
#+ Editado:	2023/01/07 01:48:18.886033
# ------------------------------------------------------------------------------
from src.operations.info import main
from uteis.imprimir import jprint
from src.db.db import DB
from typing import Union
import pathlib

from src.dtos.Media import Media
from src.dtos.MediaAgrupacion import MediaAgrupacion
from src.dtos.MediaFasciculo import MediaFasciculo
from src.dtos.Arquivo import Arquivo
from src.dtos.Almacen import Almacen
from src.dtos.NomeCarpeta import NomeCarpeta
# ------------------------------------------------------------------------------
# non moi ben que esta info este aqui soamente
MEDIAS_AGRUPABLES = ['serie', 'miniserie']
# ------------------------------------------------------------------------------
def loop_variable(db: DB, variable: str) -> str:
    if variable == 'Tipo':
        posibilidades = db.select_tipos()
    elif variable == 'Situación':
        posibilidades = db.select_situacions()
    elif variable == 'Almacén':
        posibilidades = db.select_almacens()

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

def get_x_info(info: dict, key: str) -> Union[None, float, int, str]:
    try:
        x = info[key]
    except KeyError:
        x = None
    return x
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

def get_carpeta(db: DB, fich: str) -> NomeCarpeta:
    carpetas = db.select_carpetas()
    nome_carpeta = NomeCarpeta(nome=pathlib.Path(fich).parent.name)

    for carpeta in carpetas:
        if carpeta.nome == nome_carpeta.nome:
            nome_carpeta = carpeta
            break

    return nome_carpeta

def get_arquivo(db: DB, media: Media, info: dict, fich: str) -> Arquivo:

    mudo = input('* É mudo? (s/[n]): ').lower()
    if mudo == 's':
        mudo = 1
    else:
        mudo = 0

    cor = input('* Ten cor? ([s]/n): ').lower()
    if cor == 'n':
        cor = 0
    else:
        cor = 1

    nome = get_x_info(info, 'Nome ficheiro')
    extension = get_x_info(info, 'Extension')
    tamanho = get_x_info(info, 'Tamanho')
    duracion = get_x_info(info, 'Duracion')
    bit_rate = get_x_info(info, 'Bit Rate')
    titulo = get_x_info(info, 'Titulo')
    data_creacion = get_x_info(info, 'Data creacion')

    arquivo = Arquivo(
            nome=nome,
            extension=extension,
            tamanho=tamanho,
            duracion=duracion,
            bit_rate=bit_rate,
            titulo=titulo,
            data_creacion=data_creacion,
            mudo=mudo,
            cor=cor,
    )

    arquivo.id_almacen = loop_variable(db, 'Almacén')
    carpeta = get_carpeta(db, fich)
    arquivo.id_carpeta = carpeta.id_

    if media.id_tipo in MEDIAS_AGRUPABLES:
        #id_media_fasciculo=
        pass
    else:
        arquivo.id_media = media.id_

    return arquivo, carpeta

# ------------------------------------------------------------------------------
def insertar(db: DB):
    print('\n*** INSERTAR ***')

    media = get_media(db)
    print()
    if media.id_tipo in MEDIAS_AGRUPABLES:
        agrupacion = get_agrupacion(db, media)
        print()

    fich = input('* Path do ficheiro: ')
    info = main(fich)

    arquivo, carpeta = get_arquivo(db, media, info, fich)

    print('*** INSERTAR ***\n')
# ------------------------------------------------------------------------------
