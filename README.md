Profession Time Telegram Bot
Overview
A Telegram bot created quickly for a school competition to support a homeroom teacher. It provides info about the "Profession Time" program and teacher Azhar Tanatovna, answering in Kazakh with text and voice.
Features

Answers in Kazakh about "Profession Time," professions, or Azhar Tanatovna.
Short, inspiring responses (30-40 seconds).
Text-to-speech using Facebook MMS-TTS.
Powered by Google Gemini API.
Sends text and voice messages via Telegram.

Tech Stack

Python
google-generativeai (Gemini API)
transformers (MMS-TTS)
python-telegram-bot
torch & scipy

Setup

Install dependencies:pip install google-generativeai python-telegram-bot transformers torch scipy


Add API keys:
gemini_api: Google Gemini API key
telegram_token: Telegram bot token


Run:python bot.py



Usage

Start bot with /start.
Ask about "Profession Time," professions, or Azhar Tanatovna.
Get text and voice replies.

Notes

Built quickly for a school event.
Voice synthesis depends on internet and MMS-TTS.
Keep API keys secure.

Author
Created by a student for a school competition.
License
For educational use only.
