#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/03/28 19:05:06.665609
#+ Editado:	2023/03/29 20:01:03.958508
# ------------------------------------------------------------------------------
import asyncio
from pathlib import Path
from typing import List, Tuple, List

from src.utils import Config, download_images
from src.enum import MetadataSourcesEnum
from src.service import TMDBService

from src.model.entity import MediaPlatform, Poster, Extension
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
class MetadataService:
    """Service for obtaining all the required metadata"""

    source: MetadataSourcesEnum

    def __init__(self, source: MetadataSourcesEnum) -> None:
        self.source = source

    def download_posters(self, media_platforms: List[MediaPlatform]) -> List[Poster]:
        if self.source == MetadataSourcesEnum.TMDB:
            links, paths = self.__download_poster_tmdb(links=[ele.link for ele in media_platforms])

        posters = []
        for link, path, media in zip(links, paths, [ele.media for ele in media_platforms]):
            posters.append(Poster(extension=Extension(name=path.suffix), name=path.stem, media=media))
        return posters

    def __download_poster_tmdb(self, links: List[str]) -> Tuple[List[str], List[Path]]:
        links = asyncio.run(TMDBService().get_poster_links(links=links))
        paths = asyncio.run(download_images(folder=Config().poster_folder, links=links))

        return links, paths

# ------------------------------------------------------------------------------
