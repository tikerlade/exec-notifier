import os

from emoji import emojize
from telegram.ext import CommandHandler, Updater

# General information
TELEGRAM_TOKEN = str(os.getenv("TELEGRAM_TOKEN"))
HEROKU_URL = str(os.getenv("HEROKU_URL"))
PORT = int(os.environ.get("PORT", "88"))


def start(update, context):
    chat_id = update.effective_chat.id
    respond_text = f"Hey :waving_hand:, your ID is: `{chat_id}`"

    context.bot.send_message(chat_id, text=emojize(respond_text), parse_mode="Markdown")


def main():
    updater = Updater(token=TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    # Start receiving updates
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TELEGRAM_TOKEN)
    updater.bot.set_webhook(HEROKU_URL + TELEGRAM_TOKEN)

    # Close listener when it's necessary
    updater.idle()


if __name__ == "__main__":
    # Run the main part of the program
    main()
