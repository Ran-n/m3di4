[//]: # ( -*- coding: utf-8 -*- )
[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Autor:  	Ran# )
[//]: # (+ Creado: 	2023/01/04 21:56:10.000000 )
[//]: # (+ Editado:	2023/02/19 12:30:49.057894 )
[//]: # ( ---------------------------------------------------------------------- )

# media4

Manager for your own personal media library.\
Allows you to automatically add useful information about media files to a database and lets you manage your library and access information and stats regarding it.


## Index

- [How to Start](#how-to-start)
- [Frequent Stuff](#frequent-stuff)
- [Code Features](#code-features)
- [Documentation](media/doc/index.md#documentation)
- [Tasks](#tasks)
- [TODO](#todo)


## How to Start

1. Copy the config.cnf file into a .cnf file and configure the options to your liking.


## Frequent Stuff

Information about common useful things

### About the .cnf file

If you comment any, the default (as shown) value will still be used.
You can not leave the right part of the parameter definition in blank, you either put something or delete it entirely.

## Code features

- Logging
- Configuration file

## Tasks

- [ ] Make a simplified version of the diagrams
- [X] Add in platform id for sharesite table
- [X] Create new NK for ShareSite table
- [ ] Make Add Function for WarehouseType
- [ ] Make Add Function for Warehouse
- [ ] Make Add Function for ShareSiteType
- [ ] Make Add Function for ShareSite
- [X] Make Add Function for Platform
- [ ] Make Make Telegram service
- [ ] Automatically use the Telegram service for updating the subs of sharesite depending on platform (use thread)
- [ ] Separate/Make the i18n tables into Name and/or Description.
    - [X] LanguageName
    - [X] Platform
    - [X] ShareSiteType
    - [X] ShareSite
    - [X] Warehouse
    - [X] WarehouseType
    - [X] Media, MediaGroup & MediaIssue
    - [X] Country
    - [X] CodecType
    - [ ] Codec
    - [ ] MediaType
    - [ ] MediaStatus

## TODO

- [ ] Make "info.py" a service.
- [ ] Make the CustomTKinter GUI.
- [ ] Remake the insert media option and add other options.
- [ ] Migrate the app language everywhere in the code into english.
- [ ] Allow inserting dates before year 0.
- [ ] Check if a date of an issue is in between the appropiate years according to its group/media
- [ ] Automatically update the subs of the Telegram ShareSites.
- [ ] Dont only show name on groups since it can be null and number is more important anyways.
- [ ] Make less confusing what part of input you are in when a subinput is opened (insert media group of newly created media)
