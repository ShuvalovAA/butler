from io import BytesIO
from typing import Protocol


class ITranscriptor(Protocol):
    async def transcribe(self, audio: BytesIO) -> str: ...
