#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/21 03:06:54.968132
#+ Editado:	2023/03/21 20:57:58.923041
# ------------------------------------------------------------------------------
from configobj import ConfigObj
from uteis.ficheiro import cargarJson as load_json
import os
import pathlib
from datetime import datetime

from src.enum import UIEnum
from src.exception import TableNameException, LanguageException, UserInterfaceException
# ------------------------------------------------------------------------------
class Config(object):
    """"""
    config_file: str = '.cnf'
    table_names_file: str = 'media/db/table_names.json'
    supported_languages_file: str = 'media/i18n/supported_languages.json'

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Config, self).__new__(self)

            # ts of program start
            self.program_start_ts = datetime.now()

            # importing file contents
            self.database_tables = load_json(self.table_names_file)
            self.supported_languages = load_json(self.supported_languages_file)
            self.file_content = ConfigObj(self.config_file)
            #

            ## setup of class attributes
            # language
            self.language = self.file_content.get('language', 'eng')
            # database
            self.populate_db = self.file_content.get('user_interface', 'true').capitalize()
            # folder locations
            self.i18n_folder = self.file_content.get('i18n_folder', 'media/i18n')
            self.log_folder = self.file_content.get('log_folder', 'media/logs')
            # database location
            self.database_file = self.file_content.get('db_file_location', 'media/db/Database.db')
            # services
            token = self.file_content.get('telegram_bot_token', None)
            self.telegram_bot_token = token if token != '' else None
            # ui
            self.ui = self.file_content.get('user_interface', 'terminal')
            # pagination
            self.pagination_limit = int(self.file_content.get('pagination_limit', 5))
            # terminal symbols
            self.title_symbol = self.file_content.get('title_symbol', '*')
            self.input_symbol = self.file_content.get('input_symbol', '>')
            self.option_title_symbol = self.file_content.get('option_title_symbol', '<')
            self.separator_symbol = self.file_content.get('separator_symbol', '-')
            self.error_symbol = self.file_content.get('error_symbol', '!!')
            self.add_symbol = self.file_content.get('add_symbol', '+')
            self.remove_symbol = self.file_content.get('remove_symbol', '-')
            self.equal_symbol = self.file_content.get('equal_symbol', '=')
            self.all_symbol = self.file_content.get('all_symbol', '*')
            ##

            # checking of the attributes
            if self.language not in self.supported_languages.keys():
                raise LanguageException(f'Language not supported yet, try: {self.supported_languages}')

            try:
                self.ui = UIEnum(self.ui)
            except ValueError:
                raise UserInterfaceException(f'User Interface not supported, try: {[o.value for o in UI]}')
            #

            # create folders
            for folder in [self.log_folder, pathlib.Path(self.database_file).parent]:
                os.makedirs(folder, exist_ok=True)

        return self.instance

    def get_table_name(self, table_name: str) -> str:
        """ Given a table name (as stated in the config file) it returns its actual name in the DB.
        """
        try:
            return self.database_tables[table_name]
        except KeyError:
            raise TableNameException(f'Table "{table_name}" does not exist in the config \
                    file "{Config().table_names_file}"')

    def get_num_entities(self) -> int:
        """ Returns the name of entity files created in the folder -2.
        The minus two is need in order to not keep count of the __init__.py
        and the base_entity.py files.

        """
        return len(next(os.walk('./src/model/entity/'))[2])-2

    def get_num_defined_tables_db(self) -> int:
        """
        """
        return len(self.database_tables)+1
# ------------------------------------------------------------------------------
