[//]: # ( -*- coding: utf-8 -*- )
[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Autor:  	Ran# )
[//]: # (+ Creado: 	2023/02/12 15:28:24.413478 )
[//]: # (+ Editado:	2023/03/12 20:16:17.611579 )
[//]: # ( ---------------------------------------------------------------------- )

[↩️](index.md#documentation)

# Tables
Explanation of what each table of the database was designed to contain.

## Index
- [Platform](#platform)
- [ShareSite](#sharesite)
- [ShareSiteType](#sharesitetype)
- [ShareSiteSubs](#sharesitesubs)
- [Codec](#codec)
- [CodecType](#codectype)
- [Media](#media)
- [MediaGroup](#mediagroup)
- [MediaIssue](#mediaissue)
- [MediaType](#mediatype)
- [MediaStatus](#mediastatus)
- [MediaPoster](#mediaposter)
- [Language](#language)
- [Code](#code)
- [CodeName](#codename)
- [App](#app)
- [AppVersion](#appversion)
- [File](#file)
- [FileStream](#filestream)
- [Country](#country)
- [Web](#web)
- [Encoder](#encoder)
- [Warehouse](#warehouse)
- [WarehouseType](#warehousetype)
- [Extension](#extension)
- [Folder](#folder)

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

## ShareSiteType
What is the type of the [ShareSite](#sharesite) medium its related to.

Examples of these would be "group" or "channel".

## ShareSiteSubs
Number of people that are subscribed on a particular [ShareSite](#sharesite).
This is its own table since the number its regularly updated and records of its previous value are kept.

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

## CodeName
All the different types of names a [Code](#code) can have.

## App
Application used for the creation of a [File](#file).

## AppVersion
Specific version of an [App](#app) used in the creation of a [File](#file).

## File
Particular physical representation of the [Media](#media) or [MediaIssue](#mediaissue) saved in the database.
It can be composed of [streams](#filestreams).

## FileStream
Some [Files](#file) such as vídeos or audios have something called streams.
These are simply smaller components of whose combination results in the specific [File](#file) that contains them.

For example, in a video [File](#file), some streams could be the video image, its sound, a embedded image and a subtitle track.
In the case of a standard audio [File](#file), it would have one single stream being the sound.

## Country
Contains states/nations that currently exist or existed in the past.

## Web
Website that currently or formerly existed.

This data could technically overlap with the one inside [Platform](#platform) or [ShareSite](#sharesite) since any of those can be websites, but this table is thought more as a information website related to [Media](#media) (like imdb or tmdb).

It could be interesting to also link both [MediaGroup](#mediagroup) and [MediaIssue](#mediaissue) to this table aswell; but for now this is postponned since it can be deduced from the present arrangement.

## Encoder
Information related to a [File](#file) creation.

One example of an encoder would be: "libebml v1.4.4 + libmatroska v1.7.1".

## Warehouse
Location where a [File](#file) is stored at.
This can be a physical or virtual, its [type](#warehousetype) will determine it.

Examples of this would be: The library of Alexandria, a personal computer, a cloud storage place or a external hard drive.

## WarehouseType
Determines the type of a [Warehouse](#warehouse) element.

Building on the previous examples: the type of the library of Alexandria could be library, of a personal computer could be hard drive or computer, of a cloud storage place could be cloud, web or cloud/web hard drive and of a external hard drive could be hard drive.

## MediaPoster
This table is thought to be used by graphical user interfaces to know where to get from images for showing in the user interface.

For example, what folder and file name to pull all the images of all the [medias](#media) to show in a list [medias](#media) screen.

## Extension
What extension do the files posses.
This is related to the tables [File](#file) and [MediaPoster](#mediaposter).

Some examples are: 'mkv', 'mp4', 'pdf', 'mp3', 'avi', 'png', 'gif', 'ogg', etc.

## Folder
Path of the folder that contains a [File](#file).
Using this information as well as the [Warehouse](#warehouse) one a file should be unequivocally traceable.
