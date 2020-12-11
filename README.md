# Welcome to the EasyBot!
Easy bot is a simple solution for making a Discord bot with Python

Currently this is version v0.6

## Get started

First, download the files inside a directory
Install python3 and libraries
`pip3 install json discord`

## Creating bot

Create an application on discord developer portal https://discord.com/developers/applications
Activate bot functionality and copy the secret token, paste it inside `token.txt`

## Configuring the bot

Open `commands.json` and program your bot
`DebugType`: Nothing for now
`NotFoundError`: If the user writes a command that doesn't exist, the bot will say this

`Commands`: All commands

Start the bot with `python3 main.py`
