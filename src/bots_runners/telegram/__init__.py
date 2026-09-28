from src.bots_runners.telegram.implementations import (
    TelegramBotRunner,
    TelegramCredetials,
)
from src.butler.types import BotRegystred

TelegramBot = BotRegystred(
    runner_class=TelegramBotRunner,
    creds_class=TelegramCredetials
)
