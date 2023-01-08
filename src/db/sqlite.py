#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/08 15:50:59.650394
# ------------------------------------------------------------------------------
#* Concrete Strategy (Strategy Pattern)
# ------------------------------------------------------------------------------
import src.db.idb as idb

import sqlite3
from sqlite3 import Connection, Cursor

from typing import List, Tuple, Union

from src.dtos.Arquivo import Arquivo
from src.dtos.Almacen import Almacen
from src.dtos.Codec import Codec
from src.dtos.CompartirLugar import CompartirLugar
from src.dtos.Lingua import Lingua
from src.dtos.Media import Media
from src.dtos.MediaSituacion import MediaSituacion
from src.dtos.MediaTipo import MediaTipo
from src.dtos.MediaWeb import MediaWeb
from src.dtos.NomeCarpeta import NomeCarpeta
from src.dtos.Secuencia import Secuencia
from src.dtos.Web import Web
from src.dtos.ArquivoAdxunto import ArquivoAdxunto
from src.dtos.ArquivoAudio import ArquivoAudio
from src.dtos.ArquivoSubtitulo import ArquivoSubtitulo
from src.dtos.ArquivoVideo import ArquivoVideo
from src.dtos.Compartido import Compartido
# ------------------------------------------------------------------------------
class Sqlite(idb.DB):
    def __init__(self, ficheiro: str) -> None:
        self.ficheiro = ficheiro
        self.conn = None
        self.cur = None

    def get_conn(self) -> Connection:
        if self.conn == None:
            return self.conectar()[0]
        return self.con

    def get_cur(self) -> Cursor:
        if self.cur == None:
            return self.conectar()[1]
        return self.cur

    def conectar(self) -> tuple([Connection, Cursor]):
        self.conn = sqlite3.connect(self.ficheiro)
        self.cur = self.conn.cursor()
        return (self.conn, self.cur)

    def desconectar(self, commit: bool = True) -> None:
        if self.conn:
            if commit:
                self.conn.commit()
            self.conn.close()
            self.conn = None
            self.cur = None

    # SELECT
    def select(self, nome_taboa: str) -> List[Union[MediaTipo, MediaSituacion, Almacen, NomeCarpeta, Secuencia, CompartirLugar, Web]]:
        pass

    def select_tipos(self) -> List[MediaTipo]:
        results = self.get_cur().execute(f'select ID, Nome from "_Media Tipo"').fetchall()
        valores = []
        for result in results:
            valores.append(MediaTipo(id_=result[0], nome=result[1]))
        return valores

    def select_situacions(self) -> List[MediaSituacion]:
        results = self.get_cur().execute(f'select ID, Nome from "_Media Situación"').fetchall()
        valores = []
        for result in results:
            valores.append(MediaTipo(id_=result[0], nome=result[1]))
        return valores

    def select_almacens(self) -> List[Almacen]:
        results = self.get_cur().execute(f'select ID, Nome from "_Almacén"').fetchall()
        valores = []
        for result in results:
            valores.append(Almacen(id_=result[0], nome=result[1]))
        return valores

    def select_carpetas(self) -> List[NomeCarpeta]:
        results = self.get_cur().execute(f'select ID, Nome from "Nome Carpeta"').fetchall()
        valores = []
        for result in results:
            valores.append(NomeCarpeta(id_=result[0], nome=result[1]))
        return valores

    def select_secuencias(self) -> List[Secuencia]:
        results = self.get_cur().execute(f'select name, seq from "sqlite_sequence"').fetchall()
        valores = []
        for result in results:
            valores.append(Secuencia(nome=result[0], seq=result[1]))
        return valores

    def select_lugares(self) -> List[CompartirLugar]:
        results = self.get_cur().execute(f'select ID, Nome, Privado, Ligazón, Tipo, Plataforma from "_Compartir Lugar"').fetchall()
        valores = []
        for result in results:
            valores.append(CompartirLugar(id_=result[0], nome=result[1], privado=result[2], ligazon=result[3], tipo=result[4], plataforma=result[5]))
        return valores

    def select_webs(self) -> List[Web]:
        results = self.get_cur().execute(f'select ID, Nome, Siglas, Ligazón from "_Web"').fetchall()
        valores = []
        for result in results:
            valores.append(Web(id_=result[0], nome=result[1], siglas=result[2], ligazon=result[3]))
        return valores

    def get_lingua_by_code(self, code: str) -> Lingua:
        if code != None:
            result = self.get_cur().execute(f'select l.ID, l.Nome, l.Desc from "_Lingua Códigos" lc left join "_Lingua" l on l.ID=lc."ID Lingua" where lc."Código" like "{code}"').fetchone()
            if result != None:
                return Lingua(id_=result[0], nome=result[1], desc=result[2])
        return None

    def get_codec_by_name(self, name: str) -> Codec:
        if name != None:
            result = self.get_cur().execute(f'select ID, Nome, Nome Longo, Desc from "_Codec" where Nome like "{name}"').fetchone()
            if result != None:
                return Codec(id_=result[0], nome=result[1], nome_longo=result[2], desc=result[3])
        return None

    # INSERT
    def insert(self, obj: Union[Media, MediaWeb, NomeCarpeta, Arquivo, ArquivoAdxunto, ArquivoAudio, ArquivoSubtitulo, ArquivoVideo, Compartido]) -> None:
        pass

    def insert_media(self, obj: Media) -> None:
        self.get_cur().execute(f'insert into {Media.nome_taboa} ("ID", "Nome", "Ano Inicio", "Ano Fin", "ID Tipo", "ID Situación") values ("{obj.id_}", "{obj.nome}", "{obj.ano_ini}", "{obj.ano_fin}", "{obj.id_tipo}", "{obj.id_situacion}")')

    def insert_mediaweb(self, obj: MediaWeb) -> None:
        self.get_cur().execute(f'insert into "{MediaWeb.nome_taboa}" ("ID Media", "ID Web", "Ligazón") values ("{obj.id_media}", "{obj.id_web}", "{obj.ligazon}")')

    def insert_nomecarpeta(self, obj: NomeCarpeta) -> None:
        self.get_cur().execute(f'insert into "{NomeCarpeta.nome_taboa}" ("ID", "Nome", "ID Media") values ("{obj.id_}", "{obj.nome}", "{obj.id_media}")')

    def insert_arquivo(self, obj: Arquivo) -> None:
        self.get_cur().execute(f'insert into "{Arquivo.nome_taboa}" ("ID", "Nome", "Extensión", "Tamanho", "Duración", "Bit Rate", "Título", "Data Creación", "ID Almacén", "ID Carpeta", "ID Media", "ID Media Fascículo") values ("{obj.id_}", "{obj.nome}", "{obj.extension}", "{obj.tamanho}", "{obj.duracion}", "{obj.bit_rate}", "{obj.titulo}", "{obj.data_creacion}", "{obj.id_almacen}", "{obj.id_carpeta}", "{obj.id_media}", "{obj.id_media_fasciculo}")')

    def insert_arquivoadxunto(self, obj: ArquivoAdxunto) -> None:
        self.get_cur().execute(f'insert into "{ArquivoAdxunto.nome_taboa}" ("ID Arquivo", "ID Codec", "Nome", "Inicio", "Tamanho", "Duración") values ("{obj.id_arquivo}", "{obj.id_codec}", "{obj.nome}", "{obj.tamanho}", "{obj.inicio}", "{obj.duracion}")')

    def insert_arquivoaudio(self, obj: ArquivoAudio) -> None:
        self.get_cur().execute(f'insert into "{ArquivoAudio.nome_taboa}" ("ID Arquivo", "ID Codec", "Canles", "Sample Rate", "Bit Rate", "ID Lingua", "xDefecto", "Forzado", "Comentario", "Nome", "Tamanho", "Inicio", "Duración") values ("{obj.id_arquivo}", "{obj.id_codec}", "{obj.canles}", "{obj.sample_rate}", "{obj.bit_rate}", "{obj.id_lingua}", "{obj.xdefecto}", "{obj.forzado}", "{obj.comentario}", "{obj.nome}", "{obj.tamanho}", "{obj.inicio}", "{obj.duracion}")')

    def insert_arquivosub(self, obj: ArquivoSubtitulo) -> None:
        self.get_cur().execute(f'insert into "{ArquivoSubtitulo.nome_taboa}" ("ID Arquivo", "ID Codec", "ID Lingua", "xDefecto", "Forzado", "Texto", "Nome", "Tamanho", "Inicio", "Duración") values ("{obj.id_arquivo}", "{obj.id_codec}", "{obj.id_lingua}", "{obj.xdefecto}", "{obj.forzado}", "{obj.texto}", "{obj.nome}", "{obj.tamanho}", "{obj.inicio}", "{obj.duracion}")')

    def insert_arquivovideo(self, obj: ArquivoVideo) -> None:
        self.get_cur().execute(f'insert into "{ArquivoVideo.nome_taboa}" ("ID Arquivo", "ID Lingua", "Calidade", "Resolución", "ID Codec", "Aspecto Sample", "Aspecto Display", "Formato Pixel", "Sample Rate", "Bit Rate", "FPS", "Tamanho", "Inicio", "Duración", "Cor", "Nome") values ("{obj.id_arquivo}", "{obj.id_lingua}", "{obj.calidade}", "{obj.resolucion}", "{obj.id_codec}", "{obj.aspecto_sample}", "{obj.aspecto_display}", "{obj.formato_pixel}", "{obj.sample_rate}", "{obj.bit_rate}", "{obj.fps}", "{obj.tamanho}", "{obj.inicio}", "{obj.duracion}", "{obj.cor}", "{obj.nome}")')

    def insert_compartido(self, obj: Compartido) -> None:
        self.get_cur().execute(f'insert into "{Compartido.nome_taboa}" ("ID Arquivo", "ID Lugar", "Ligazón") values ("{obj.id_arquivo}", "{obj.id_lugar}", "{obj.ligazon}")')
# ------------------------------------------------------------------------------
