[//]: # ( -*- coding: utf-8 -*- )
[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Autor:  	Ran# )
[//]: # (+ Creado: 	2023/02/12 15:28:24.413478 )
[//]: # (+ Editado:	2023/02/20 18:23:47.395420 )
[//]: # ( ---------------------------------------------------------------------- )

# Tables
Explanation of what each table of the database was designed to contain.

## Index
- [Platform](#platform)
- [ShareSite](#sharesite)
- [Codec](#codec)
- [CodecType](#codectype)
- [Media](#media)
- [MediaGroup](#mediagroup)
- [MediaIssue](#mediaissue)
- [MediaType](#mediatype)
- [MediaStatus](#mediastatus)
- [Language](#language)
- [Code](#code)

## Platform
Refers to the place that holds the ShareSite site.
The ShareSite may not have a platform it is enclosed in.

For example:
If the [ShareSite](#sharesite) is a Telegram Channel its related [Platform](#platform) would be "Telegram".
On the other hand, if the [ShareSite](#sharesite) is a website the [Platform](#platform) would be null.

## ShareSite
What medium/site is the [Media](#media) shared at, this [ShareSite](#sharesite) can have a platform (like "Telegram") or not (if it its own website).

For example:
If the [ShareSite](#sharesite) is a Telegram Channel its related [Platform](#platform) would be "Telegram".
On the other hand, if the [ShareSite](#sharesite) is a website the [Platform](#platform) would be null.

## Codec
Property related to a [File](#file) stream.
It gives information of what type of encoding it has.
Some examples are "h264", "ac3" or "subrip".

## CodecType
The type of the [Codec](#codec) related to the [File](#file) stream.
Some examples are "video", "audio" or "subitle".

## Media
Any element of media like a movie, a tv show, a documentary, a band, a youtube channel etc.
The distinction of which type it is is made with the relationship with [MediaType](#mediatype).

## MediaGroup
Intermedium grouping for [Media](#media) elements.
A perfect example for this is a tv show season, though its also used for things like a music album.

## MediaIssue
Minimum entity separation a [Media](#media) can have.
They can also have a related [MediaGroup](#mediaGroup).
This can be an episode, a book chapter, a youtube video or even a song.

## MediaType
What is the type of the [Media](#media) its related with.
This can be a film, a tv show, a book, a youtube channel or even a music band.

## MediaStatus
What is the status of the [Media](#media) its related with.
This can be in emision, canceled, premiered, etc.

## Language
Spoken and written languages arround the world.

## Code
Represents what type of codes exist and with its relationship with other entities it assigns a code to each.
Right now only related with [Language](#language) but it can be extended in the future.
Examples os this can be "ISO 639-3", "Glottolog" or "LCID".
