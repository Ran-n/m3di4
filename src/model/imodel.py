#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/03/30 22:19:42.404936
# ------------------------------------------------------------------------------
#* Strategy Interface (Strategy Pattern)
# ------------------------------------------------------------------------------
from abc import ABC, abstractmethod
# ------------------------------------------------------------------------------
from sqlite3 import Connection, Cursor
from typing import List, Union, Tuple

from src.model.entity import Media, Group, Issue
from src.model.entity import Type, Status
from src.model.entity import Platform, ShareSite, ShareSiteSubs
from src.model.entity import Warehouse
from src.model.entity import Extension, Folder, App, Version, Encoder, File
from src.model.entity import Codec, Language, Track, TrackLanguage
from src.model.entity import LanguageCode, Poster, MediaPlatform
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
class iModel(ABC):  # pylint: disable=C0103
    """Strategy Interface for the model part of the MVC design."""

    @abstractmethod
    def get_conn_db(self) -> Connection:
        """ Returns a connection to the DB.
        @ Input:
        @ Output:
        ╚═ Connection   -   Connection object to the DB.
        """

    @abstractmethod
    def get_cur_db(self) -> Cursor:
        """ Returns a cursor to the DB.
        @ Input:
        @ Output:
        ╚═ Cursor   -   Cursor object in the DB.
        """

    @abstractmethod
    def connect_db(self) -> tuple([Connection, Cursor]):
        """ Does the whole process of connecting to a DB.
        @ Input:
        @ Ouput:
        ╚═ (Connection, Cursor) -   Tuple with objects of DB Connection and Cursor.
        """

    @abstractmethod
    def disconnect_db(self, commit: bool = True) -> None:
        """ Does the whole process of disconnecting from a DB.
        @ Input:
        ╚═  · commit -   bool    -   True
            └ Indicates if changes to the DB should be commited or rolled back.
        @ Output:
        """

    @abstractmethod
    def save_db(self) -> None:
        """ Saves the non commited changes to the DB.
        @ Input:
        @ Output:
        """

    @abstractmethod
    def exists(self, obj: Union[Group, Issue, Platform,
            Type, ShareSite, Warehouse, Extension,
            LanguageCode, Media, MediaPlatform, Poster]) -> bool:
        """ Checks if a element is saved in the DB.
        @ Input:
        ╚═  · obj   -   Any Entity Object   -   True
            └ Object to check if it exists in the DB.
        @ Output:
        ╚═  bool    -   Indicating if the object exists or not.
        """

    @abstractmethod
    def get_num(self, table_name: Union[str, Tuple[str, str]]) -> int:
        """ Returns the number of elements in a table.
        @ Input:
        ╚═  · table_name    -   str, Tuple[str]
            └ Name/s of the table to query.
        @ Output:
        ╚═  int - Number of entries on the table/s.
        """

    @abstractmethod
    def get_group_num_by_media_id(self, media_id: int) -> int:
        """ Returns the number of group elements discriminating by media id.
        @ Input:
        ╚═  · media_id  -   int
            └ Id of the media to use as a discriminator.
        @ Output:
        ╚═  int - Number of entries on the table that meet the criteria.
        """

    @abstractmethod
    def get_all(self, table_name: Union[str, Tuple[str, str]], limit: int = None,
                offset: int = 0, alfabetic: bool = False) -> List[Union[
                    Type, Status, Media, Platform, ShareSite, Issue, Warehouse, Poster,
                    MediaPlatform]]:
        """ Return all elements of a table.
        @ Input:
        ╠═  · table_name    -   str
        ║   └ Name of the table to query.
        ╠═  · limit         -   int     -   None
        ║   └ Maximum number of elements to retrieve.
        ╠═  · offset        -   int     -   0
        ║   └ How far removed from the start should the results to return start.
        ╚═  · alfabetic     -   bool    -   None
            └ Indicate if the output should be alfabetically ordered.
        @ Output:
        ╚═  List[Any Entity Object]   -   With all the information of the table.
        """

    # ---

    @abstractmethod
    def get_by_id(self, table_name: str, id_: int) ->\
            Union[Type, Status, Media,
                  Platform, Group, App,
                  Extension, Warehouse, Folder, Issue,
                  Version, Encoder, File, Codec,
                  Track, Language, Poster]:
        """ Returns a element of the table discriminating by its id.
        @ Input:
        ╠═  · table_name    -   str
        ║   └ Name of the table to query.
        ╚═  · id_           -   int
            └ Identifier of the element to gather from the table.
        @ Output:
        ╠═  Any Entity Object    -   The element of the table discriminated by id.
        ╚═  None                 -   If no matches exists.
        """

    @abstractmethod
    def get_by_nk(self, obj: Union[Group, Version, Encoder, File, Type, Codec]) -> \
            Union[Group, Version, Encoder, File, Type, Codec, Track,
                  Language, TrackLanguage, Poster, Media]:
        """ Returns a group discriminated by its natural key (NK).
        @ Input:
        ╚═  · obj   -   Entity
            └ The Entity object to use in the search.
        @ Output:
        ╠═  Any Entity  -   The element of the table discriminated by natural key.
        ╚═  None        -   If no matches exists.
        """

    @abstractmethod
    def get_group_by_media_id(self, id_: int, limit: int = None,
                                    offset: int = 0, alfabetic: bool = None
                                    ) -> Union[None, List[Group]]:
        """ Returns a group discriminated by its id.
        @ Input:
        ╠═  · id_       -   int
        ║   └ Id of the media to use as a discriminator.
        ╠═  · limit     -   int     -   None
        ║   └ Maximum number of elements to retrieve.
        ╠═  · offset    -   int     -   0
        ║   └ How far removed from the start should the results to return start.
        ╚═  · alfabetic -   bool    -   None
            └ Indicate if the output should be alfabetically ordered.
        @ Output:
        ╠═  Group   -   The element of the table discriminated by natural key.
        ╚═  None         -   If no matches exists.
        """

    def get_language_by_codename(self, codename: str) -> Union[None, Language]:
        """ Returns a language discriminated by the given codename.
        If a new code is added that makes it so codenames are reused
        for different languages this function must be rewritten.
        @ Input:
        ╠═  · codename  -   str
        ║   └ Code that identifies the language in some system.
        ╠═  · limit     -   int     -   None
        ║   └ Maximum number of elements to retrieve.
        ╠═  · offset    -   int     -   0
        ║   └ How far removed from the start should the results to return start.
        ╚═  · alfabetic -   bool    -   None
            └ Indicate if the output should be alfabetically ordered.
        @ Output:
        ╠═  Language    -   That matches the codename posibilities.
        ╚═  None        -   If no matches exists.
        """

    @abstractmethod
    def get_by_name(self, table_name: str, name: str, limit: int = None,
                    offset: int = 0, alfabetic: bool = False
                    ) -> Union[None, List[Union[Type, Status,
                                                Extension, Folder, App, Language]]]:
        """ Returns all elements of table that match the given name.
        @ Input:
        ╠═  · table_name    -   str
        ║   └ Id of the media to use as a discriminator.
        ╠═  · name          -   str
        ║   └ Name to use to descriminate the data of the table by.
        ╠═  · limit         -   int     -   None
        ║   └ Maximum number of elements to retrieve.
        ╠═  · offset        -   int     -   0
        ║   └ How far removed from the start should the results to return start.
        ╚═  · alfabetic     -   bool    -   None
            └ Indicate if the output should be alfabetically ordered.
        @ Output:
        ╠═  List[Any Entity Object] -   The elements of the table discriminated by name.
        ╚═  None                    -   If no matches exists.
        """

    # ---

    @abstractmethod
    def insert(self, obj: Union[Status, Type, Media, Group,
                                Issue, Platform, ShareSite,
                                Warehouse, Extension, Folder, App,
                                Version, Encoder, Codec, Track,
                                TrackLanguage, Poster, MediaPlatform]
               ) -> None:
        """ Adds an element to a DB table.
        @ Input:
        ╚═  · obj   -   Any Entity Type
            └ Entity to insert in the DB.
        @ Output:
        ╚═  None
        """
# ------------------------------------------------------------------------------
