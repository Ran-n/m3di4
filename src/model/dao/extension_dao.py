#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/04/05 16:41:53.055819
#+ Editado:	2023/04/05 17:30:22.582010
# ------------------------------------------------------------------------------
from src.model import iModel

from src.model.entity import Extension
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
class ExtensionDAO:
    """Data Access Object"""

    def __new__(self, model: iModel):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
            self.instance.model = model
        return self.instance

    def save(self, extension: Extension) -> Extension:
        """Saving an DAO object"""
        if not self.model.exists(extension):
            self.model.insert(extension)
        return self.model.get_by_name(table_name=Extension.table_name,
                                      name=extension.name)
# ------------------------------------------------------------------------------
