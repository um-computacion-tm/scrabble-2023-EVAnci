#!/usr/bin/env bash

if [ ! -f "/usr/local/bin/codeclimate" ]
then
	curl -L https://github.com/codeclimate/codeclimate/archive/master.tar.gz | tar xvz -C /home/$USER/
	(cd /home/$USER/codeclimate-* && sudo make install)
	codeclimate engines:install
fi

coverage run -m unittest && coverage report -m
codeclimate analyze
