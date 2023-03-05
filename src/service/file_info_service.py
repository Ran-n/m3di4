#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/26 21:12:03.645397
#+ Editado:	2023/03/04 21:22:04.657915
# ------------------------------------------------------------------------------
import logging
from pathlib import Path
import ffmpeg
from typing import Union, List

from src.utils import AddFileTerminalViewOutput, FileInfoServiceOutput
from src.utils import get_app_version, fraction_2_float

from src.model.entity import Extension, Warehouse, Media, MediaIssue, File
from src.model.entity import FileStream, Encoder, Folder
#from src.model.entity import AppVersion, App
from src.model.entity import Codec, CodecType, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
class FileInfoService:
    """"""

    def __init__(self, file_data: AddFileTerminalViewOutput) -> None:
        logging.info(_(f'Starting the FileInfoService'))
        self.file_data = file_data

        self.original_names = file_data.original_names
        self.file_paths = file_data.file_paths
        self.warehouses = file_data.warehouses
        if file_data.medias:
            self.medias = file_data.medias
        elif file_data.media_issues:
            self.medias = file_data.media_issues


    @staticmethod
    def get_file_info(file_path: str, original_name: str,
                      warehouse: Warehouse, media: Union[Media, MediaIssue],
                      format_: dict, tags: dict, streams: List[dict]) -> File:
        """
        """
        filename = None
        extension = None
        if ('filename' in format_):
            file_name = Path(format_['filename']).stem
            folder = Path(format_['filename']).parent
            extension = Extension(name=Path(format_['filename']).suffix,
                      format_name=format_.get('format_name'),
                      format_name_long=format_.get('format_long_name'))

        if isinstance(media, Media):
            f = File(name=file_name, extension=extension, warehouse=warehouse, media=media)
        elif isinstance(media, MediaIssue):
            f = File(name=file_name, extension=extension, warehouse=warehouse, media_issue=media)

        f.folder=Folder(path=str(folder))
        if original_name: f.original_name = original_name
        if ('title' in tags): f.title=tags['title']
        if ('nb_streams' in format_): f.nb_streams=format_['nb_streams']
        if ('nb_programs' in format_): f.nb_programs=format_['nb_programs']
        if ('start_time' in format_): f.start=format_['start_time']
        if ('duration' in format_): f.duration=format_['duration']
        if ('size' in format_): f.size=format_['size']
        if ('bit_rate' in format_): f.bit_rate=format_['bit_rate']
        if ('probe_score' in format_): f.probe_score=format_['probe_score']
        if ('creation_time' in tags): f.creation_ts=tags['creation_time']
        if ('encoder' in tags): f.encoder=Encoder(name=tags['encoder'])

        try:
            # i can only try to access 1st since the tags are the same in all streams
            if (streams[0].get('tags') and '_STATISTICS_WRITING_APP' in streams[0].get('tags')):
                f.app_version=get_app_version(streams[0].get('tags').get('_STATISTICS_WRITING_APP'))
        except IndexError:
            pass
        return f

    @staticmethod
    def get_stream_info(file: File, format_: dict, tags: dict,
                        stream: dict) -> FileStream:

        tags = stream.get('tags')
        disposition = stream.get('disposition')

        # we assume these are always in the stream
        codec = Codec(name=stream.get('codec_name'), name_long=stream.get('codec_long_name'),
                      type_=CodecType(name=stream.get('codec_type')),
                      tag_string=stream.get('codec_tag_string'), tag=stream.get('codec_tag'))

        fs = FileStream(file=file, codec=codec, index=stream.get('index'))

        #if 'quality' in stream: fs.quality
        #if 'text_subtitle' in stream: fs.text_subtitle=stream.get('text_subtitle')
        #if 'color' in stream: fs.color=stream.get('color')

        if 'profile' in stream: fs.profile=stream.get('profile')
        if 'sample_fmt' in stream: fs.sample_format=stream.get('sample_fmt')
        if 'sample_rate' in stream: fs.sample_rate=stream.get('sample_rate')
        if 'channels' in stream: fs.channels=stream.get('channels')
        if 'channel_layout' in stream: fs.channel_layout=stream.get('channel_layout')
        if 'width' in stream: fs.width=stream.get('width')
        if 'height' in stream: fs.height=stream.get('height')
        if 'coded_width' in stream: fs.coded_width=stream.get('coded_width')
        if 'coded_height' in stream: fs.coded_height=stream.get('coded_height')
        if 'closed_captions' in stream: fs.closed_captions=stream.get('closed_captions')
        if 'film_grain' in stream: fs.film_grain=stream.get('film_grain')
        if 'has_b_frames' in stream: fs.has_b_frames=stream.get('has_b_frames')
        if 'sample_aspect_ratio' in stream: fs.sample_aspect_ratio=stream.get('sample_aspect_ratio')
        if 'display_aspect_ratio' in stream: fs.display_aspect_ratio=stream.get('display_aspect_ratio')
        if 'pix_fmt' in stream: fs.pixel_format=stream.get('pix_fmt')
        if 'level' in stream: fs.level=stream.get('level')
        if 'color_range' in stream: fs.color_range=stream.get('color_range')
        if 'color_space' in stream: fs.color_space=stream.get('color_space')
        if 'color_transfer' in stream: fs.color_transfer=stream.get('color_transfer')
        if 'color_primaries' in stream: fs.color_primaries=stream.get('color_primaries')
        if 'chroma_location' in stream: fs.chroma_location=stream.get('chroma_location')
        if 'field_order' in stream: fs.field_order=stream.get('field_order')
        if 'refs' in stream: fs.refs=stream.get('refs')
        if 'is_avc' in stream: fs.is_avc=stream.get('is_avc')
        if 'nal_length_size' in stream: fs.nal_length_size=stream.get('nal_length_size')
        if 'r_frame_rate' in stream: fs.r_frame_rate=fraction_2_float(stream.get('r_frame_rate'))
        if 'avg_frame_rate' in stream: fs.avg_frame_rate=fraction_2_float(stream.get('avg_frame_rate'))
        if 'time_base' in stream: fs.time_base=stream.get('time_base')
        if 'bits_per_raw_sample' in stream: fs.bits_per_raw_sample=stream.get('bits_per_raw_sample')
        if 'bits_per_sample' in stream: fs.bits_per_sample=stream.get('bits_per_sample')
        if 'dmix_mode' in stream: fs.dmix_mode=stream.get('dmix_mode')
        if 'extradata_size' in stream: fs.extradata_size=stream.get('extradata_size')
        if 'start_pts' in stream: fs.start_pts=stream.get('start_pts')
        if 'start_time' in stream: fs.start=stream.get('start_time')
        if 'bit_rate' in stream: fs.bit_rate=stream.get('bit_rate')
        if disposition:
            if 'default' in disposition: fs.default=disposition.get('default')
            if 'dub' in disposition: fs.dub=disposition.get('dub')
            if 'original' in disposition: fs.original=disposition.get('original')
            if 'comment' in disposition: fs.comment=disposition.get('comment')
            if 'lyrics' in disposition: fs.lyrics=disposition.get('lyrics')
            if 'karaoke' in disposition: fs.karaoke=disposition.get('karaoke')
            if 'forced' in disposition: fs.forced=disposition.get('forced')
            if 'hearing_impaired' in disposition: fs.hearing_impaired=disposition.get('hearing_impaired')
            if 'visual_impaired' in disposition: fs.visual_impaired=disposition.get('visual_impaired')
            if 'clean_effects' in disposition: fs.clean_effects=disposition.get('clean_effects')
            if 'attached_pic' in disposition: fs.attached_pic=disposition.get('attached_pic')
            if 'timed_thumbnails' in disposition: fs.timed_thumbnails=disposition.get('timed_thumbnails')
            if 'captions' in disposition: fs.captions=disposition.get('captions')
            if 'descriptions' in disposition: fs.descriptions=disposition.get('descriptions')
            if 'metadata' in disposition: fs.metadata=disposition.get('metadata')
            if 'dependent' in disposition: fs.dependent=disposition.get('dependent')
            if 'still_image' in disposition: fs.still_image=disposition.get('still_image')
        if tags:
            if 'language' in tags: fs.language=Language(name=tags.get('language'))
            if 'title' in tags: fs.title=tags.get('title')
            if 'BPS' in tags: fs.bps=tags.get('BPS')
            if 'DURATION' in tags: fs.duration=tags.get('DURATION')
            if 'NUMBER_OF_FRAMES' in stream: fs.frame_number=stream.get('NUMBER_OF_FRAMES')
            if 'NUMBER_OF_BYTES' in tags: fs.size=tags.get('NUMBER_OF_BYTES')

        return fs

    def run(self) -> List[FileInfoServiceOutput]:
        logging.info(_(f'Executing the run method of the FileInfoService class'))
        output = []
        for file_path, original_name, warehouse, media in zip(self.file_paths, self.original_names,
                                                              self.warehouses, self.medias):
            output_streams = []
            file_info = ffmpeg.probe(file_path)

            streams = file_info.get('streams', None)
            format_ = file_info.get('format', None)
            if format_:
                tags = format_.get('tags', None)

            # file
            file=self.get_file_info(file_path=file_path, original_name=original_name,
                                 warehouse=warehouse, media=media, format_=format_,
                                 tags=tags, streams=streams)
            for stream in streams:
                output_streams.append(self.get_stream_info(file=file, format_=format_,
                                                           tags=tags, stream=stream))

            output.append(FileInfoServiceOutput(file=file, streams=output_streams))
        return output

# ------------------------------------------------------------------------------
