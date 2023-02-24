[//]: # ( -*- coding: utf-8 -*- )
[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Autor:  	Ran# )
[//]: # (+ Creado: 	2023/02/24 15:59:53.402052 )
[//]: # (+ Editado:	2023/02/24 21:27:37.052189 )
[//]: # ( ---------------------------------------------------------------------- )

[↩️](../index.md#versions)

# Media4 2.0

First proper iteration of the program and first version where actually the name Media4 is used.
The name changed from Media 3 to 4 since the database was recreated entirely.

## Index
- [Changelog](#changelog)
- [Tasks Done](#tasks-done)

## Changelog
Since 2023-02-24 (started keeping track)
Until

- Created DB as improvement of previous one.
- Created Diagrams.
- Created DB creation script.
- Created DB insertion script.
- Created basic MVC program structure.
- Created i18n tables for the DB.

## Tasks Done
- [X] Add in platform id for ShareSite table.
- [X] Create new NK for ShareSite table.
- [X] Make Add function for Platform elements.
- [X] Separate/Make the i18n tables into Name and/or Description.
    - [X] LanguageName
    - [X] Platform
    - [X] ShareSiteType
    - [X] ShareSite
    - [X] Warehouse
    - [X] WarehouseType
    - [X] Media, MediaGroup & MediaIssue
    - [X] Country
    - [X] CodecType
    - [X] Codec
    - [X] MediaType
    - [X] MediaStatus
    - [X] Web (Description)
    - [X] Code (Description)
    - [X] Extension (Description)
    - [X] Encoder (Description)
    - [X] App (Description)
    - [X] AppVersion (Description)
- [X] Move the active attribute just below the id one.
- [X] Add the active flag to all i18n primary tables.
