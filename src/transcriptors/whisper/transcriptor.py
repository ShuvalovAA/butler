import os
import asyncio
import tempfile
from io import BytesIO
from pathlib import Path
from typing import override

import whisper
import imageio_ffmpeg

from src.transcriptors.interface import ITranscriptor


class WhisperTranscriptor(ITranscriptor):
    def __init__(self, model_size: str = "base", language: str = "ru") -> None:
        # создаём директорию для симлинка и самого tmp
        self.tmp_dir: Path = Path("/home/tomy/reps/butler/tmp") # TODO: почистить
        bin_dir = self.tmp_dir / "bin"
        bin_dir.mkdir(parents=True, exist_ok=True)

        ffmpeg_link = bin_dir / "ffmpeg"
        if not ffmpeg_link.exists():
            ffmpeg_link.symlink_to(imageio_ffmpeg.get_ffmpeg_exe())

        os.environ["PATH"] = str(bin_dir) + os.pathsep + os.environ.get("PATH", "")

        self._model = whisper.load_model(model_size)
        self._language = language

    @override
    async def transcribe(self, audio: BytesIO) -> str:
        return await asyncio.to_thread(self._transcribe_sync, audio)

    def _transcribe_sync(self, audio: BytesIO) -> str:
        with tempfile.NamedTemporaryFile(
            suffix=".oga",
            dir=self.tmp_dir,
            delete=False,
        ) as tmp:
            tmp.write(audio.getvalue())
            tmp_path = tmp.name

        try:
            result = self._model.transcribe(tmp_path, language=self._language)
            return result.get("text", "").strip()
        finally:
            os.unlink(tmp_path)