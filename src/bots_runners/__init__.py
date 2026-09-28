from collections.abc import Mapping

from src.bots_runners.telegram import TelegramBot
from src.butler.types import AllowedBots, BotRegystred

BOT_REGISTRY: Mapping[AllowedBots, BotRegystred] = {
    AllowedBots.TELEGRAMM: TelegramBot
}
