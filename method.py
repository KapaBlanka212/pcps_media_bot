import re
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

import constnats as CONST
from logger_control import setup_logger

"""
UNIT: FUCTION
~~~~~~~~~~~~~
    In block of code bellow are described all nessessary functions for Polina tg bot.
"""

logger = setup_logger(CONST.METHODS_LOGGER_NAME, CONST.METHODS_LOGGER_FILE)

async def handle_text(update: Update, context: CallbackContext) -> None:
    user_text = update.message.text
    await update.message.reply_text(f"Вы написали: {user_text}")


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Привет! Я новый и очень крутой бот-анонсер для чата медиа отдела PCPS.")


def sanitize_input(input_text: str) -> str:
    sanitized_text = re.sub(r'[^\w\s@]', '', input_text)
    return sanitized_text.strip()

def escape_markdown(text):
    escape_chars = r'\*_`['
    return ''.join(f'\\{char}' if char in escape_chars else char for char in text)

# Асинхронный метод для отправки сообщения в группу
async def send_to_chat_group(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    message_thread_id = update.message.message_thread_id
    group_name = sanitize_input(context.args[0].upper())
    message = sanitize_input(' '.join(context.args[1:]))
    
    if group_name in CONST.GROUPS:
        tagged_users = ' '.join([f'{user}' for user in CONST.GROUPS[group_name]])
        full_message = escape_markdown(f'{message} {tagged_users}')
        
        if message_thread_id:
            await context.bot.send_message(chat_id=chat_id, text=full_message, parse_mode=ParseMode.MARKDOWN, message_thread_id=message_thread_id)
        else:
            await context.bot.send_message(chat_id=chat_id, text=full_message, parse_mode=ParseMode.MARKDOWN)
    else:
        await update.message.reply_text(CONST.MSG_GROUP_NOT_EXIST.format(group_name=group_name))


async def get_chat_and_thread_id(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    message_thread_id = update.message.message_thread_id
    await update.message.reply_text(f"Chat ID: {chat_id}\nThread ID: {message_thread_id}")


def restricted_access(func):
    async def wrapper(update: Update, context: CallbackContext) -> None:
        allowed_users = ['NIKI']
        user = update.message.from_user
        if user.username not in allowed_users:
            await update.message.reply_text(CONST.MSG_NO_ACCESS)
            return
        return await func(update, context)
    return wrapper
