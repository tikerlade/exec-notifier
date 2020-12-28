import argparse
import configparser
import os
import subprocess
from datetime import datetime

import requests

POST_URL = "https://notifier-publisher.herokuapp.com/send_message"


def send_result(arguments, start_time, end_time, return_code, text):
    config = configparser.ConfigParser()
    config.read("config.ini")

    chat_id = config["telegram"]["telegram_id"]

    title = "Success" if return_code == 0 else "Error"
    command = " ".join(arguments)
    execution_time = end_time - start_time
    message = f"*{title}* \nCommand: `{command}` \nExecution time: `{execution_time}` \n\nLog output will be below."

    data = {"chat_id": chat_id, "text": message, "file_text": text}

    requests.post(POST_URL, json=data)


def notify(arguments):

    start_time = datetime.today()
    result = subprocess.run(arguments, shell=True, capture_output=True)
    end_time = datetime.today()

    return_code = result.returncode
    if return_code == 0:
        text = result.stdout.decode("utf-8")
    else:
        text = result.stderr.decode("utf-8")

    send_result(arguments, start_time, end_time, return_code, text)


def config(arguments):
    config = configparser.ConfigParser()
    config["telegram"] = {"telegram_id": arguments.telegram_id}

    with open("config.ini", "w") as fout:
        config.write(fout)


def check_config():
    config = configparser.ConfigParser()

    if not os.path.isfile("config.ini"):
        return False

    config.read("config.ini")

    if "telegram" not in config:
        return False

    telegram_config = config["telegram"]
    if "telegram_id" not in telegram_config:
        return False

    return True


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    config_parser = subparsers.add_parser("config")
    config_parser.add_argument(
        "--telegram_id",
        help="Your telegram_id. You can get it from @userinfobot bot.",
        type=str,
        required=True,
    )
    config_parser.set_defaults(mode="config")

    notify_parser = subparsers.add_parser("notify")
    notify_parser.set_defaults(mode="notify")

    known, unknown = parser.parse_known_args()
    if known.mode == "config":
        config(known)
    elif known.mode == "notify":
        if check_config():
            notify(unknown)
        else:
            raise FileNotFoundError("You have not configured the tool.")


if __name__ == "__main__":
    main()
