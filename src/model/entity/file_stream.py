#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/27 18:43:19.591632
#+ Editado:	2023/02/16 23:22:25.490609
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import BaseEntity, File, Codec, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class FileStream(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('FileStream'))
    file: File
    codec: Codec
    language: Language
    index: int
    title: Optional[str] = field(default=None)
    profile: Optional[str] = field(default=None)
    quality: Optional[str] = field(default=None)
    width: Optional[int] = field(default=None)
    height: Optional[int] = field(default=None)
    coded_width: Optional[int] = field(default=None)
    coded_height: Optional[int] = field(default=None)
    closed_captions: Optional[int] = field(default=None)
    film_grain: Optional[int] = field(default=None)
    has_b_frames: Optional[int] = field(default=None)
    sample_aspect_ratio: Optional[str] = field(default=None)
    display_aspect_ratio: Optional[str] = field(default=None)
    pixel_format: Optional[str] = field(default=None)
    level: Optional[int] = field(default=None)
    color: Optional[int] = field(default=None)
    color_range: Optional[str] = field(default=None)
    color_space: Optional[str] = field(default=None)
    color_transfer: Optional[str] = field(default=None)
    color_primaries: Optional[str] = field(default=None)
    chroma_location: Optional[str] = field(default=None)
    field_order: Optional[str] = field(default=None)
    refs: Optional[int] = field(default=None)
    is_avc: Optional[int] = field(default=None)
    nal_length_size: Optional[int] = field(default=None)
    r_frame_rate: Optional[float] = field(default=None)
    avg_frame_rate: Optional[float] = field(default=None)
    time_base: Optional[float] = field(default=None)
    start_pts: Optional[int] = field(default=None)
    bits_per_raw_sample: Optional[int] = field(default=None)
    bits_per_sample: Optional[int] = field(default=None)
    extradata_size: Optional[int] = field(default=None)
    default: Optional[int] = field(default=None)
    dub: Optional[int] = field(default=None)
    original: Optional[int] = field(default=None)
    comment: Optional[int] = field(default=None)
    lyrics: Optional[int] = field(default=None)
    karaoke: Optional[int] = field(default=None)
    forced: Optional[int] = field(default=None)
    hearing_impaired: Optional[int] = field(default=None)
    visual_impaired: Optional[int] = field(default=None)
    clean_effects: Optional[int] = field(default=None)
    attached_pic: Optional[int] = field(default=None)
    timed_thumbnails: Optional[int] = field(default=None)
    captions: Optional[int] = field(default=None)
    descriptions: Optional[int] = field(default=None)
    metadata: Optional[int] = field(default=None)
    dependent: Optional[int] = field(default=None)
    still_image: Optional[int] = field(default=None)
    start: Optional[float] = field(default=None)
    duration: Optional[float] = field(default=None)
    size: Optional[int] = field(default=None)
    bit_rate: Optional[int] = field(default=None)
    sample_rate: Optional[int] = field(default=None)
    sample_format: Optional[str] = field(default=None)
    channels: Optional[int] = field(default=None)
    channel_layout: Optional[str] = field(default=None)
    bps: Optional[int] = field(default=None)
    frame_number: Optional[int] = field(default=None)
    dmix_mode: Optional[int] = field(default=None)
    text_subtitle: Optional[int] = field(default=None)
    active: Optional[int] = field(default=1)
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
