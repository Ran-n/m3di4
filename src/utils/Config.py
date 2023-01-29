#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/21 03:06:54.968132
#+ Editado:	2023/01/29 00:35:03.357591
# ------------------------------------------------------------------------------
from uteis.ficheiro import cargarJson as load_json
import os
import pathlib

from src.exception.exception import TableNameException
# ------------------------------------------------------------------------------
class Config(object):
    file: str = '.cnf'

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Config, self).__new__(self)

            self.file_content = load_json(self.file)

            self.language = self.file_content.get('language', '')
            self.i18n_folder = self.file_content.get('internationalization_folder', '')
            self.log_folder = self.file_content.get('log_folder', '')
            self.database_file = self.file_content.get('db_file_location', '')
            self.database_tables = self.file_content.get('db_table_names', '')

            for folder in [self.log_folder, pathlib.Path(self.database_file).parent]:
                os.makedirs(folder, exist_ok=True)

        return self.instance

    def get_table_name(self, table_name: str) -> str:
        """
        Given a table name (as stated in the config file) it returns its actual name in the DB.
        """
        try:
            return self.database_tables[table_name]
        except KeyError:
            raise TableNameException(f'Table "{table_name}" does not exist in the config file "{Config().file}"')

    def get_num_entities(self) -> int:
        """
        """
        return len(next(os.walk('./src/model/entity/'))[2])-1

    def get_num_defined_tables_db(self) -> int:
        """
        """
        return len(self.database_tables)+1
# ------------------------------------------------------------------------------
