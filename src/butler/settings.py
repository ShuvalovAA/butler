import tomllib
from dataclasses import dataclass
from pathlib import Path

from src.bots_runners.interface import IBotRunner

from ..bots_runners import BOT_REGISTRY
from .deserializers.base import check_mapping, check_str
from .types import AllowedBots


@dataclass
class Settings:
    bot_runner: IBotRunner
    proxy_url: str


def load_settings(path: Path) -> Settings:
    with open(path, "rb") as f:
        config_toml = check_mapping(tomllib.load(f))

    bot_type = AllowedBots(
        check_str(config_toml['bot_type'])
    )
    proxy_url = check_str(config_toml['proxy_url'])
    bot = BOT_REGISTRY[bot_type]
    bot_credetials = BOT_REGISTRY[bot_type].creds_class(
        **check_mapping(config_toml['bot_credetials'])
    )
    tmp_dir = Path(check_str(config_toml['proxy_url']))
    bot_runner = bot.runner_class(creds=bot_credetials, proxy_url=proxy_url, tmp_dir=tmp_dir)

    return Settings(bot_runner=bot_runner, proxy_url=proxy_url)
