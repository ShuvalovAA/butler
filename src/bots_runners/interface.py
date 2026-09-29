from typing import Protocol


class IBotRunner(Protocol):
    def __init__(self, creds, proxy_url, tmp_dir) -> None:
        ...

    async def run(self) -> None:
        ...

    def register_handlers_commands(self) -> None:
        ...
