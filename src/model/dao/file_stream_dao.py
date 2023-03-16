#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/03/08 18:48:53.576098
#+ Editado:	2023/03/13 21:57:01.412361
# ------------------------------------------------------------------------------
from src.model import iModel

from src.model.entity import File, FileStream, Codec, CodecType
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
class FileStreamDao:
    """Data Access Object"""

    def __init__(self, model: iModel) -> None:
        self.model = model

    def __get_codec_type(self, codec_type: CodecType) -> CodecType:
        """Bring the full data of the object from DB and insert it if new."""
        if codec_type:
            found_codec_type=self.model.get_by_nk(codec_type)
            if not found_codec_type:
                self.model.insert(codec_type)
                return self.__get_codec_type(codec_type)
            return found_codec_type

    def __get_codec(self, codec: Codec) -> Codec:
        """Bring the full data of the object from DB and insert it if new."""
        if codec:
            codec.type_=self.__get_codec_type(codec.type_)
            found_codec=self.model.get_by_nk(codec)
            if not found_codec:
                self.model.insert(codec)
                return self.__get_codec(codec)
            return found_codec

    def save(self, stream: FileStream) -> FileStream:
        found_stream = self.model.get_by_nk(stream)
        if found_stream:
            return found_stream

        stream.codec=self.__get_codec(stream.codec)

        self.model.insert(stream)
        return self.model.get_by_nk(stream)

        """
        if stream.language is not None:
            if self.model.exists(LanguageCode(language=None, code=None, codename=stream.language.name)):
                print('existe')
            else:
                raise UnknownLanguageException(codename=stream.language.name)
        """
# ------------------------------------------------------------------------------
