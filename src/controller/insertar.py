#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/06 17:48:55.515052
#+ Editado:	2023/01/14 18:35:34.470729
# ------------------------------------------------------------------------------
from typing import Union, List
import pathlib

from uteis.imprimir import jprint

from src.controller.info import main
from src.model.model import Model

from src.dtos.Almacen import Almacen
from src.dtos.Arquivo import Arquivo
from src.dtos.ArquivoAdxunto import ArquivoAdxunto
from src.dtos.ArquivoAudio import ArquivoAudio
from src.dtos.ArquivoSubtitulo import ArquivoSubtitulo
from src.dtos.ArquivoVideo import ArquivoVideo
from src.dtos.Compartido import Compartido
from src.dtos.CompartirLugar import CompartirLugar
from src.dtos.Lingua import Lingua
from src.dtos.Media import Media
from src.dtos.MediaAgrupacion import MediaAgrupacion
from src.dtos.MediaFasciculo import MediaFasciculo
from src.dtos.MediaNomes import MediaNomes
from src.dtos.MediaNomesLinguas import MediaNomesLinguas
from src.dtos.MediaNomesPaises import MediaNomesPaises
from src.dtos.MediaSituacion import MediaSituacion
from src.dtos.MediaTipo import MediaTipo
from src.dtos.MediaWeb import MediaWeb
from src.dtos.NomeCarpeta import NomeCarpeta
from src.dtos.Pais import Pais
from src.dtos.Web import Web
# ------------------------------------------------------------------------------
def loop_variable(model: Model, variable: str, msg: str = None) -> str:
    if variable == 'Tipo':
        posibilidades = model.select(MediaTipo.nome_taboa)
    elif variable == 'Situación':
        posibilidades = model.select(MediaSituacion.nome_taboa)
    elif variable == 'Almacén':
        posibilidades = model.select(Almacen.nome_taboa)
    elif variable == 'Lugar':
        posibilidades = model.select(CompartirLugar.nome_taboa)
    elif variable == 'Web':
        posibilidades = model.select(Web.nome_taboa)
    elif variable == 'Lingua':
        posibilidades = model.select(Lingua.nome_taboa, alfabetic=True)
    elif variable == 'Pais':
        posibilidades = model.select(Pais.nome_taboa)

    posibilidades_ids = []
    for ele in posibilidades:
        posibilidades_ids.append(ele.id_)

    while True:
        if not msg:
            msg = variable
        resul = input(f'* {msg}: ')
        if resul == '?':
            print()
            for ele in posibilidades:
                print(f'\t {ele}')
            print()
        elif resul in posibilidades_ids:
            break
    return resul

def loop_variable_until(model: Model, variable: str, msg: str = None) -> List[str]:
    variables = []
    while True:
        variables.append(loop_variable(model, variable, msg))
        continue_ = input('* Máis? (s/[n]): ').lower()
        if continue_ != 's':
            break
    return variables

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
def get_media(model: Model, medias_agrupables: List[int]) -> Media:
    print('> Media')
    media = Media(
            nome=input('* Nome da Media: '),
            ano_ini=validar_numero('Ano Inicio'),
            ano_fin=validar_numero('Ano Fin'),
    )
    if media.ano_fin == '=':
        media.ano_fin = media.ano_ini

    media.id_tipo = loop_variable(model, 'Tipo')
    if media.id_tipo in medias_agrupables:
        media.id_situacion = loop_variable(model, 'Situación')
    else:
        situacion = model.get_situacion_by_name('Estreada')
        if situacion:
            media.id_situacion = situacion.id_
        """
        for ele in model.select(MediaSituacion.nome_taboa):
            if ele.nome == 'Estreada':
                media.id_situacion = ele.id_
                break
        """
    return media

def get_agrupacion(model: Model, media: Media) -> MediaAgrupacion:
    print('> Agrupación')
    return MediaAgrupacion(
            nome=input('* Nome da Agrupación: '),
            numero=validar_numero('Número'),
            ano_ini=validar_numero('Ano Inicio'),
            ano_fin=validar_numero('Ano Fin'),
            id_media=media.id_,
    )

def get_carpeta(model: Model, fich: str, media: Media) -> NomeCarpeta:
    nome = pathlib.Path(fich).parent.name
    nome_carpeta = model.get_nomecarpeta_by_name(nome)
    if not nome_carpeta:
        nome_carpeta = NomeCarpeta(nome=nome)
    return nome_carpeta

def get_arquivo(model: Model, media: Media, info: dict, fich: str, medias_agrupables: List[int]) -> tuple[Arquivo, NomeCarpeta]:
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

    arquivo.id_almacen = loop_variable(model, 'Almacén')
    carpeta = get_carpeta(model, fich, media)
    arquivo.id_carpeta = carpeta.id_

    if media.id_tipo in medias_agrupables:
        #id_media_fasciculo=
        pass
    else:
        arquivo.id_media = media.id_

    return arquivo, carpeta

