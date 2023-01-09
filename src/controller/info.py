#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/12/29 01:43:44.566474
#+ Editado:	2023/01/09 23:34:00.255312
# ------------------------------------------------------------------------------
import sys
import ffmpeg
import pathlib
from datetime import datetime
from dateutil import parser
from typing import List, Union

from uteis.imprimir import jprint
# ------------------------------------------------------------------------------
def formato_lingua(lingua: Union[List[str], str]) -> str:
    if (type(lingua) == str): return lingua
    return f'{lingua[1]} [{lingua[0]}]'

def get_lingua(lingua: str) -> str:
    dic_linguas = {
            #'eng': ['en', 'Inglés'],
            'eng': ['en', 'Ingles'],
            'ita': ['it', 'Italiano'],
            #'spa': ['cas', 'Castelán'],
            'spa': ['cas', 'Castelan'],
            #'fre': ['fr', 'Francés'],
            'fre': ['fr', 'Frances'],
            #'jpn': ['ni', 'Xaponés'],
            'jpn': ['ni', 'Xapones'],
            #'ger': ['de', 'Alemán'],
            'ger': ['de', 'Aleman'],
            'pol': ['pl', 'Polaco'],
            #'por': ['po', 'Portugués'],
            'por': ['po', 'Portugues'],
            'nor': ['no', 'Noruego'],
            'swe': ['sw', 'Sueco'],
            #'dut': ['nl', 'Neederlandés'],
            'dut': ['nl', 'Neederlandes'],
            #'fin': ['sk', 'Finlandés'],
            'fin': ['sk', 'Finlandes'],
            #'dan': ['da', 'Danés'],
            'dan': ['da', 'Danes'],
            #'ara': ['da', 'Árabe'],
            'ara': ['arabe', 'Arabe'],
            #'cat': ['cat', 'Catalán'],
            'cat': ['cat', 'Catalan'],
            'cze': ['checo', 'Checo'],
            'gre': ['grego', 'Grego'],
            'baq': ['eu', 'Euskera'],
            'fil': ['filipino', 'Filipino'],
            'glg': ['gz', 'Galego'],
            'heb': ['iv', 'Hebreo'],
            'hrv': ['croata', 'Croata'],
            #'hun': ['mn', 'Húngaro'],
            'hun': ['mn', 'Hungaro'],
            'ind': ['indonesio', 'Indonesio'],
            'kor': ['ko', 'Koreano'],
            'may': ['me', 'Malai'],
            'nob': ['nobok', 'Noruego de libro'],
            'rum': ['lr', 'Rumano'],
            'rus': ['rus', 'Ruso'],
            'tha': ['thai', 'Thai'],
            'tur': ['tu', 'Turko'],
            'ukr': ['uk', 'Ukraniano'],
            'vie': ['vietnamita', 'Vietnamita'],
            'chi': ['zh', 'Chinés'],
    }

    return formato_lingua(dic_linguas.get(lingua, f"ERRO: Engadir lingua '{lingua}'"))

def hms2s(tempo: str) -> str:
    h, m, s = tempo.split(':')
    s, ms = str(float(s)).split('.')
    return str(int(h)*60*60+int(m)*60+int(s))+'.'+ms

def get_codec_types() -> dict:
    return {
            'video': 'videos',
            'audio': 'audios',
            'subtitle': 'subtitulos',
            'attachment': 'adxuntos',
    }

def get_ignored_files() -> dict:
    return [
            '.txt',
            '.info',
            '.jpg',
            '.png',
    ]

def get_codec(codec: str) -> Union[str, None]:
    codec_types = get_codec_types()
    try:
        return codec_types[codec]
    except KeyError as e:
        raise Exception(f'Non existe o codec "{codec}".') from e
