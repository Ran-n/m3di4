#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/03/28 21:50:56.938123
#+ Editado:	2023/03/29 19:43:34.108885
# ------------------------------------------------------------------------------
import aiohttp
import asyncio
from pathlib import Path
from blake3 import blake3
import imghdr
from typing import List
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
async def download_image(folder: Path, link: str, hash_name: bool = True) -> Path:
    """Given a image link will download it to the specified folder"""

    folder.mkdir(parents=True, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            value = await response.read()

    if hash_name:
        filename = blake3(value).hexdigest()
    else:
        filename = link.split('/')[-1]
    filename = folder/filename

    if filename.suffix == '':
        filename=filename.with_suffix('.'+imghdr.what(file=None, h=value).replace('jpeg', 'jpg'))

    with filename.open('wb') as f:
        f.write(value)

    return filename

async def download_images(folder: str, links: List[str]) -> List[Path]:
    """Given a list of image links will download each one to the specified folder"""
    if not isinstance(links, list):
        links = [links]
    return await asyncio.gather(*[download_image(folder=folder, link=link) for link in links])
# ------------------------------------------------------------------------------
