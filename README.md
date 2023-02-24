[//]: # ( -*- coding: utf-8 -*- )
[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Autor:  	Ran# )
[//]: # (+ Creado: 	2023/01/04 21:56:10.000000 )
[//]: # (+ Editado:	2023/02/24 21:39:08.619115 )
[//]: # ( ---------------------------------------------------------------------- )

# media4
Manager for your own personal media library.\
Allows you to automatically add useful information about media files to a database and lets you manage your library and access information and stats regarding it.


## Index
- [Documentation](media/doc/index.md#documentation)
- [How to Start](#how-to-start)
- [Frequent Stuff](#frequent-stuff)
- [Code Features](#code-features)
- [Tasks](#tasks)
- [TODO](#todo)


## How to Start
1. You may copy the config.cnf file into a .cnf file and configure the options to your liking (if not, default config will be used).
2. Run the program executing the following:
    ```
    $ ./main.py
    ```

## Frequent Stuff
Information about common useful things

### About the .cnf file
If you comment any, the default (as shown) value will still be used.
You can not leave the right part of the parameter definition in blank, you either put something or delete it entirely.

## Code features
- Logging
- Configuration file

## Tasks
- [ ] Make Add Function for WarehouseType
- [ ] Make Add Function for Warehouse
- [ ] Make Add Function for ShareSiteType
- [ ] Make Add Function for ShareSite
- [ ] Make Make Telegram service
- [ ] Make MediaIssue not always have MediaGroup.

## TODO
- [ ] Make "info.py" a service.
- [ ] Make the CustomTKinter GUI.
- [ ] Allow inserting dates before year 0.
- [ ] Check if a date of an issue is in between the appropiate years according to its group/media
- [ ] Automatically update the subs of the Telegram ShareSites.
    - [ ] Make service to connect to the API of Telegram.
    - [ ] Use the service for updating the subs of ShareSite depending on Platform (use thread).
- [ ] Dont only show name on "MediaGroup"s since it can be null and number is more important anyways.
- [ ] Make less confusing what part of input you are in when a subinput is opened (insert media group of newly created media)
- [ ] Add authors (this is tricky because it would also imply, if done correctly, to add attributions).
