#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/25 16:47:35.526685
#+ Editado:	2023/02/25 20:54:28.849299
# ------------------------------------------------------------------------------
import aiohttp
import logging
import asyncio
from typing import Union, List

from src.utils import Config
from src.exception import WrongChatIdTypeException
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
class TelegramService:
    """"""
    base_url: str = 'https://api.telegram.org/'

    def __init__(self):
        logging.info(_(f'Starting the TelegramService with bot_token=\
                {Config().telegram_bot_token}'))
        self.bot_token = Config().telegram_bot_token
        self.url = self.base_url + f'bot{self.bot_token}/'

    async def get_chat_members(self, chat_id: str) -> Union[int, None]:
        logging.info(_(f'Getting chat members count on chat_id={chat_id}'))
        if self.bot_token is None:
            logging.info(_(f'Exiting operation because bot token is not set'))
            return None

        local_url = self.url + 'getChatMembersCount?chat_id='
        if isinstance(chat_id, str):
            if chat_id.isdigit():
                local_url += '-100'
            else:
                local_url += '@'
        else:
            logging.error(_('The chat_id={chat_id} provided is not a str.'))
            raise WrongChatIdTypeException()
        local_url += chat_id

        async with aiohttp.ClientSession() as session:
            async with session.get(local_url) as response:
                value = await response.json()
        try:
            return value['result']
        except KeyError:
            return None

    async def get_many_chat_members(self, chat_ids: List[str]) ->\
            List[Union[int, None]]:
        """"""
        logging.info(_(f'Getting chat members count on multiple chat_ids'))
        if not isinstance(chat_ids, list):
            chat_ids = [chat_ids]
        return await asyncio.gather(*[self.get_chat_members(chat_id) for chat_id in chat_ids])
# ------------------------------------------------------------------------------
