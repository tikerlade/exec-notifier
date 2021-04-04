#!/bin/sh

mkdir -p $(jupyter --data-dir)/nbextensions/exec_notifier

curl -LJO https://github.com/tikerlade/exec-notifier/tree/master/nbextension/exec_notifier.js > $(jupyter --data-dir)/nbextensions/exec_notifier/exec_notifier.js
curl -LJO https://github.com/tikerlade/exec-notifier/tree/master/nbextension/exec_notifier.yaml > $(jupyter --data-dir)/nbextensions/exec_notifier/exec_notifier.yaml
curl -LJO https://github.com/tikerlade/exec-notifier/tree/master/nbextension/README.md > $(jupyter --data-dir)/nbextensions/exec_notifier/README.md
