from telebot import apihelper
from bot_commands import *


if Config.USE_PROXY == "true":
    apihelper.proxy = {'http': f'{Config.PROXY}'}
    logger.info("Proxy enabled and configured.")
if Config.USE_CUSTOM_API == "true":
    apihelper.API_URL = f"{Config.CUSTOM_API}/bot{{0}}/{{1}}"
    logger.info("Custom API URL set.")
logger.info("Bot successfully initialized.")


# logger.info("Starting the bot...")
bot.infinity_polling()