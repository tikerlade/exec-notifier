import argparse
import configparser
import os
import subprocess
import sys
from datetime import datetime

import requests

POST_URL = "https://notifier-publisher.herokuapp.com/send_message"
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../config.ini")


def send_result(arguments, start_time, end_time, return_code, text):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    chat_id = config["telegram"]["telegram_id"]

    title = "Success" if return_code == 0 else "Error"
    command = " ".join(arguments)
    execution_time = end_time - start_time
    message = f"*{title}* \nCommand: `{command}` \nExecution time: `{execution_time}` \n\nLog output will be below."

    data = {"chat_id": chat_id, "text": message, "file_text": text}

    with open("log.txt", "w") as fout:
        fout.write(text)

    files = {"log.txt": open("log.txt", "rb")}

    requests.post(POST_URL, data=data, files=files)


def notify(arguments):

    start_time = datetime.today()
    result = subprocess.run(arguments, shell=True, capture_output=True)
    end_time = datetime.today()

    return_code = result.returncode
    if return_code == 0:
        text = result.stdout.decode("utf-8")
    else:
        text = result.stderr.decode("utf-8") or result.stdout.decode("utf-8")

    send_result(arguments, start_time, end_time, return_code, text)


def config(arguments):
    config = configparser.ConfigParser()
    config["telegram"] = {"telegram_id": arguments.telegram_id}

    with open(CONFIG_FILE, "w") as fout:
        config.write(fout)


def check_config():
    # Initialize config parser
    config = configparser.ConfigParser()

    # Check that config file exists
    if not os.path.isfile(CONFIG_FILE):
        return False

    config.read(CONFIG_FILE)

    # Check telegram field in config
    if "telegram" not in config:
        return False

    telegram_config = config["telegram"]
    if "telegram_id" not in telegram_config:
        return False

    return True


def parse_args(args: list):
    # Initialize parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Configure parser for config mode
    config_parser = subparsers.add_parser("config")
    config_parser.add_argument(
        "--telegram_id",
        help="Your telegram_id. You can get it from @userinfobot bot.",
        type=str,
        required=True,
    )
    config_parser.set_defaults(mode="config")

    # Configure parser for notify mode
    notify_parser = subparsers.add_parser("notify")
    notify_parser.set_defaults(mode="notify")

    return parser.parse_known_args(args)


def run_from_args(known_args, unknown_args):
    if known_args.mode == "config":
        config(known_args)
    elif known_args.mode == "notify":
        if check_config():
            notify(unknown_args)
        else:
            raise FileNotFoundError("You have not configured the tool.")


def main():
    # Parse arguments from CLI
    arguments = parse_args(sys.argv[1:])
    known, unknown = arguments

    # Run program with given arguments
    run_from_args(known, unknown)


if __name__ == "__main__":
    main()
