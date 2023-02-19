[//]: # ( -*- coding: utf-8 -*- )
[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Autor:  	Ran# )
[//]: # (+ Creado: 	2023/02/12 15:28:24.413478 )
[//]: # (+ Editado:	2023/02/19 12:39:39.673176 )
[//]: # ( ---------------------------------------------------------------------- )

# Tables

Explanation of what each table of the database was designed to contain.

## Index
- [Platform](#platform)
- [ShareSite](#sharesite)
- [Codec](#codec)
- [CodecType](#codectype)

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
