#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/14 17:36:04.413922
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.model.imodel import iModel
# ------------------------------------------------------------------------------
from sqlite3 import Connection, Cursor
from typing import List, Tuple, Union

from src.dtos.Almacen import Almacen
from src.dtos.Arquivo import Arquivo
from src.dtos.ArquivoAdxunto import ArquivoAdxunto
from src.dtos.ArquivoAudio import ArquivoAudio
from src.dtos.ArquivoSubtitulo import ArquivoSubtitulo
from src.dtos.ArquivoVideo import ArquivoVideo
from src.dtos.Codec import Codec
from src.dtos.Compartido import Compartido
from src.dtos.CompartirLugar import CompartirLugar
from src.dtos.Lingua import Lingua
from src.dtos.Media import Media
from src.dtos.MediaNomes import MediaNomes
from src.dtos.MediaNomesLinguas import MediaNomesLinguas
from src.dtos.MediaNomesPaises import MediaNomesPaises
from src.dtos.MediaSituacion import MediaSituacion
from src.dtos.MediaTipo import MediaTipo
from src.dtos.MediaWeb import MediaWeb
from src.dtos.NomeCarpeta import NomeCarpeta
from src.dtos.Pais import Pais
from src.dtos.Secuencia import Secuencia
from src.dtos.Web import Web
# ------------------------------------------------------------------------------
class Model:
    def __init__(self, strategy: iModel):
        # obrigamos ó uso dunha instancia
        if isinstance(strategy, iModel):
            self.model = strategy
        else:
            raise ValueError("Ten que herdar de " + iModel.__name__)

    def get_conn_db(self) -> Connection:
        return self.model.get_conn_db()

    def get_cur_db(self) -> Cursor:
        return self.model.get_cur_db()

    def connect_db(self) -> tuple([Connection, Cursor]):
        return self.model.connect_db()

    def disconnect_db(self, commit: bool = True) -> None:
        return self.model.disconnect_db(commit)

    def save_db(self) -> None:
        return self.model.save_db()

    # SELECT
    def select(self, nome_taboa: str, alfabetic: bool = False) -> List[Union[MediaTipo, MediaSituacion, Almacen, NomeCarpeta, Secuencia, CompartirLugar, Web, Lingua, Pais]]:
        if nome_taboa == MediaTipo.nome_taboa:
            return self.model.select_tipos()
        elif nome_taboa == MediaSituacion.nome_taboa:
            return self.model.select_situacions()
        elif nome_taboa == Almacen.nome_taboa:
            return self.model.select_almacens()
        elif nome_taboa == NomeCarpeta.nome_taboa:
            return self.model.select_carpetas()
        elif nome_taboa == Secuencia.nome_taboa:
            return self.model.select_secuencias()
        elif nome_taboa == CompartirLugar.nome_taboa:
            return self.model.select_lugares()
        elif nome_taboa == Web.nome_taboa:
            return self.model.select_webs()
        elif nome_taboa == Lingua.nome_taboa:
            return self.model.select_linguas(alfabetic)
        elif nome_taboa == Pais.nome_taboa:
            return self.model.select_paises()

    def get_situacion_by_name(self, name: str) -> MediaSituacion:
        return self.model.get_situacion_by_name(name)

    def get_lingua_by_code(self, code: str) -> Lingua:
        return self.model.get_lingua_by_code(code)

    def get_codec_by_name(self, name: str) -> Codec:
        return self.model.get_codec_by_name(name)

    def get_nomecarpeta_by_name(self, name: str) -> NomeCarpeta:
        return self.model.get_nomecarpeta_by_name(name)

    # INSERT
    def insert(self, obj: Union[Media, MediaWeb, NomeCarpeta, Arquivo, ArquivoAdxunto, ArquivoAudio, ArquivoSubtitulo, ArquivoVideo, Compartido, MediaNomes, MediaNomesLinguas, MediaNomesPaises]) -> Union[None, int]:
        if type(obj) == Media:
            return self.model.insert_media(obj)
        elif type(obj) == MediaWeb:
            return self.model.insert_mediaweb(obj)
        elif type(obj) == NomeCarpeta:
            return self.model.insert_nomecarpeta(obj)
        elif type(obj) == Arquivo:
            return self.model.insert_arquivo(obj)
        elif type(obj) == ArquivoAdxunto:
            return self.model.insert_arquivoadxunto(obj)
        elif type(obj) == ArquivoAudio:
            return self.model.insert_arquivoaudio(obj)
        elif type(obj) == ArquivoSubtitulo:
            return self.model.insert_arquivosub(obj)
        elif type(obj) == ArquivoVideo:
            return self.model.insert_arquivovideo(obj)
        elif type(obj) == Compartido:
            return self.model.insert_compartido(obj)
        elif type(obj) == MediaNomes:
            return self.model.insert_medianomes(obj)
        elif type(obj) == MediaNomesLinguas:
            return self.model.insert_medianomeslinguas(obj)
        elif type(obj) == MediaNomesPaises:
            return self.model.insert_medianomespaises(obj)
# ------------------------------------------------------------------------------
