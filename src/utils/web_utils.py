#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# + Autor:  	Ran#
# + Creado: 	2023/03/28 21:50:56.938123
# + Editado:	2026/03/17 00:00:00.000000
# ------------------------------------------------------------------------------
import aiohttp
import asyncio
from pathlib import Path
from blake3 import blake3
from typing import List
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
def _image_ext(data: bytes) -> str:
    """Detect image extension from magic bytes (replaces removed imghdr module)."""
    if data[:3] == b"\xff\xd8\xff":
        return "jpg"
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return "png"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return "gif"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    if data[:2] == b"BM":
        return "bmp"
    return "bin"


async def download_image(folder: Path, link: str, hash_name: bool = True) -> Path:
    """Given a image link will download it to the specified folder"""

    folder.mkdir(parents=True, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            value = await response.read()

    if hash_name:
        filename = blake3(value).hexdigest()
    else:
        filename = link.split("/")[-1]
    filename = folder / filename

    if filename.suffix == "":
        filename = filename.with_suffix("." + _image_ext(value))

    with filename.open("wb") as f:
        f.write(value)

    return filename


async def download_images(folder: str, links: List[str]) -> List[Path]:
    """Given a list of image links will download each one to the specified folder"""
    if not isinstance(links, list):
        links = [links]
    return await asyncio.gather(*[download_image(folder=folder, link=link) for link in links])


# ------------------------------------------------------------------------------
