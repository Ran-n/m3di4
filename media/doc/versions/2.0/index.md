[//]: # ( -*- coding: utf-8 -*- )
[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Autor:  	Ran# )
[//]: # (+ Creado: 	2023/02/24 15:59:53.402052 )
[//]: # (+ Editado:	2023/03/24 17:56:12.932997 )
[//]: # ( ---------------------------------------------------------------------- )

[↩️](../index.md#versions)

# Media4 2.0

First proper iteration of the program and first version where actually the name Media4 is used.
The name changed from Media 3 to 4 since the database was recreated entirely.

## Index
- [Changelog](#changelog)
- [To Done](#to-done)

## Changelog
Since 2023-02-24 (started keeping track)
Until

- Created DB as improvement of previous one.
- Created Diagrams.
- Created DB creation script.
- Created DB insertion script.
- Created basic MVC program structure.
- Created i18n tables for the DB.
- Created app string translations.
- Added automatic adding file and tracks information to the DB.
- Created terminal UI.
- Created graphical UI.

## To Done
- [X] Remake the insert media option and add other options.
- [X] Migrate the app language everywhere in the code into english.
- [X] Add in platform id for ShareSite table.
- [X] Create new NK for ShareSite table.
- [X] Make Add function for Platform elements.
- [X] Make a simplified version of the diagrams
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
- [X] Add active field to all tables that benefit from it.
    - [X] Add the active flag to all i18n primary tables.
    - [X] Encoder
    - [X] CodecType
    - [X] LanguageCode
    - [X] Language
    - [X] Extension
- [X] Automatically update the subs of the Telegram ShareSites.
    - [X] Make Add Function for ShareSiteType
    - [X] Make Add Function for ShareSite
    - [X] Make service to connect to the API of Telegram.
    - [X] Use the service for updating the subs of ShareSite depending on Platform (use thread).
- [X] Automatically add all information about a File.
    - [X] Make Add Function for WarehouseType
    - [X] Make Add Function for Warehouse
    - [X] Make "info.py" a service.
- [X] Add a root/original/ur language to the language table. (For example American's English ur language would be English and english would not have an ur language.)
- [X] Made a global type and status tables instead of one for each element.
- [X] Entertain the idea of summing up Platform and Web tables.
- [X] Fix terminal view so that it doesnt assume that adding a single file means its a media, it can be an issue.
- [X] Make Groups and Issues able to have a related Poster too.