def get_video(model: Model, arquivo: Arquivo, info: dict) -> ArquivoVideo:
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

    codec = model.get_codec_by_name(info.get('Codec'))
    lingua = model.get_lingua_by_code(info.get('Lingua'))

    if codec:
        arquivovideo.id_codec = codec.id_
    if lingua:
        arquivovideo.id_lingua = lingua.id_

    return arquivovideo

def get_audio(model: Model, arquivo: Arquivo, info: dict) -> ArquivoAudio:
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

    codec = model.get_codec_by_name(info.get('Codec'))
    lingua = model.get_lingua_by_code(info.get('Lingua'))

    if codec:
        arquivoaudio.id_codec = codec.id_
    if lingua:
        arquivoaudio.id_lingua = lingua.id_

    return arquivoaudio

def get_sub(model: Model, arquivo: Arquivo, info: dict) -> ArquivoSubtitulo:
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

    codec = model.get_codec_by_name(info.get('Codec'))
    lingua = model.get_lingua_by_code(info.get('Lingua'))

    if codec:
        arquivosub.id_codec = codec.id_
    if lingua:
        arquivosub.id_lingua = lingua.id_

    return arquivosub

def get_attachment(model: Model, arquivo: Arquivo, info: dict) -> ArquivoAdxunto:
    arquivoadxunto = ArquivoAdxunto(
        nome=info.get('Nome'),
        tamanho=info.get('Tamanho'),
        inicio=info.get('Inicio'),
        duracion=info.get('Duracion'),
        id_arquivo=arquivo.id_,
    )

    codec = model.get_codec_by_name(info.get('Codec'))

    if codec:
        arquivoadxunto.id_codec=codec.id_

    return arquivoadxunto
# ------------------------------------------------------------------------------
def insertar(model: Model) -> None:
    print('\n*** INSERTAR ***')

    medias_agrupables = model.get_mediatipo_agrupables(id_only=True)

    media = get_media(model, medias_agrupables)
    print()
    if media.id_tipo in medias_agrupables:
        agrupacion = get_agrupacion(model, media)
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
                id_web=loop_variable(model, 'Web'),
            ))

    print()

    # media nomes
    names = []
    langs = []
    countries = []

    media_nome = MediaNomes(
            nome=media.nome,
            id_media=media.id_,
    )
    while True:
        names.append(media_nome)
        for id_lang in loop_variable_until(model=model, variable='Lingua', msg='Linguas do nome da Media'):
            langs.append(MediaNomesLinguas(
                id_media_nomes=media_nome.id_,
                id_lingua=id_lang,
            ))

        for id_country in loop_variable_until(model=model, variable='Pais', msg='Países do nome da Media'):
            countries.append(MediaNomesPaises(
                id_media_nomes=media_nome.id_,
                id_pais=id_country,
            ))

        print()

        media_nome = MediaNomes(
                nome=input('* Nome alternativo da media (. para finalizar): '),
                id_media=media.id_,
        )
        if media_nome.nome == '.':
            break

    print()

    while True:
        fich = input('* Path do ficheiro: ')
        if fich != "" and pathlib.Path(fich).exists():
            break
    info = main(fich)

    arquivo, carpeta = get_arquivo(model, media, info, fich, medias_agrupables)

    videos = []
    if info.get('videos'):
        for video in info['videos']:
            videos.append(get_video(model, arquivo, video))

    audios = []
    if info.get('audios'):
        for audio in info['audios']:
            audios.append(get_audio(model, arquivo, audio))

    subs = []
    if info.get('subtitulos'):
        for sub in info['subtitulos']:
            subs.append(get_sub(model, arquivo, sub))

    attachments = []
    if info.get('adxuntos'):
        for attachment in info['adxuntos']:
            attachments.append(get_attachment(model, arquivo, attachment))

    print()
    shared = []
    while True:
        link = input('* Ligazón de compartido (. para finalizar): ')
        if link == '.':
            break
        elif link != '':
            shared.append(Compartido(
                ligazon=link,
                id_lugar=loop_variable(model, 'Lugar'),
                id_arquivo=arquivo.id_
            ))

    ## gardar
    # media
    model.insert(media)

    # media nomes
    for name in names:
        model.insert(name)
    # media nomes linguas
    for lang in langs:
        model.insert(lang)
    # media nomes paises
    for country in countries:
        model.insert(country)

    # media web
    for web in webs:
        model.insert(web)
    # carpeta
    model.insert(carpeta)

    # arquivo
    model.insert(arquivo)
    # arquivo adxunto
    for attachment in attachments:
        model.insert(attachment)
    # arquivo audio
    for audio in audios:
        model.insert(audio)
    # arquivo subtitulo
    for sub in subs:
        model.insert(sub)
    # arquivo video
    for video in videos:
        model.insert(video)
    # compartido
    for share in shared:
        model.insert(share)

    model.save_db()

    print('*** INSERTAR ***\n')
# ------------------------------------------------------------------------------
