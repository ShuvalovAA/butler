import asyncio
import os
from pathlib import Path

from .settings import load_settings


async def main():
    settings = load_settings(
        path=Path(os.environ['CONFIG_FILE_PATH'])
    )

    await settings.bot_runner.run()


if __name__ == '__main__':
    asyncio.run(main())
