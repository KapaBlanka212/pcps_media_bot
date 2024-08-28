"""
Developed with love by Nick(@NikiKostr) for PCPS Media telegramm group
"""
import logging
import os
from dotenv import load_dotenv
from telegram.ext import Application, MessageHandler, CommandHandler
import telegram.ext.filters as filters

from method import restricted_access, start, send_to_chat_group, handle_text, get_chat_and_thread_id

"""
UNIT: TOKENS
~~~~~~~~~~~~
"""

load_dotenv()
TOKEN = os.getenv('YOUR_TOKEN')


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", restricted_access(start)))
    application.add_handler(CommandHandler("send_to_group", restricted_access(send_to_chat_group)))
    application.add_handler(CommandHandler("get_chat_and_thread_id", restricted_access(get_chat_and_thread_id)))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    try:
        application.run_polling()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
