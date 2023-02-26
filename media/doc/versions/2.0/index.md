[//]: # ( -*- coding: utf-8 -*- )
[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Autor:  	Ran# )
[//]: # (+ Creado: 	2023/02/24 15:59:53.402052 )
[//]: # (+ Editado:	2023/02/26 15:25:34.083621 )
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
