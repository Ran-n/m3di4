#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/03/27 15:55:28.670916
#+ Editado:	2023/03/28 21:48:45.559900
# ------------------------------------------------------------------------------
import aiohttp
import logging
import asyncio
from typing import List

from src.utils import Config
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
class TMDBService:
    """Service for quering the TMDB API"""

    base_url: str = 'https://api.themoviedb.org/3/'
    img_base_url: str = 'https://image.tmdb.org/t/p/original'

    def __init__(self) -> None:
        logging.info(_(f'''Starting the TMDBService with api key =
                       {Config().tmdb_api_key}'''))
        self.api_key = Config().tmdb_api_key

    async def get_poster_links(self, links: List[str]) -> List[str]:
        return await asyncio.gather(*[self.get_poster_link(link) for link in links])

    async def get_poster_link(self, link: str) -> str:
        tmdb_media_type, tmdb_id = [ele.split('-')[0] for ele in link.split('/')[-3:] if ele != '']

        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.base_url}{tmdb_media_type}/{tmdb_id}?api_key={self.api_key}') as response:
                value = await response.json()

        try:
            return self.img_base_url+value['poster_path']
        except KeyError:
            return None

# ------------------------------------------------------------------------------
