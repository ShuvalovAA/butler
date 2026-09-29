from pathlib import Path
from typing import override

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters import Command

from src.butler.types import TelegramCredetials

from ..interface import IBotRunner
from .commands import cmd_start, handle_voice
from src.transcriptors.whisper.transcriptor import WhisperTranscriptor

class TelegramBotRunner(IBotRunner):
    def __init__(
        self,
        creds: TelegramCredetials,
        proxy_url: str,
        tmp_dir: Path
    ) -> None:
        self._creds = creds
        session = AiohttpSession(proxy=proxy_url)
        self._bot = Bot(token=creds.token, session=session)
        self._dispatcher = Dispatcher()
        self._dispatcher.workflow_data["transcriptor"] = WhisperTranscriptor(tmp_dir=tmp_dir)
        self._register_handlers()

    def _register_handlers(self) -> None:
        router = Router()
        router.message.register(cmd_start, Command("start"))
        router.message.register(handle_voice, F.voice | F.audio )
        self._dispatcher.include_router(router)

    @override
    async def run(self) -> None:
        try:
            await self._dispatcher.start_polling(self._bot)
        finally:
            await self._bot.session.close()
