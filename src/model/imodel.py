#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/15 20:15:24.889827
# ------------------------------------------------------------------------------
#* Strategy Interface (Strategy Pattern)
# ------------------------------------------------------------------------------
from abc import ABC, abstractmethod
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
from src.dtos.Secuencia import Secuencia
from src.dtos.Web import Web
# ------------------------------------------------------------------------------
class iModel(ABC):
    @abstractmethod
    def get_conn_db(self) -> Connection:
        pass

    @abstractmethod
    def get_cur_db(self) -> Cursor:
        pass

    @abstractmethod
    def connect_db(self) -> tuple([Connection, Cursor]):
        pass

    @abstractmethod
    def disconnect_db(self, commit: bool = True) -> None:
        pass

    @abstractmethod
    def save_db(self) -> None:
        pass

    @abstractmethod
    def select(self, nome_taboa: str, alfabetic: bool = False) -> List[Union[MediaTipo, MediaSituacion, Almacen, NomeCarpeta, Secuencia, CompartirLugar, Web, Lingua, Pais]]:
        pass

    @abstractmethod
    def get_situacion_by_name(self, name: str) -> MediaSituacion:
        pass

    @abstractmethod
    def get_lingua_by_code(self, code: str) -> Lingua:
        pass

    @abstractmethod
    def get_codec_by_name(self, name: str) -> Codec:
        pass

    @abstractmethod
    def get_nomecarpeta_by_name(self, name: str) -> NomeCarpeta:
        pass

    @abstractmethod
    def get_mediatipo_agrupables(self, id_only:bool = False) -> List[Union[MediaTipo, str]]:
        pass

    @abstractmethod
    def insert(self, obj: Union[Media, MediaAgrupacion, MediaFasciculo, MediaWeb, NomeCarpeta, Arquivo, ArquivoAdxunto, ArquivoAudio, ArquivoSubtitulo, ArquivoVideo, Compartido, MediaNomes, MediaNomesLinguas, MediaNomesPaises]) -> Union[None, int]:
        pass
# ------------------------------------------------------------------------------
