#!/usr/bin/env bash

pip install --quiet pipenv
pipenv install --dev
pipenv check
pipenv shell  # use `exit` to end the session
echo "use 'exit' to deactivate this pipenv virtualenv"
