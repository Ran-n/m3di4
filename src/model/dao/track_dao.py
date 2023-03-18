#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/03/08 18:48:53.576098
#+ Editado:	2023/03/17 23:38:08.213756
# ------------------------------------------------------------------------------
from src.model import iModel

from src.model.entity import File, Track, Codec, Type
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
class TrackDao:
    """Data Access Object"""

    def __init__(self, model: iModel) -> None:
        self.model = model

    def __get_type(self, type: Type) -> Type:
        """Bring the full data of the object from DB and insert it if new."""
        if type:
            found_type=self.model.get_by_nk(type)
            if not found_type:
                self.model.insert(type)
                return self.__get_type(type)
            return found_type

    def __get_codec(self, codec: Codec) -> Codec:
        """Bring the full data of the object from DB and insert it if new."""
        if codec:
            codec.type_=self.__get_type(codec.type_)
            found_codec=self.model.get_by_nk(codec)
            if not found_codec:
                self.model.insert(codec)
                return self.__get_codec(codec)
            return found_codec

    def save(self, track: Track) -> Track:
        found_track = self.model.get_by_nk(track)
        if found_track:
            return found_track

        track.codec=self.__get_codec(track.codec)

        self.model.insert(track)
        return self.model.get_by_nk(track)

        """
        if track.language is not None:
            if self.model.exists(LanguageCode(language=None, code=None, codename=track.language.name)):
                print('existe')
            else:
                raise UnknownLanguageException(codename=track.language.name)
        """
# ------------------------------------------------------------------------------
