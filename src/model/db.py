#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/09 23:34:52.860281
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
import src.model.idb as idb
# ------------------------------------------------------------------------------
from sqlite3 import Connection, Cursor
from typing import List, Tuple, Union

from src.dtos.MediaTipo import MediaTipo
from src.dtos.MediaSituacion import MediaSituacion
from src.dtos.Almacen import Almacen
from src.dtos.NomeCarpeta import NomeCarpeta
from src.dtos.Secuencia import Secuencia
from src.dtos.Lingua import Lingua
from src.dtos.Codec import Codec
from src.dtos.CompartirLugar import CompartirLugar
from src.dtos.Web import Web
from src.dtos.Media import Media
from src.dtos.MediaWeb import MediaWeb
from src.dtos.Arquivo import Arquivo
from src.dtos.ArquivoAdxunto import ArquivoAdxunto
from src.dtos.ArquivoAudio import ArquivoAudio
from src.dtos.ArquivoSubtitulo import ArquivoSubtitulo
from src.dtos.Compartido import Compartido
from src.dtos.ArquivoVideo import ArquivoVideo
# ------------------------------------------------------------------------------
class DB:
    def __init__(self, db: idb.DB):
        # obrigamos ó uso dunha instancia
        if isinstance(db, idb.DB):
            self.db = db
        else:
            raise ValueError("Ten que herdar de " + DB.__name__)

    def get_conn(self) -> Connection:
        return self.db.get_conn()

    def get_cur(self) -> Cursor:
        return self.db.get_cur()

    def conectar(self) -> tuple([Connection, Cursor]):
        return self.db.conectar()

    def desconectar(self, commit: bool = True) -> None:
        return self.db.desconectar(commit)

    def save(self) -> None:
        return self.db.save()

    # SELECT
    def select(self, nome_taboa: str) -> List[Union[MediaTipo, MediaSituacion, Almacen, NomeCarpeta, Secuencia, CompartirLugar, Web]]:
        if nome_taboa == MediaTipo.nome_taboa:
            return self.db.select_tipos()
        elif nome_taboa == MediaSituacion.nome_taboa:
            return self.db.select_situacions()
        elif nome_taboa == Almacen.nome_taboa:
            return self.db.select_almacens()
        elif nome_taboa == NomeCarpeta.nome_taboa:
            return self.db.select_carpetas()
        elif nome_taboa == Secuencia.nome_taboa:
            return self.db.select_secuencias()
        elif nome_taboa == CompartirLugar.nome_taboa:
            return self.db.select_lugares()
        elif nome_taboa == Web.nome_taboa:
            return self.db.select_webs()

    def get_situacion_by_name(self, name: str) -> MediaSituacion:
        return self.db.get_situacion_by_name(name)

    def get_lingua_by_code(self, code: str) -> Lingua:
        return self.db.get_lingua_by_code(code)

    def get_codec_by_name(self, name: str) -> Codec:
        return self.db.get_codec_by_name(name)

    def get_nomecarpeta_by_name(self, name: str) -> NomeCarpeta:
        return self.db.get_nomecarpeta_by_name(name)

    # INSERT
    def insert(self, obj: Union[Media, MediaWeb, NomeCarpeta, Arquivo, ArquivoAdxunto, ArquivoAudio, ArquivoSubtitulo, ArquivoVideo, Compartido]) -> None:
        if type(obj) == Media:
            return self.db.insert_media(obj)
        elif type(obj) == MediaWeb:
            return self.db.insert_mediaweb(obj)
        elif type(obj) == NomeCarpeta:
            return self.db.insert_nomecarpeta(obj)
        elif type(obj) == Arquivo:
            return self.db.insert_arquivo(obj)
        elif type(obj) == ArquivoAdxunto:
            return self.db.insert_arquivoadxunto(obj)
        elif type(obj) == ArquivoAudio:
            return self.db.insert_arquivoaudio(obj)
        elif type(obj) == ArquivoSubtitulo:
            return self.db.insert_arquivosub(obj)
        elif type(obj) == ArquivoVideo:
            return self.db.insert_arquivovideo(obj)
        elif type(obj) == Compartido:
            return self.db.insert_compartido(obj)
# ------------------------------------------------------------------------------
