from io import BytesIO
from aiogram.types import Message
from src.transcriptors.interface import ITranscriptor
from aiogram import Bot


async def cmd_start(message: Message) -> None:
    await message.answer("Привет! Я асинхронный Telegram-бот.")


async def echo(message: Message) -> None:
    await message.answer(f"Ты написал: {message.text}")


async def handle_voice(
    message: Message,
    transcriptor: ITranscriptor
) -> None:
    # await message.answer("Ты отправил голосовое сообщение")
    bot = message.bot
    media = message.voice or message.audio
    if media is None:
        await message.answer("Пришли голосовое сообщение 🎤")
        return

    duration = media.duration or 0
    if duration > 10:
        await message.answer(
            f"⏱ Максимум {10} сек., а у тебя {duration}."
        )
        return

    status = await message.answer("🎤 Распознаю...")

    file = await bot.get_file(media.file_id)
    buffer = BytesIO()
    await bot.download_file(file.file_path, destination=buffer)
    buffer.seek(0)

    try:
        text = await transcriptor.transcribe(buffer)
    except Exception as e:
        await status.edit_text(f"❌ Ошибка: {e}")
        return

    await status.edit_text(f"🎤 «{text}»" if text else "🤷 Не разобрал")
