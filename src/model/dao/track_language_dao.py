#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/03/13 21:56:47.666911
#+ Editado:	2023/03/16 19:00:07.493545
# ------------------------------------------------------------------------------
from src.model import iModel

from src.exception import UnknownLanguageException
from src.model.entity import LanguageCode, LanguageName
from src.model.entity import TrackLanguage
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
class TrackLanguageDao:
    """Data Access Object"""

    def __init__(self, model: iModel) -> None:
        self.model = model

    def save(self, track_language: TrackLanguage) -> TrackLanguage:
        # language
        if track_language.language.name is not None:
            is_code = self.model.exists(LanguageCode(language=None, code=None,
                                                     codename=track_language.language.name))
            is_name = self.model.exists(LanguageName(language=None, name=track_language.language.name))

            if not is_code and not is_name:
                raise UnknownLanguageException(codename=track_language.language.name)
            elif is_code:
                track_language.language = self.model.get_language_by_codename(codename=track_language.language.name)
            elif is_name:
                track_language.language = self.model.get_by_name(track_language.language)
                if isinstance(track_language.language, list):
                    raise Exception('Why is this a list?')

        found_track_language = self.model.get_by_nk(track_language)
        if found_track_language:
            return found_track_language

        self.model.insert(track_language)
        return self.model.get_by_nk(track_language)
# ------------------------------------------------------------------------------
