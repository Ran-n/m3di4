#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/27 21:28:18.456217
#+ Editado:	2023/03/16 21:53:40.602927
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Union, Tuple

from src.model.entity import Media, Issue, Warehouse
from src.model.entity import File, Track, TrackLanguage
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class AddFileTerminalViewOutput:
    """Class that encapsulates what the add function of a file in the terminal
    view should return."""
    original_names: List[str]
    file_paths: List[Path]
    warehouses: List[Warehouse]
    medias: Optional[Media] = field(default=None)
    issues: Optional[List[Issue]] = field(default=None)

    def __post__init__(self) -> None:
        if not any([self.medias, self.issues]):
            raise TypeError(f'{self.__class__.__name}.__init__() missing 1 \
                    required positional argument: "medias" or "issues"')

        if issues and len(file_paths) != len(issues):
            raise TypeError(f'{self.__class__.__name}.__init__() the class attribute \
                    lists "file_paths" and "issues" are not the same length.')
# ------------------------------------------------------------------------------
@dataclass
class FileInfoServiceOutput:
    """Class that encapsulates the return elements of the run method of the
    FileInfoService class."""
    file: File
    tracks: List[Tuple[Track, List[TrackLanguage]]]
# ------------------------------------------------------------------------------
