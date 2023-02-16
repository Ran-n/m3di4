#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/12 13:46:42.274532
#+ Editado:	2023/02/16 23:36:26.666878
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, WarehouseTypeName, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class WarehouseTypeNameLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('WarehouseTypeNameLanguage'))
    warehouse_type_name: WarehouseTypeName
    language: Language
    id_: Optional[int] = field(default=None)
    added_ts: Optional[str] = field(default=None)
    modified_ts: Optional[str] = field(default=None)
# ------------------------------------------------------------------------------
