#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/27 21:28:18.456217
#+ Editado:	2023/03/04 14:47:19.429974
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Union

from src.model.entity import Media, MediaIssue, Warehouse
from src.model.entity import File, FileStream
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
    media_issues: Optional[List[MediaIssue]] = field(default=None)

    def __post__init__(self) -> None:
        if not any([self.medias, self.media_issues]):
            raise TypeError(f'{self.__class__.__name}.__init__() missing 1 \
                    required positional argument: "medias" or "media_issues"')

        if media_issues and len(file_paths) != len(media_issues):
            raise TypeError(f'{self.__class__.__name}.__init__() the class attribute \
                    lists "file_paths" and "media_issues" are not the same length.')
# ------------------------------------------------------------------------------
@dataclass
class FileInfoServiceOutput:
    """Class that encapsulates the return elements of the run method of the
    FileInfoService class."""
    file: File
    streams: List[FileStream]
# ------------------------------------------------------------------------------
