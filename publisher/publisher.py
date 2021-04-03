import logging
import os

from flask import Flask, request
from telegram.bot import Bot

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

app = Flask(__name__)
bot = Bot(TELEGRAM_TOKEN)

logging.basicConfig(level=logging.INFO)


@app.route("/send_message", methods=["POST"])
def send_message():
    print(request)
    data = request.form
    logging.info(f"Data received {data}")
    print(f"Data received {data}")

    chat_id = data["chat_id"]
    text_information = data["text"]

    bot.send_message(chat_id=chat_id, text=text_information, parse_mode="Markdown")
    bot.send_document(chat_id=chat_id, document=request.files["log.txt"])

    return "Success"
