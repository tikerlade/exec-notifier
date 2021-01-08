import os

from flask import Flask, request
from telegram.bot import Bot

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

app = Flask(__name__)
bot = Bot(TELEGRAM_TOKEN)


@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.json
    file = request.files
    print(data)

    chat_id = data["chat_id"]
    text_information = data["text"]
    file = file["log.txt"]

    bot.send_message(chat_id=chat_id, text=text_information, parse_mode="Markdown")
    bot.send_document(chat_id=chat_id, document=file)

    return "Success"
