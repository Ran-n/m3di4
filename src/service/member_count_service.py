#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/25 20:53:07.340161
#+ Editado:	2023/02/25 22:46:11.632895
# ------------------------------------------------------------------------------
import logging
import asyncio
from typing import List

from src.service import TelegramService
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
class MemberCountService:
    """"""

    def __init__(self):
        logging.info(_(f'Starting the MemberCountService'))

    def run(self, chats: dict[List[str]]) -> dict[List[int]]:
        logging.info(_(f'Running the counting of members of each ShareSite'))

        chats['telegram'] = asyncio.run(TelegramService().get_many_chat_members(chats['telegram']))

        return chats
# ------------------------------------------------------------------------------
