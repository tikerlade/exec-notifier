<h1> <img align="center" width="64" height="64" src="https://habrastorage.org/webt/x8/jn/ao/x8jnaoprxwqpopluc_oldypk284.png"> Execution Notifier </h1>

[![PyPI](https://img.shields.io/pypi/v/exec-notifier)](https://pypi.org/project/exec-notifier/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Actions Status](https://github.com/tikerlade/exec-notifier/workflows/Deploy%20Bot/badge.svg)](https://github.com/tikerlade/exec-notifier/actions/)
[![Actions Status](https://github.com/tikerlade/exec-notifier/workflows/Release%20to%20PyPI/badge.svg)](https://github.com/tikerlade/exec-notifier/actions/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/tikerlade/exec-notifier/master.svg)](https://results.pre-commit.ci/latest/github/tikerlade/exec-notifier/master)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/exec-notifier)

This tool provides you ability to send yourself information about looong executed command when it is done. Information will be sent using Telegram Bot. Logs and error messages (if they'll occur) will be delivered too.

If your log will be too long (longer 1_000_000 signs we'll not send it).

## Prerequisites

1. Python 3.4 or higher
2. Telegram ID - get it from [@exec_notifier_bot](https://telegram.me/exec_notifier_bot) by using `/start` command.

## Installation and running
You need to run your commands in quotes(`""`) when passing script to run.

```shell
>>> pip install exec-notifier
>>> exec_notifier config --telegram_id=YOUR_TELEGRAM_ID
>>> exec_notifier notify "[your_command_here]"
```

## Examples

```shell
>>> exec_notifier notify "ls -l | head"
>>> exec_notifier notify "ls -l > output.txt"
>>> exec_notifier notify "ls -l && sleep 3 && ps"
>>> exec_notifier notify "zip Downloads"
```

## Future
* Your own bot support will be added
