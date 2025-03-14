# WaifuList bot

this is a bot that will help you manage your waifu list, this is a game from telegram

## Table of contents

- [WaifuList bot](#waifulist-bot)
	- [Table of contents](#table-of-contents)
	- [How to install](#how-to-install)
		- [EVN](#evn)
		- [Create venv](#create-venv)
		- [Use venv](#use-venv)
		- [install dependencies with pip](#install-dependencies-with-pip)
		- [Run bot](#run-bot)
		- [Stop bot](#stop-bot)
		- [Deactivate venv](#deactivate-venv)

## How to install

### EVN

	cp .env.example .env

edit .env file and add your telegram token

### Create venv

	python3 -m venv .{env_name}

### Use venv

	source .{env_name}/bin/activated

### install dependencies with pip

	pip install -r requirements.txt

### Run bot
if make install in your system use the next commands:

	make start
	or
	make dev

if make is not installed in your system use the next commands:

	python3 main.py
	or
	python3 -m jurigged -v main.py

### Stop bot

	Ctrl+C

### Deactivate venv

	deactivate



