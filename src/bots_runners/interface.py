from typing import Protocol


class IBotRunner(Protocol):
    async def run(self) -> None:
        ...

    def register_handlers_commands(self) -> None:
        ...
