#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/26 21:12:03.645397
#+ Editado:	2023/03/17 16:32:32.093865
# ------------------------------------------------------------------------------
import logging
from pathlib import Path
import ffmpeg
from pymediainfo import MediaInfo
from typing import Union, List, Tuple, Dict

from src.utils import AddFileTerminalViewOutput, FileInfoServiceOutput
from src.utils import get_version, fraction_2_float

from src.model.entity import Extension, Warehouse, Media, Issue, File
from src.model.entity import Track, TrackLanguage, Encoder, Folder
from src.model.entity import Codec, Type, Language
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
        elif file_data.issues:
            self.medias = file_data.issues


    @staticmethod
    def get_file_info(file_path: str, original_name: str,
                      warehouse: Warehouse, media: Union[Media, Issue],
                      format_: dict, tags: dict, tracks: List[dict]) -> File:
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
            f = File(name=file_name, folder=Folder(path=str(folder)),
                     extension=extension, warehouse=warehouse, media=media)
        elif isinstance(media, Issue):
            f = File(name=file_name, folder=Folder(path=str(folder)),
                     extension=extension, warehouse=warehouse, issue=media)

        if original_name: f.original_name = original_name
        if ('title' in tags): f.title=tags['title']
        if ('nb_tracks' in format_): f.nb_tracks=format_['nb_tracks']
        if ('nb_programs' in format_): f.nb_programs=format_['nb_programs']
        if ('start_time' in format_): f.start=format_['start_time']
        if ('duration' in format_): f.duration=format_['duration']
        if ('size' in format_): f.size=format_['size']
        if ('bit_rate' in format_): f.bit_rate=format_['bit_rate']
        if ('probe_score' in format_): f.probe_score=format_['probe_score']
        if ('creation_time' in tags): f.creation_ts=tags['creation_time']
        if ('encoder' in tags): f.encoder=Encoder(name=tags['encoder'])

        try:
            # i can only try to access 1st since the tags are the same in all tracks
            if (tracks[0].get('tags') and '_STATISTICS_WRITING_APP' in tracks[0].get('tags')):
                f.version=get_version(tracks[0].get('tags').get('_STATISTICS_WRITING_APP'))
        except IndexError:
            pass
        return f

    @staticmethod
    def get_track_info(file: File, format_: Dict, tags: Dict,
                        track: Tuple[Dict, List[Dict]]) -> Tuple[Track, List[TrackLanguage]]:
        track, track2 = track

        languages = []

        tags = track.get('tags')
        disposition = track.get('disposition')

        # we assume these are always in the track
        codec = Codec(name=track.get('codec_name'), name_long=track.get('codec_long_name'),
                      type_=Type(name=track.get('codec_type')),
                      tag_string=track.get('codec_tag_string'), tag=track.get('codec_tag'))

        fs = Track(file=file, codec=codec, index=track.get('index'))

        # xFCR
        #if 'quality' in track: fs.quality
        #if 'text_subtitle' in track: fs.text_subtitle=track.get('text_subtitle')
        #if 'color' in track: fs.color=track.get('color')

        if 'profile' in track: fs.profile=track.get('profile')
        if 'sample_fmt' in track: fs.sample_format=track.get('sample_fmt')
        if 'sample_rate' in track: fs.sample_rate=track.get('sample_rate')
        if 'channels' in track: fs.channels=track.get('channels')
        if 'channel_layout' in track: fs.channel_layout=track.get('channel_layout')
        if 'width' in track: fs.width=track.get('width')
        if 'height' in track: fs.height=track.get('height')
        if 'coded_width' in track: fs.coded_width=track.get('coded_width')
        if 'coded_height' in track: fs.coded_height=track.get('coded_height')
        if 'closed_captions' in track: fs.closed_captions=track.get('closed_captions')
        if 'film_grain' in track: fs.film_grain=track.get('film_grain')
        if 'has_b_frames' in track: fs.has_b_frames=track.get('has_b_frames')
        if 'sample_aspect_ratio' in track: fs.sample_aspect_ratio=track.get('sample_aspect_ratio')
        if 'display_aspect_ratio' in track: fs.display_aspect_ratio=track.get('display_aspect_ratio')
        if 'pix_fmt' in track: fs.pixel_format=track.get('pix_fmt')
        if 'level' in track: fs.level=track.get('level')
        if 'color_range' in track: fs.color_range=track.get('color_range')
        if 'color_space' in track: fs.color_space=track.get('color_space')
        if 'color_transfer' in track: fs.color_transfer=track.get('color_transfer')
        if 'color_primaries' in track: fs.color_primaries=track.get('color_primaries')
        if 'chroma_location' in track: fs.chroma_location=track.get('chroma_location')
        if 'field_order' in track: fs.field_order=track.get('field_order')
        if 'refs' in track: fs.refs=track.get('refs')
        if 'is_avc' in track: fs.is_avc=track.get('is_avc')
        if 'nal_length_size' in track: fs.nal_length_size=track.get('nal_length_size')
        if 'r_frame_rate' in track: fs.r_frame_rate=fraction_2_float(track.get('r_frame_rate'))
        if 'avg_frame_rate' in track: fs.avg_frame_rate=fraction_2_float(track.get('avg_frame_rate'))
        if 'time_base' in track: fs.time_base=track.get('time_base')
        if 'bits_per_raw_sample' in track: fs.bits_per_raw_sample=track.get('bits_per_raw_sample')
        if 'bits_per_sample' in track: fs.bits_per_sample=track.get('bits_per_sample')
        if 'dmix_mode' in track: fs.dmix_mode=track.get('dmix_mode')
        if 'extradata_size' in track: fs.extradata_size=track.get('extradata_size')
        if 'start_pts' in track: fs.start_pts=track.get('start_pts')
        if 'start_time' in track: fs.start=track.get('start_time')
        if 'bit_rate' in track: fs.bit_rate=track.get('bit_rate')
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
            if 'language' in tags:
                # i leave this like this since when i make the dtos it will make more sense
                if isinstance(tags.get('language'), list):
                    for lang in tags.get('language'):
                        languages.append(Language(name=lang))
                else:
                    #languages.append(Language(name=tags.get('language')))
                    languages.append(Language(name=track2.get('language')))
            if 'title' in tags: fs.title=tags.get('title')
            if 'BPS' in tags: fs.bps=tags.get('BPS')
            if 'DURATION' in tags: fs.duration=tags.get('DURATION')
            if 'NUMBER_OF_FRAMES' in track: fs.frame_number=track.get('NUMBER_OF_FRAMES')
            if 'NUMBER_OF_BYTES' in tags: fs.size=tags.get('NUMBER_OF_BYTES')

        return (fs, [TrackLanguage(track=fs, language=lang) for lang in languages])

    def run(self) -> List[FileInfoServiceOutput]:
        logging.info(_(f'Executing the run method of the FileInfoService class'))
        output = []
        for file_path, original_name, warehouse, media in zip(self.file_paths, self.original_names,
                                                              self.warehouses, self.medias):
            output_tracks = []
            file_info = ffmpeg.probe(file_path)
            file_info2 = MediaInfo.parse(file_path).to_data()['tracks']

            tracks = file_info.get('streams', None)
            format_ = file_info.get('format', None)
            if format_:
                tags = format_.get('tags', None)

            # file
            file=self.get_file_info(file_path=file_path, original_name=original_name,
                                 warehouse=warehouse, media=media, format_=format_,
                                 tags=tags, tracks=tracks)
            for track, track2 in zip(tracks, file_info2[1:]):
                output_tracks.append(self.get_track_info(file=file, format_=format_,
                                                           tags=tags, track=(track, track2)))

            output.append(FileInfoServiceOutput(file=file, tracks=output_tracks))
        return output

# ------------------------------------------------------------------------------
