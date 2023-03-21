[//]: # ( -*- coding: utf-8 -*- )
[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Autor:  	Ran# )
[//]: # (+ Creado: 	2023/02/12 15:28:24.413478 )
[//]: # (+ Editado:	2023/03/20 17:28:50.129184 )
[//]: # ( ---------------------------------------------------------------------- )

[↩️](index.md#documentation)

# Tables
Explanation of what each table of the database was designed to contain.

## Index
- [Type](#type)
- [Status](#status)
- [Platform](#platform)
- [ShareSite](#sharesite)
- [ShareSiteSubs](#sharesitesubs)
- [Codec](#codec)
- [Media](#media)
- [Group](#group)
- [Issue](#issue)
- [Poster](#poster)
- [Language](#language)
- [Code](#code)
- [CodeName](#codename)
- [App](#app)
- [Version](#version)
- [File](#file)
- [Track](#track)
- [Country](#country)
- [Encoder](#encoder)
- [Warehouse](#warehouse)
- [Extension](#extension)
- [Folder](#folder)

## Type
Global type object, used to categorize elements.
For [Media](#media) this can be a "film", "tv show", "book", "youtube channel" or simply "channel" and even a "music band".
For [ShareSite](#sharesite) this can be mediums such as "group" or "channel".
For [Codec](#codec) some examples are "video", "audio" or "subitle".
For [Warehouse](#warehouse) and building on its own provided examples: the type of the library of Alexandria could be library, of a personal computer could be hard drive or computer, of a cloud storage place could be cloud, web or cloud/web hard drive and of a external hard drive could be hard drive.
Making "library", hard drive" or "cloud storage" some examples of types for [Warehouse](#warehouse).

## Status
Global status object, used to show the status of any type of object.
Whe used with the [Media](#media) table some examples would be: "emitting", "returning", "ended", "canceled", "premiered", "released", etc.

## Platform
Any system outside of this program.
More specifically it refers to the place that holds the [ShareSite](#sharesite) site or information about a [Media](#media).
Though the [ShareSite](#sharesite) may not have a platform it is enclosed in.

For example:
If the [ShareSite](#sharesite) is a Telegram Channel its related [Platform](#platform) would be "Telegram".
On the other hand, if the [ShareSite](#sharesite) is a website the [Platform](#platform) would be null.
For [Media](#media) it is usually linked to information pages/services like imdb, tmdb or omdb.

It could be interesting to also link both [Group](#group) and [Issue](#issue) to this table aswell; but for now this is postponned since it can be deduced from the present arrangement.

## ShareSite
What medium/site is the [Media](#media) shared at, this [ShareSite](#sharesite) can have a platform (like "Telegram") or not (if it its own website).

For example:
If the [ShareSite](#sharesite) is a Telegram Channel its related [Platform](#platform) would be "Telegram".
On the other hand, if the [ShareSite](#sharesite) is a website the [Platform](#platform) would be null.

## ShareSiteSubs
Number of people that are subscribed on a particular [ShareSite](#sharesite).
This is its own table since the number its regularly updated and records of its previous value are kept.

## Codec
Property related to a [File](#file) track.
It gives information of what type of encoding it has.
Some examples are "h264", "ac3" or "subrip".

## Media
Any element of media like a movie, a tv show, a documentary, a band, a youtube channel etc.
The distinction of which type it is is made with the relationship with [Type](#type).

## Group
Intermedium grouping for [Media](#media) elements.
A perfect example for this is a tv show season, though its also used for things like a music album.

## Issue
Minimum entity separation a [Media](#media) can have.
They can also have a related [Group](#Group).
This can be an episode, a book chapter, a youtube video or even a song.

## Language
Spoken and written languages arround the world.

## Code
Represents what type of codes exist and with its relationship with other entities it assigns a code to each.
Right now only related with [Language](#language) but it can be extended in the future.
Examples os this can be "BCP 47", "ISO 639-3", "Glottolog" or "LCID".

## CodeName
All the different types of names a [Code](#code) can have.

## App
Application used for the creation of a [File](#file).

## Version
Specific version of an [App](#app) used in the creation of a [File](#file).

## File
Particular physical representation of the [Media](#media) or [Issue](#issue) saved in the database.
It can be composed of [tracks](#track).

## Track
Some [Files](#file) such as vídeos or audios have something called tracks.
These are simply smaller components of whose combination results in the specific [File](#file) that contains them.

For example, in a video [File](#file), some tracks could be the video image, its sound, a embedded image and a subtitle track.
In the case of a standard audio [File](#file), it would have one single track being the sound.

## Country
Contains states/nations that currently exist or existed in the past.

## Encoder
Information related to a [File](#file) creation.

One example of an encoder would be: "libebml v1.4.4 + libmatroska v1.7.1".

## Warehouse
Location where a [File](#file) is stored at.
This can be a physical or virtual, its [type](#warehousetype) will determine it.

Examples of this would be: The library of Alexandria, a personal computer, a cloud storage place or a external hard drive.

## MediaPoster
This table is thought to be used by graphical user interfaces to know where to get from images for showing in the user interface.

For example, what folder and file name to pull all the images of all the [medias](#media) to show in a list [medias](#media) screen.

## Extension
What extension do the files posses.
This is related to the tables [File](#file) and [Poster](#poster).

Some examples are: 'mkv', 'mp4', 'pdf', 'mp3', 'avi', 'png', 'gif', 'ogg', etc.

## Folder
Path of the folder that contains a [File](#file).
Using this information as well as the [Warehouse](#warehouse) one a file should be unequivocally traceable.
