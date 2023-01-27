#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/21 03:06:54.968132
#+ Editado:	2023/01/23 18:23:00.943154
# ------------------------------------------------------------------------------
from uteis.ficheiro import cargarJson

from src.exception.exception import TableNameException
# ------------------------------------------------------------------------------
class Config(object):
    file: str = '.cnf'

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Config, self).__new__(self)

            self.file_content = cargarJson(self.file)
            self.database_file = self.file_content.get('db_file_location', '')
            self.database_tables = self.file_content.get('db_table_names', '')

        return self.instance

    def get_table_name(self, table_name: str) -> str:
        """
        Given a table name (as stated in the config file) it returns its actual name in the DB.
        """
        try:
            return self.database_tables[table_name]
        except KeyError:
            raise TableNameException(f'Table "{table_name}" does not exist in the config file "{Config().file}"')
# ------------------------------------------------------------------------------
