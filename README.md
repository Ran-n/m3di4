# media4

Program for automatically adding useful information about media files to a database.
Allows you to manage a personal library and access information and stats regarding it.


## Index

- [How to Start](#how-to-start)
- [Frequent Stuff](#frequent-stuff)
- [TODO](#todo)


## How to Start

1. Copy the config.cnf file into a .cnf file and configure the options to your liking.


## Frequent Stuff

Information about common useful things

### About the .cnf file

If you comment any, the default (as shown) value will still be used.
You can not leave the right part of the parameter definition in blank, you either put something or delete it entirely.


## TODO

- [ ] Finalize the migration to MVC by refactoring all of the "insertar" code and adding the missing code in the terminal view strategy.
- [ ] Move the "info.py" and make it a service withing the program and not part of the controller.
- [ ] Add a GUI as part of the view strategies.
- [ ] Add a config option to set the strategies to use in the program.
- [ ] Add more options into the program as so you can, for example, insert into an already existing media or edit information.
- [ ] Migrate the app language everywhere in the code into english.
- [ ] Create several language options for the views.
