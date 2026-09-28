from typing import override

from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command

from pytest import Session
from src.butler.types import TelegramCredetials

from ..interface import IBotRunner
from .commands import cmd_start, echo


class TelegramBotRunner(IBotRunner):
    def __init__(
        self,
        creds: TelegramCredetials,
        proxy_url: str
    ) -> None:
        self._creds = creds
        session = AiohttpSession(proxy=proxy_url)
        self._bot = Bot(token=creds.token, session=session)
        self._dispatcher = Dispatcher()
        self._register_handlers()

    def _register_handlers(self) -> None:
        router = Router()
        router.message.register(cmd_start, Command("start"))
        router.message.register(echo)
        self._dispatcher.include_router(router)

    @override
    async def run(self) -> None:
        try:
            await self._dispatcher.start_polling(self._bot)
        finally:
            await self._bot.session.close()
