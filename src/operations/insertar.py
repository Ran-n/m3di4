#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/06 17:48:55.515052
#+ Editado:	2023/01/08 16:41:07.048441
# ------------------------------------------------------------------------------
from src.operations.info import main
from uteis.imprimir import jprint
from src.db.db import DB
from typing import Union
import pathlib

from src.dtos.Almacen import Almacen
from src.dtos.Arquivo import Arquivo
from src.dtos.ArquivoAdxunto import ArquivoAdxunto
from src.dtos.ArquivoAudio import ArquivoAudio
from src.dtos.ArquivoSubtitulo import ArquivoSubtitulo
from src.dtos.ArquivoVideo import ArquivoVideo
from src.dtos.Media import Media
from src.dtos.MediaAgrupacion import MediaAgrupacion
from src.dtos.MediaFasciculo import MediaFasciculo
from src.dtos.MediaSituacion import MediaSituacion
from src.dtos.MediaTipo import MediaTipo
from src.dtos.MediaWeb import MediaWeb
from src.dtos.NomeCarpeta import NomeCarpeta
from src.dtos.CompartirLugar import CompartirLugar
from src.dtos.Web import Web
from src.dtos.Compartido import Compartido
# ------------------------------------------------------------------------------
# non moi ben que esta info este aqui soamente
MEDIAS_AGRUPABLES = ['serie', 'miniserie']
# ------------------------------------------------------------------------------
def loop_variable(db: DB, variable: str) -> str:
    if variable == 'Tipo':
        posibilidades = db.select(MediaTipo.nome_taboa)
    elif variable == 'Situación':
        posibilidades = db.select(MediaSituacion.nome_taboa)
    elif variable == 'Almacén':
        posibilidades = db.select(Almacen.nome_taboa)
    elif variable == 'Lugar':
        posibilidades = db.select(CompartirLugar.nome_taboa)
    elif variable == 'Web':
        posibilidades = db.select(Web.nome_taboa)

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
    if media.id_tipo in MEDIAS_AGRUPABLES:
        media.id_situacion = loop_variable(db, 'Situación')
    else:
        for ele in db.select(MediaSituacion.nome_taboa):
            if ele.nome == 'Estreada':
                media.id_situacion = ele.id_
                break
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

def get_carpeta(db: DB, fich: str, media: Media) -> NomeCarpeta:
    carpetas = db.select(NomeCarpeta.nome_taboa)
    nome_carpeta = NomeCarpeta(
            nome=pathlib.Path(fich).parent.name,
            id_media=media.id_,
    )

    for carpeta in carpetas:
        if carpeta.nome == nome_carpeta.nome:
            nome_carpeta = carpeta
            break

    return nome_carpeta

def get_arquivo(db: DB, media: Media, info: dict, fich: str) -> tuple[Arquivo, NomeCarpeta]:
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
    )

    arquivo.id_almacen = loop_variable(db, 'Almacén')
    carpeta = get_carpeta(db, fich, media)
    arquivo.id_carpeta = carpeta.id_

    if media.id_tipo in MEDIAS_AGRUPABLES:
        #id_media_fasciculo=
        pass
    else:
        arquivo.id_media = media.id_

    return arquivo, carpeta

def get_video(db: DB, arquivo: Arquivo, info: dict) -> ArquivoVideo:
    calidade = input('* Calidade: ')
    cor = input('* Ten cor? ([s]/n): ').lower()
    if cor == 'n':
        cor = 0
    else:
        cor = 1

    arquivovideo = ArquivoVideo(
            calidade=calidade,
            resolucion=info.get('Resolucion'),
            aspecto_sample=info.get('Ratio aspecto sample'),
            aspecto_display=info.get('Ratio aspecto display'),
            formato_pixel=info.get('Formato de pixel'),
            sample_rate=info.get('Sample Rate'),
            bit_rate=info.get('Bit Rate'),
            fps=info.get('Frame Rate'),
            tamanho=info.get('Tamanho'),
            inicio=info.get('Inicio'),
            duracion=info.get('Duracion'),
            nome=info.get('Nome'),
            cor=cor,
            id_arquivo=arquivo.id_,
    )

    codec = db.get_codec_by_name(info.get('Codec'))
    lingua = db.get_lingua_by_code(info.get('Lingua'))

    if codec:
        arquivovideo.id_codec = codec.id_
    if lingua:
        arquivovideo.id_lingua = lingua.id_

    return arquivovideo

def get_audio(db: DB, arquivo: Arquivo, info: dict) -> ArquivoAudio:
    print(f"\n#{info.get('Posicion')} (Audio), lingua: {info.get('Lingua2')}, nome: {info.get('Nome')}")
    xdefecto = input('* Por defecto? (s/[n]): ').lower()
    if xdefecto == 's':
        xdefecto = 1
    else:
        xdefecto = 0

    forzado = input('* Forzado? (s/[n]): ').lower()
    if forzado == 's':
        forzado = 1
    else:
        forzado = 0

    comentario = input('* Comentario? (s/[n]): ').lower()
    if comentario == 's':
        comentario = 1
    else:
        comentario = 0

    canles = info.get('Canles')
    if not canles:
        canles = info.get('Numero canles')

    arquivoaudio = ArquivoAudio(
            canles=canles,
            sample_rate=info.get('Sample Rate'),
            bit_rate=info.get('Bit Rate'),
            nome=info.get('Nome'),
            tamanho=info.get('Tamanho'),
            inicio=info.get('Inicio'),
            duracion=info.get('Duracion'),
            id_arquivo=arquivo.id_,
            xdefecto=xdefecto,
            forzado=forzado,
            comentario=comentario,
    )

    codec = db.get_codec_by_name(info.get('Codec'))
    lingua = db.get_lingua_by_code(info.get('Lingua'))

    if codec:
        arquivoaudio.id_codec = codec.id_
    if lingua:
        arquivoaudio.id_lingua = lingua.id_

    return arquivoaudio

