[//]: # ( -*- coding: utf-8 -*- )
[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Autor:  	Ran# )
[//]: # (+ Creado: 	2023/02/12 15:28:24.413478 )
[//]: # (+ Editado:	2023/02/15 23:04:42.114422 )
[//]: # ( ---------------------------------------------------------------------- )

# Tables

Explanation of what each table of the database was designed to contain.

## Index
- [Platform](#platform)
- [ShareSite](#sharesite)

## Platform

Refers to the place that holds the ShareSite site.
The ShareSite may not have a platform it is enclosed in.

For example:
If the "ShareSite" is a Telegram Channel its related "Platform" would be "Telegram".
On the other hand, if the "ShareSite" is a website the "Platform" would be null.

## ShareSite

What medium/site is the media shared at, this "ShareSite" can have a platform (like "Telegram") or not (if it its own website).

For example:
If the "ShareSite" is a Telegram Channel its related "Platform" would be "Telegram".
On the other hand, if the "ShareSite" is a website the "Platform" would be null.
