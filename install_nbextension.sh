#!/bin/sh

mkdir -p $(jupyter --data-dir)/nbextensions/exec_notifier

curl -L https://raw.githubusercontent.com/tikerlade/exec-notifier/master/nbextension/exec_notifier.js > $(jupyter --data-dir)/nbextensions/exec_notifier/exec_notifier.js
curl -L https://raw.githubusercontent.com/tikerlade/exec-notifier/master/nbextension/exec_notifier.yaml > $(jupyter --data-dir)/nbextensions/exec_notifier/exec_notifier.yaml
curl -L https://raw.githubusercontent.com/tikerlade/exec-notifier/master/nbextension/README.md > $(jupyter --data-dir)/nbextensions/exec_notifier/README.md
curl -L https://raw.githubusercontent.com/tikerlade/exec-notifier/master/nbextension/bot_report.png > $(jupyter --data-dir)/nbextensions/exec_notifier/bot_report.png
