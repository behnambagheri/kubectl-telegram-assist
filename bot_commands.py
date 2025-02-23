import telebot
from telebot import types
from config import Config, logger, Tlogger

Tlogger = Tlogger
hideBoard = types.ReplyKeyboardRemove()

bot = telebot.TeleBot(token=Config.BOT_TOKEN, parse_mode='HTML')

commands = {
    'menu': 'Explore bot options',
    'help': 'Information about available commands',
}

help_text = (
        "<b>📚 Available Commands and Features:</b>\n\n"
        "<b>Commands:</b>\n"
        "&#8226; <b>/menu</b> - Open the main menu for easy navigation.\n\n"
        "<b>Interactive Options:</b>\n"
        "&#8226; <b>Get ID</b> - Show your unique Telegram User ID.\n"
    )

# Help Command
@bot.message_handler(commands=['help'])
def command_help(message) -> None:

    general_buttons(message.chat.id, help_text)

# Menu Command
@bot.message_handler(commands=['help'])
def menu(message) -> None:
    first_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""
    user_id = message.from_user.id

    logger.info(f"User: {first_name} {last_name} - {user_id} requested the menu.")
    text = (
        "<b>Please choose an option:</b>"
    )
    general_buttons(message.chat.id, text)

# Menu Command
@bot.message_handler(commands=['get_id'])
def get_id(message) -> None:
    first_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""
    user_id = message.from_user.id
    user_name = message.from_user.username or ""
    cid = message.chat.id
    logger.info(f"User: {first_name} {last_name} - {user_id} requested the menu.")
    text = (
        f"<b>Your ID:</b> <u>{user_id}</u>\n"
        f"<b>Firstname:</b> <u>{first_name}</u>\n"
        f"<b>Lastname:</b> <u>{last_name}</u>\n"
        f"<b>Username:</b> <u>{user_name}</u>"
    )
    general_buttons(message.chat.id, text)


# Handle Other Messages
@bot.message_handler(func=lambda message: True)

def handle_messages(message):
    first_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""
    user_id = message.from_user.id
    user_name = message.from_user.username or ""
    cid = message.chat.id
    logger.debug(f"User: {first_name} {last_name} - {user_id}\n"
                f"Message ID: {cid}\n"
                f"Message: {message.text}")



    if message.text == "GetID":
        text = (
            f"<b>Your ID:</b> <u>{user_id}</u>\n"
            f"<b>Firstname:</b> <u>{first_name}</u>\n"
            f"<b>Lastname:</b> <u>{last_name}</u>\n"
            f"<b>Username:</b> <u>{user_name}</u>"
        )
        bot.send_chat_action(cid, "typing")
        general_buttons(cid, text)

    elif message.text == "Help":
        general_buttons(cid, help_text)
    else:
        logger.info(f"User: {first_name} {last_name} - {user_id} Invalid Command.")
        text = (
            "Invalid command. Please use /menu or /help for guidance.\n"
            "<b>Please choose an option:</b>"
        )
        general_buttons(cid, text)



def general_buttons(cid, note) -> None:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("GetID")
    item2 = types.KeyboardButton("Help")
    markup.add(item1, item2)
    bot.send_message(cid, note, reply_markup=markup)

