# Gemini on Discord

[中文](README.md) | English

[![license](https://img.shields.io/pypi/l/ansicolortags.svg)](LICENSE)

## Intro
Typing `/chat`, and enter some message in `message`. You can easily talk to Gemini.

It can read images too. Just typing `/see`, attach an image file to `image`, and enter some text in `message` (optional). You can let AI react to your image. Note that this command has no memory function.


## Set up the project

### Create a virtual environment
I develop this project on Python [3.10.13](https://www.python.org/downloads/release/python-31012/).

Create a virtual environment in any ways, such as venv, conda..., whatever you want. Then execute this command in the environment.
```
pip install requirements.txt
```

### Obtaining APIs
1. Gemini API

    1. Go to [Google AI](https://ai.google.dev/).

    2. Click `Get API Key in Google AI Studio`.

    3. Agree terms of service, after that, go to `Google AI Studio`。

    4. Click `Get API Key` on the left, and then click `Create API key in new project`, copy the API key. If error *The caller does not have permission* comes out，see [StackOverflow](https://stackoverflow.com/questions/77762483/the-caller-does-not-have-permission-when-creating-api-key) I found.

2. Discord API

    1. Go to [Discord Developer](https://discord.com/developers/applications).

    2. Click `Application` on the left, and then click `New Application` on the upper right. Enter a name, and agree terms of service.

    3. Click `Bot` on the left, and then click `Add Bot` on the right.

    4. Slide down while you see `MESSAGE CONTENT INTENT`, check it.

    5. Slide up while you see `View Token` (`Reset Token` if you have already had one), click it and copy the API key.

### Execute
Create `.env` in the root directory of the project, and modify it like this
```
DISCORD_API_KEY = "Your Discord Bot Token"
GEMINI_API_KEY = "Your Gemini API key"
```
After that, execute `main.py`。

## Set up Discord Bot on your server
1. Go to [Discord Developer](https://discord.com/developers/applications).

2. Click `Application` on the left, choose the bot you just created.

3. Click `OAuth2` on the left, `URL Generator` should be underneath it, click it.

4. Check `bot` on `SCOPE`, Checking `Send Message` on `BOT PERMISSIONS` is basically enough. Check all options on column `TEXT PERMISSIONS` if you are not sure.

5. Slide up while you see `GENERATED URL`, copy this link and paste to your browser, and then add bot to your server.


## Set of commands

command | description
---|---
/chat| Typing `/chat` and enter message in `message`, send to `gemini-pro`.
/reset| Program will store your latest 10 conversation records, typing `/reset` to remove all of them.
/see| Typing `/see` and attach an image to `image`, entering message in `message` is optional, send to `gemini-pro-vision`.