# Notifier
[![PyPI](https://img.shields.io/pypi/v/exec-notifier)](https://pypi.org/project/exec-notifier/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Actions Status](https://github.com/tikerlade/exec-notifier/workflows/deploy_publisher.yml/badge.svg)](https://github.com/tikerlade/exec-notifier/actions/)

This tool provides you ability to send yourself information about looong executed command when it is done. Information will be sent using Telegram Bot, which you can generate for yourself with Telegram BotFather.

## Prerequisites
In execution of your application you will need your Telegram ID. To get it visit [@exec_notifier_bot](https://telegram.me/exec_notifier_bot) and use `/start` command.

## Installation and running
```shell
>>> pip install exec-notifier
>>> exec_notifier config --telegram_id=YOUR_TELEGRAM_ID
>>> exec_notifier notify [your_command_here]
```