# ------------------------------------------------------------------------------
def canle(datos: dict, stream: dict, unidades: bool) -> dict:
    nova_canle = {}

    try:
        tags = stream['tags']
    except:
        tags = None

    codec = get_codec(stream['codec_type'])

    # Posición
    if ('index' in stream):
        #nova_canle['Posición'] = stream['index'] + 1
        nova_canle['Posicion'] = stream['index'] + 1
    # Codec
    if ('codec_name' in stream):
        nova_canle['Codec'] = stream['codec_name']
    # Índice
    if ('codec_long_name' in stream):
        nova_canle['Codec nome'] = stream['codec_long_name']
    # Nome
    if (tags and 'title' in tags):
        nova_canle['Nome'] = tags['title']
    # Nome Ficheiro
    if (tags and 'filename' in tags):
        nova_canle['Nome Ficheiro'] = tags['filename']
    # Comentario
    if (tags and 'comment' in tags):
        nova_canle['Comentario'] = tags['comment']
    # Lingua
    if (tags and 'language' in tags):
        nova_canle['Lingua'] = tags['language']
        nova_canle['Lingua2'] = get_lingua(tags['language'])
    # Resolución
    if (('width' in stream) and ('height' in stream)):
        #nova_canle['Resolución'] = str(stream['width']) + 'x' + str(stream['height'])
        nova_canle['Resolucion'] = str(stream['width']) + 'x' + str(stream['height'])
    # Ratio aspecto sample
    if ('sample_aspect_ratio' in stream):
        nova_canle['Ratio aspecto sample'] = stream['sample_aspect_ratio']
    # Ratio aspecto display
    if ('display_aspect_ratio' in stream):
        nova_canle['Ratio aspecto display'] = stream['display_aspect_ratio']
    # Formato de pixel
    if ('pix_fmt' in stream):
        nova_canle['Formato de pixel'] = stream['pix_fmt']
    # Frame Rate
    if ((stream['codec_type'] == 'video') and ('avg_frame_rate' in stream)):
        numerador, divisor = [int(ele) for ele in stream['avg_frame_rate'].split('/')]
        if (divisor == 0):
            nova_canle['Frame Rate'] = stream['avg_frame_rate'].split('/')[0]
            if (unidades):
                nova_canle['Frame Rate'] += ' fps'
        else:
            nova_canle['Frame Rate'] = str(round(numerador/divisor, 2))
            if (unidades):
                nova_canle['Frame Rate'] += ' fps'
    # Canles
    if ('channel_layout' in stream):
        nova_canle['Canles'] = " (".join(stream['channel_layout'].split('('))
    # Número canles
    if ('channels' in stream):
        #nova_canle['Número canles'] = stream['channels']
        nova_canle['Numero canles'] = stream['channels']
    # Sample Rate
    if ('sample_rate' in stream):
        nova_canle['Sample Rate'] = stream['sample_rate']
        if (unidades):
            nova_canle['Sample Rate'] += ' Hz'
    # Bit Rate
    if ('bit_rate' in stream):
        nova_canle['Bit Rate'] = stream['bit_rate']
        if (unidades):
            nova_canle['Bit Rate'] += ' b/s'
    # Tamanho
    if (tags and 'NUMBER_OF_BYTES' in tags):
        nova_canle['Tamanho'] = tags['NUMBER_OF_BYTES']
        if (unidades):
            nova_canle['Tamanho'] += ' B'
    # Inicio
    if ('start_time' in stream):
        nova_canle['Inicio'] = str(float(stream['start_time']))
        if (unidades):
            nova_canle['Inicio'] += ' s'
    # Duración
    if (tags and 'DURATION' in tags):
        #nova_canle['Duración'] = hms2s(tags['DURATION'])
        nova_canle['Duracion'] = hms2s(tags['DURATION'])
        if (unidades):
            #nova_canle['Duración'] += ' s'
            nova_canle['Duracion'] += ' s'
    if ('duration' in stream):
        #nova_canle['Duración'] = str(float(stream['duration']))
        nova_canle['Duracion'] = str(float(stream['duration']))
        if (unidades):
            #nova_canle['Duración'] += ' s'
            nova_canle['Duracion'] += ' s'

    # disposition

    # non existe a lista dos streams crear
    if (codec not in datos):
        datos[codec] = []
    # meter nova canle
    datos[codec].append(nova_canle)

    return datos
