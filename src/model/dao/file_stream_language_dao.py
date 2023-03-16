#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/03/13 21:56:47.666911
#+ Editado:	2023/03/15 21:50:15.644179
# ------------------------------------------------------------------------------
from src.model import iModel

from src.exception import UnknownLanguageException
from src.model.entity import LanguageCode, LanguageName
from src.model.entity import FileStreamLanguage
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
class FileStreamLanguageDao:
    """Data Access Object"""

    def __init__(self, model: iModel) -> None:
        self.model = model

    """
    def __get_codec_type(self, codec_type: CodecType) -> CodecType:
        ""Bring the full data of the object from DB and insert it if new.""
        if codec_type:
            found_codec_type=self.model.get_by_nk(codec_type)
            if not found_codec_type:
                self.model.insert(codec_type)
                return self.__get_codec_type(codec_type)
            return found_codec_type

    def __get_codec(self, codec: Codec) -> Codec:
        ""Bring the full data of the object from DB and insert it if new.""
        if codec:
            codec.type_=self.__get_codec_type(codec.type_)
            found_codec=self.model.get_by_nk(codec)
            if not found_codec:
                self.model.insert(codec)
                return self.__get_codec(codec)
            return found_codec
    """

    def save(self, stream_language: FileStreamLanguage) -> FileStreamLanguage:
        # language
        if stream_language.language.name is not None:
            is_code = self.model.exists(LanguageCode(language=None, code=None,
                                                     codename=stream_language.language.name))
            is_name = self.model.exists(LanguageName(language=None, name=stream_language.language.name))

            if not is_code and not is_name:
                raise UnknownLanguageException(codename=stream_language.language.name)
            elif is_code:
                stream_language.language = self.model.get_language_by_codename(codename=stream_language.language.name)
            elif is_name:
                stream_language.language = self.model.get_by_name(stream_language.language)
                if isinstance(stream_language.language, list):
                    raise Exception('Why is this a list?')

        found_stream_language = self.model.get_by_nk(stream_language)
        if found_stream_language:
            return found_stream_language

        self.model.insert(stream_language)
        return self.model.get_by_nk(stream_language)
# ------------------------------------------------------------------------------
