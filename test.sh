#!/usr/bin/env bash

docker_status=$(systemctl status docker | awk 'NR==2 {print $4}' | sed 's/;//g')
if [ "$docker_status" = "disabled" ]; then
	systemctl start docker
fi

if [ ! -f "/usr/local/bin/codeclimate" ]; then
	curl -L https://github.com/codeclimate/codeclimate/archive/master.tar.gz | tar xvz -C /home/$USER/
	(cd /home/$USER/codeclimate-* && sudo make install)
	codeclimate engines:install
fi

coverage run -m unittest && coverage report -m
codeclimate analyze
