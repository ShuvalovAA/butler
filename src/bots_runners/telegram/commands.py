from aiogram.types import Message


async def cmd_start(message: Message) -> None:
    await message.answer("Привет! Я асинхронный Telegram-бот.")


async def echo(message: Message) -> None:
    await message.answer(f"Ты написал: {message.text}")
