from collections.abc import Mapping, Sequence
from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from attr import dataclass

if TYPE_CHECKING:
    from bots_runners.interface import IBotRunner

type Toml = (
    str |
    int |
    float |
    bool |
    datetime |
    Sequence["Toml"] |
    Mapping[str, "Toml"]
)


class AllowedBots(str, Enum):
    TELEGRAMM = 'telegram'


@dataclass
class TelegramCredetials:
    token: str


type Creds = TelegramCredetials


@dataclass(frozen=True)
class BotRegystred:
    runner_class: type["IBotRunner"]
    creds_class: type[Creds]