# ------------------------------------------------------------------------------
def get_info(fich: str, unidades: bool) -> dict:
    datos = {
            'Data': str(datetime.now()),
    }
    cancion = {}
    resumo = {}

    info = ffmpeg.probe(fich)

    try:
        formato = info['format']
    except:
        formato = None
    try:
        tags = formato['tags']
    except:
        tags = None

    # Ficheiro
    if (formato and 'nb_streams' in formato):
        datos['Ficheiro'] = formato['filename']
    # Nome Ficheiro
    if (formato and 'nb_streams' in formato):
        datos['Nome ficheiro'] = pathlib.Path(formato['filename']).stem
    # Extensión
        #datos['Extensión'] = pathlib.Path(formato['filename']).suffix
        datos['Extension'] = pathlib.Path(formato['filename']).suffix
    # Formato
    if (formato and 'format_name' in formato):
        datos['Formato'] = formato['format_name']
    # Formato nome
    if (formato and 'nb_streams' in formato):
        datos['Formato nome'] = formato['format_long_name']
    # Tamanho
    if (formato and 'nb_streams' in formato):
        datos['Tamanho'] = formato['size']
        if (unidades):
            datos['Tamanho'] += ' B'
    # Duración
    if (formato and 'nb_streams' in formato):
        #datos['Duración'] = str(float(formato['duration']))
        datos['Duracion'] = str(float(formato['duration']))
        if (unidades):
            #datos['Duración'] += ' s'
            datos['Duracion'] += ' s'
    # Bit Rate
    if (formato and 'nb_streams' in formato):
        datos['Bit Rate'] = formato['bit_rate']
        if (unidades):
            datos['Bit Rate'] += ' b/s'
    # Título
    if (tags and 'title' in tags):
        #datos['Título'] = tags['title']
        datos['Titulo'] = tags['title']
    # Data creación
    if (tags and 'creation_time' in tags):
        data = parser.parse(tags['creation_time'])
        #datos['Data creación'] = data.strftime('%Y-%m-%d %H:%M:') + str(float(data.strftime('%S.%f')))
        datos['Data creacion'] = data.strftime('%Y-%m-%d %H:%M:') + str(float(data.strftime('%S.%f')))
        del data
    # Cantidade de canles
    if (formato and 'nb_streams' in formato):
        datos['Cantidade de canles'] = formato['nb_streams']

    # Disposición das canles
    #datos['Disposición das canles'] = {}
    datos['Disposicion das canles'] = {}

    # streams
    if ('streams' in info):
        for stream in info['streams']:
            datos = canle(datos, stream, unidades)

    # Album
    if (tags and 'ALBUM' in tags):
        cancion['Album'] = tags['ALBUM']
    # Artista album
    if (tags and 'album_artist' in tags):
        cancion['Artista album'] = tags['album_artist']
    # Disco
    if (tags and 'disc' in tags):
        cancion['Disco'] = tags['disc']
    # /Discos
    if (tags and 'DISCTOTAL' in tags):
        cancion['Disco'] = cancion['Disco'] + '/' + tags['DISCTOTAL']
    # Título
    if (tags and 'TITLE' in tags):
        #cancion['Título'] = tags['TITLE']
        cancion['Titulo'] = tags['TITLE']
    # Artista
    if (tags and 'ARTIST' in tags):
        cancion['Artista'] = tags['ARTIST']
    # Pista
    if (tags and 'track' in tags):
        cancion['Pista'] = tags['track']
    # /Pistas
    if (tags and 'TRACKTOTAL' in tags):
        cancion['Pista'] = cancion['Pista'] + '/' + tags['TRACKTOTAL']
    # CopyRight
    if (tags and 'COPYRIGHT' in tags):
        cancion['CopyRight'] = tags['COPYRIGHT']
    # Data
    if (tags and 'DATE' in tags):
        cancion['Data'] = tags['DATE']

    # Canción
    if len(cancion.keys()) > 0:
        #datos['Canción'] = cancion
        datos['Cancion'] = cancion

    # Disposición das canles
    for ele in get_codec_types().values():
        if ele in datos:
            resumo[ele] = len(datos[ele])
    if (len(resumo.keys()) > 0):
        #datos['Disposición das canles'] = resumo
        datos['Disposicion das canles'] = resumo
    else:
        #del datos['Disposición das canles']
        del datos['Disposicion das canles']


    return datos
# ------------------------------------------------------------------------------
def main(ficheiro: str, info_orixinal: bool = False, unidades: bool = False) -> dict:
    # se é un directorio
    if (pathlib.Path(ficheiro).is_dir()):
        temp_path = pathlib.Path(ficheiro).glob('**/*')
        fichs = [x for x in temp_path if x.is_file()]
        saida = []
        for fich in fichs[::-1]:
            if (fich.suffix not in get_ignored_files()):
                saida.append(main(fich, info_orixinal, unidades))
    else:
        if (info_orixinal):
            saida = ffmpeg.probe(ficheiro)
        else:
            saida = get_info(ficheiro, unidades)
    return saida
# ------------------------------------------------------------------------------
