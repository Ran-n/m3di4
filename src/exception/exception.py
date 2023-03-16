#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/21 03:45:01.530694
#+ Editado:	2023/03/12 22:10:18.186780
# ------------------------------------------------------------------------------
class TableNameException(Exception):
    pass

class LanguageException(Exception):
    pass

class UserInterfaceException(Exception):
    pass

class InheritException(Exception):
    pass

class WrongChatIdTypeException(Exception):
    pass

class UnknownLanguageException(Exception):
    """Raised exception when a language tag of a stream is not in the database"""
    def __init__(self, codename):
        super().__init__(f'The language code "{codename}" is not save in ' +
                'the database. Contact an admin for it to be added, you can ' +
                'also add it yourself if you have the SQL knowledge.')
# ------------------------------------------------------------------------------
