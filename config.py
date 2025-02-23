import os
from dotenv import load_dotenv
import logging
import telebot
from typing import List, Dict, Optional

load_dotenv()

class Config:
    """
    Centralized configuration management for environment variables.
    """

    BOT_TOKEN: str = os.getenv('BOT_TOKEN')
    USE_PROXY: bool = os.getenv('USE_PROXY').lower()
    PROXY: str = os.getenv('PROXY')
    USE_CUSTOM_API: bool = os.getenv('USE_CUSTOM_API').lower()
    CUSTOM_API: str = os.getenv('CUSTOM_API')
    DEBUG: bool = os.getenv('DEBUG', 'false').lower() == 'true'
    BOT_DEBUG: bool = os.getenv('BOT_DEBUG', 'false').lower() == 'true'

    full_access_users: Dict[str, List[Dict[str, str | int]]] = {}
    disconnect_users: Dict[str, List[Dict[str, str | int]]] = {}

    required_vars: List[str] = [
        'USE_PROXY',
        'PROXY',
        'USE_CUSTOM_API',
        'CUSTOM_API',
    ]

    @classmethod
    def validate(cls) -> None:
        """
        Ensures all critical environment variables are set.
        Raises an error if any required variable is missing.
        """
        missing_vars = [var for var in cls.required_vars if not getattr(cls, var)]
        if missing_vars:
            raise EnvironmentError(f'Missing required variable: {', '.join(missing_vars)}')

logging.basicConfig(
    level=logging.DEBUG if Config.DEBUG else logging.INFO,

    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        # logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)

class Tlogger:
    if Config.BOT_DEBUG:
        telebot.logger.setLevel(logging.DEBUG)
        # telebot.logger.setLevel(logging.INFO)
    else:
        telebot.logger.setLevel(logging.INFO)

logger = logging.getLogger("TelegramBot")
Config.validate()