def get_sub(db: DB, arquivo: Arquivo, info: dict) -> ArquivoSubtitulo:
    print(f"\n#{info.get('Posicion')} (Subtítulo), lingua: {info.get('Lingua2')}, nome: {info.get('Nome')}")
    xdefecto = input('* Por defecto? (s/[n]): ').lower()
    if xdefecto == 's':
        xdefecto = 1
    else:
        xdefecto = 0

    forzado = input('* Forzado? (s/[n]): ').lower()
    if forzado == 's':
        forzado = 1
    else:
        forzado = 0

    texto = input('* De texto? (s/[n]): ').lower()
    if texto == 's':
        texto = 1
    else:
        texto = 0

    arquivosub = ArquivoSubtitulo(
            nome=info.get('Nome'),
            tamanho=info.get('Tamanho'),
            inicio=info.get('Inicio'),
            duracion=info.get('Duracion'),
            id_arquivo=arquivo.id_,
            xdefecto=xdefecto,
            forzado=forzado,
            texto=texto,
    )

    codec = db.get_codec_by_name(info.get('Codec'))
    lingua = db.get_lingua_by_code(info.get('Lingua'))

    if codec:
        arquivosub.id_codec = codec.id_
    if lingua:
        arquivosub.id_lingua = lingua.id_

    return arquivosub

def get_attachment(db: DB, arquivo: Arquivo, info: dict) -> ArquivoAdxunto:
    arquivoadxunto = ArquivoAdxunto(
        nome=info.get('Nome'),
        tamanho=info.get('Tamanho'),
        inicio=info.get('Inicio'),
        duracion=info.get('Duracion'),
        id_arquivo=arquivo.id_,
    )

    codec = db.get_codec_by_name(info.get('Codec'))

    if codec:
        arquivoadxunto.id_codec=codec.id_

    return arquivoadxunto
# ------------------------------------------------------------------------------
def insertar(db: DB):
    print('\n*** INSERTAR ***')

    media = get_media(db)
    print()
    if media.id_tipo in MEDIAS_AGRUPABLES:
        agrupacion = get_agrupacion(db, media)
        print()

    webs = []
    while True:
        link = input('* Ligazón da media (. para finalizar): ')
        if link == '.':
            break
        elif link != '':
            webs.append(MediaWeb(
                ligazon=link,
                id_media=media.id_,
                id_web=loop_variable(db, 'Web'),
            ))

    """
    # media nomes
    names = []
    while True:
        name = input('* Nome alternativo da media (. para finalizar): ')
        if link == '.':
            break
        lang = input('* Idioma no que está este nome: ')
        country = input('* País no que se usou este nome: ')

        names.append()
    """

    print()
    while True:
        fich = input('* Path do ficheiro: ')
        if fich != "" and pathlib.Path(fich).exists():
            break
    info = main(fich)

    arquivo, carpeta = get_arquivo(db, media, info, fich)

    videos = []
    if info.get('videos'):
        for video in info['videos']:
            videos.append(get_video(db, arquivo, video))

    audios = []
    if info.get('audios'):
        for audio in info['audios']:
            audios.append(get_audio(db, arquivo, audio))

    subs = []
    if info.get('subtitulos'):
        for sub in info['subtitulos']:
            subs.append(get_sub(db, arquivo, sub))

    attachments = []
    if info.get('adxuntos'):
        for attachment in info['adxuntos']:
            attachments.append(get_attachment(db, arquivo, attachment))

    print()
    shared = []
    while True:
        link = input('* Ligazón de compartido (. para finalizar): ')
        if link == '.':
            break
        elif link != '':
            shared.append(Compartido(
                ligazon=link,
                id_lugar=loop_variable(db, 'Lugar'),
                id_arquivo=arquivo.id_
            ))

    ## gardar
    # media
    db.insert(media)
    # media nomes
    # media nomes linguas
    # media nomes paises
    # media web
    for web in webs:
        db.insert(web)
    # carpeta
    db.insert(carpeta)

    # arquivo
    db.insert(arquivo)
    # arquivo adxunto
    for attachment in attachments:
        db.insert(attachment)
    # arquivo audio
    for audio in audios:
        db.insert(audio)
    # arquivo subtitulo
    for sub in subs:
        db.insert(sub)
    # arquivo video
    for video in videos:
        db.insert(video)
    # compartido
    for share in shared:
        db.insert(share)

    print('*** INSERTAR ***\n')
# ------------------------------------------------------------------------------
