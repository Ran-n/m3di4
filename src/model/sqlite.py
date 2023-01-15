#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/15 21:25:02.819723
# ------------------------------------------------------------------------------
#* Concrete Strategy (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.model.imodel import iModel
# ------------------------------------------------------------------------------
import sqlite3
from sqlite3 import Connection, Cursor, IntegrityError

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
class Sqlite(iModel):
    def __init__(self, ficheiro: str) -> None:
        self.ficheiro = ficheiro
        self.conn = None
        self.cur = None

    def get_conn_db(self) -> Connection:
        if self.conn == None:
            return self.connect_db()[0]
        return self.conn

    def get_cur_db(self) -> Cursor:
        if self.cur == None:
            return self.connect_db()[1]
        return self.cur

    def connect_db(self) -> tuple([Connection, Cursor]):
        self.conn = sqlite3.connect(self.ficheiro)
        self.cur = self.conn.cursor()
        return (self.conn, self.cur)

    def disconnect_db(self, commit: bool = True) -> None:
        if self.conn:
            if commit:
                self.conn.commit()
            self.conn.close()
            self.conn = None
            self.cur = None

    def save_db(self) -> None:
        if self.conn:
            self.conn.commit()

    # SELECT
    def select(self, nome_taboa: str, alfabetic: bool = False) -> List[Union[MediaTipo, MediaSituacion, Almacen, NomeCarpeta, Secuencia, CompartirLugar, Web, Lingua, Pais]]:
        pass

    def select_mediatipos(self) -> List[MediaTipo]:
        results = self.get_cur_db().execute(f'select ID, Nome, Agrupable from "_Media Tipo"').fetchall()
        valores = []
        for result in results:
            valores.append(MediaTipo(id_=result[0], nome=result[1], agrupable=result[2]))
        return valores

    def select_situacions(self) -> List[MediaSituacion]:
        results = self.get_cur_db().execute(f'select ID, Nome from "_Media Situación"').fetchall()
        valores = []
        for result in results:
            valores.append(MediaSituacion(id_=result[0], nome=result[1]))
        return valores

    def select_almacens(self) -> List[Almacen]:
        results = self.get_cur_db().execute(f'select ID, Nome from "_Almacén"').fetchall()
        valores = []
        for result in results:
            valores.append(Almacen(id_=result[0], nome=result[1]))
        return valores

    def select_carpetas(self) -> List[NomeCarpeta]:
        results = self.get_cur_db().execute(f'select ID, Nome from "Nome Carpeta"').fetchall()
        valores = []
        for result in results:
            valores.append(NomeCarpeta(id_=result[0], nome=result[1]))
        return valores

    def select_secuencias(self) -> List[Secuencia]:
        results = self.get_cur_db().execute(f'select name, seq from "sqlite_sequence"').fetchall()
        valores = []
        for result in results:
            valores.append(Secuencia(nome=result[0], seq=result[1]))
        return valores

    def select_lugares(self) -> List[CompartirLugar]:
        results = self.get_cur_db().execute(f'select ID, Nome, Privado, Ligazón, Tipo, Plataforma from "_Compartir Lugar"').fetchall()
        valores = []
        for result in results:
            valores.append(CompartirLugar(id_=result[0], nome=result[1], privado=result[2], ligazon=result[3], tipo=result[4], plataforma=result[5]))
        return valores

    def select_webs(self) -> List[Web]:
        results = self.get_cur_db().execute(f'select ID, Nome, Siglas, Ligazón from "_Web"').fetchall()
        valores = []
        for result in results:
            valores.append(Web(id_=result[0], nome=result[1], siglas=result[2], ligazon=result[3]))
        return valores

    def select_linguas(self, alfabetic: bool = False) -> List[Lingua]:
        results = self.get_cur_db().execute(f'select ID, Nome, Desc from "{Lingua.nome_taboa}"').fetchall()
        valores = []
        for result in results:
            valores.append(Lingua(id_=result[0], nome=result[1], desc=result[2]))
        if alfabetic: valores.sort()
        return valores

    def select_paises(self) -> List[Pais]:
        results = self.get_cur_db().execute(f'select ID, Nome, Reino from "{Pais.nome_taboa}"').fetchall()
        valores = []
        for result in results:
            valores.append(Pais(id_=result[0], nome=result[1], reino=result[2]))
        return valores


    # GET BY X
    def get_lingua_by_code(self, code: str) -> Lingua:
        if code:
            result = self.get_cur_db().execute(f'select l.ID, l.Nome, l.Desc from "_Lingua Códigos" lc left join "_Lingua" l on l.ID=lc."ID Lingua" where lc."Código" like "{code}"').fetchone()
            if result:
                return Lingua(id_=result[0], nome=result[1], desc=result[2])
        return None

    def get_codec_by_name(self, name: str) -> Codec:
        if name:
            result = self.get_cur_db().execute(f'select ID, Nome, Nome Longo, Desc from "_Codec" where Nome like "{name}"').fetchone()
            if result:
                return Codec(id_=result[0], nome=result[1], nome_longo=result[2], desc=result[3])
        return None

    def get_situacion_by_name(self, name: str) -> MediaSituacion:
        if name:
            result = self.get_cur_db().execute(f'select "ID", "Nome" from "{MediaSituacion.nome_taboa}" where "Nome" like ?', (name,)).fetchone()
            if result:
                return MediaSituacion(id_=result[0], nome=result[1])
        return None

    def get_nomecarpeta_by_name(self, name: str) -> NomeCarpeta:
        if name:
            result = self.get_cur_db().execute(f'select "ID", "Nome" from "{NomeCarpeta.nome_taboa}" where "Nome" like ?', (name,)).fetchone()
            if result:
                return NomeCarpeta(id_=result[0], nome=result[1])
        return None

    def get_mediatipo_agrupables(self, id_only:bool = False) -> List[Union[MediaTipo, str]]:
        results = self.get_cur_db().execute(f'select ID, Nome, Agrupable from "_Media Tipo"').fetchall()
        valores = []
        if id_only:
            for result in results:
                if result[2]:
                    valores.append(result[0])
        else:
            for result in results:
                if result[2]:
                    valores.append(MediaTipo(id_=result[0], nome=result[1], agrupable=result[2]))
        return valores

    # INSERT
    def insert(self, obj: Union[Media, MediaAgrupacion, MediaFasciculo, MediaWeb, NomeCarpeta, Arquivo, ArquivoAdxunto, ArquivoAudio, ArquivoSubtitulo, ArquivoVideo, Compartido, MediaNomes, MediaNomesLinguas, MediaNomesPaises]) -> Union[None, int]:
        pass

    def insert_media(self, obj: Media) -> None:
        self.get_cur_db().execute(f'insert into "{obj.nome_taboa}" ("ID", "Nome", "Ano Inicio", "Ano Fin", "ID Tipo", "ID Situación") values (?, ?, ?, ?, ?, ?)', (obj.id_, obj.nome, obj.ano_ini, obj.ano_fin, obj.id_tipo, obj.id_situacion))

    def insert_mediaagrupacion(self, obj: MediaAgrupacion) -> None:
        self.get_cur_db().execute(f'insert into "{obj.nome_taboa}" ("ID", "Nome", "Número", "Ano Inicio", "Ano Fin", "ID Media") values (?, ?, ?, ?, ?, ?)', (obj.id_, obj.nome, obj.numero, obj.ano_ini, obj.ano_fin, obj.id_media))

    def insert_mediafasciculo(self, obj: MediaFasciculo) -> None:
        self.get_cur_db().execute(f'insert into "{obj.nome_taboa}" ("ID", "Número total", "Número en agrupación", "Nome", "Data", "ID Media", "ID Media Agrupación") values (?, ?, ?, ?, ?, ?, ?)', (obj.id_, obj.num_total, obj.num_agrupacion, obj.nome, obj.data, obj.id_media, obj.id_media_agrupacion))

    def insert_mediaweb(self, obj: MediaWeb) -> None:
        self.get_cur_db().execute(f'insert into "{MediaWeb.nome_taboa}" ("ID Media", "ID Web", "Ligazón") values (?, ?, ?)', (obj.id_media, obj.id_web, obj.ligazon))

    def insert_nomecarpeta(self, obj: NomeCarpeta) -> Union[None, int]:
        try:
            self.get_cur_db().execute(f'insert into "{NomeCarpeta.nome_taboa}" ("ID", "Nome") values (?, ?)', (obj.id_, obj.nome))
        except IntegrityError:
            return self.get_nomecarpeta_by_name(obj.nome).id_
        return None

    def insert_arquivo(self, obj: Arquivo) -> None:
        self.get_cur_db().execute(f'insert into "{Arquivo.nome_taboa}" ("ID", "Nome", "Extensión", "Tamanho", "Duración", "Bit Rate", "Título", "Data Creación", "ID Almacén", "ID Carpeta", "ID Media", "ID Media Fascículo") values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (obj.id_, obj.nome, obj.extension, obj.tamanho, obj.duracion, obj.bit_rate, obj.titulo, obj.data_creacion, obj.id_almacen, obj.id_carpeta, obj.id_media, obj.id_media_fasciculo))

    def insert_arquivoadxunto(self, obj: ArquivoAdxunto) -> None:
        self.get_cur_db().execute(f'insert into "{ArquivoAdxunto.nome_taboa}" ("ID Arquivo", "ID Codec", "Nome", "Inicio", "Tamanho", "Duración") values (?, ?, ?, ?, ?, ?)', (obj.id_arquivo, obj.id_codec, obj.nome, obj.tamanho, obj.inicio, obj.duracion))

    def insert_arquivoaudio(self, obj: ArquivoAudio) -> None:
        self.get_cur_db().execute(f'insert into "{ArquivoAudio.nome_taboa}" ("ID Arquivo", "ID Codec", "Canles", "Sample Rate", "Bit Rate", "ID Lingua", "xDefecto", "Forzado", "Comentario", "Nome", "Tamanho", "Inicio", "Duración") values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (obj.id_arquivo, obj.id_codec, obj.canles, obj.sample_rate, obj.bit_rate, obj.id_lingua, obj.xdefecto, obj.forzado, obj.comentario, obj.nome, obj.tamanho, obj.inicio, obj.duracion))

    def insert_arquivosub(self, obj: ArquivoSubtitulo) -> None:
        self.get_cur_db().execute(f'insert into "{ArquivoSubtitulo.nome_taboa}" ("ID Arquivo", "ID Codec", "ID Lingua", "xDefecto", "Forzado", "Texto", "Nome", "Tamanho", "Inicio", "Duración") values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (obj.id_arquivo, obj.id_codec, obj.id_lingua, obj.xdefecto, obj.forzado, obj.texto, obj.nome, obj.tamanho, obj.inicio, obj.duracion))

    def insert_arquivovideo(self, obj: ArquivoVideo) -> None:
        self.get_cur_db().execute(f'insert into "{ArquivoVideo.nome_taboa}" ("ID Arquivo", "ID Lingua", "Calidade", "Resolución", "ID Codec", "Aspecto Sample", "Aspecto Display", "Formato Pixel", "Sample Rate", "Bit Rate", "FPS", "Tamanho", "Inicio", "Duración", "Cor", "Nome") values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (obj.id_arquivo, obj.id_lingua, obj.calidade, obj.resolucion, obj.id_codec, obj.aspecto_sample, obj.aspecto_display, obj.formato_pixel, obj.sample_rate, obj.bit_rate, obj.fps, obj.tamanho, obj.inicio, obj.duracion, obj.cor, obj.nome))

    def insert_compartido(self, obj: Compartido) -> None:
        self.get_cur_db().execute(f'insert into "{Compartido.nome_taboa}" ("ID Arquivo", "ID Lugar", "Ligazón") values (?, ?, ?)', (obj.id_arquivo, obj.id_lugar, obj.ligazon))

    def insert_medianomes(self, obj: MediaNomes) -> int:
        self.get_cur_db().execute(f'insert into "{obj.nome_taboa}" ("ID", "Nome", "ID Media", "ID Media Agrupación", "ID Media Fascículo") values (?, ?, ?, ?, ?)', (obj.id_, obj.nome, obj.id_media, obj.id_media_agrupacion, obj.id_media_fasciculo))

    def insert_medianomeslinguas(self, obj: MediaNomesLinguas) -> None:
        self.get_cur_db().execute(f'insert into "{obj.nome_taboa}" ("ID Media Nomes", "ID Lingua") values (?, ?)', (obj.id_media_nomes, obj.id_lingua))

    def insert_medianomespaises(self, obj: MediaNomesPaises) -> None:
        self.get_cur_db().execute(f'insert into "{obj.nome_taboa}" ("ID Media Nomes", "ID País") values (?, ?)', (obj.id_media_nomes, obj.id_pais))
# ------------------------------------------------------------------------------
