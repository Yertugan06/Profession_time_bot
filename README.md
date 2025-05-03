🌟 Profession Time Telegram Bot
📖 Overview
This Telegram bot was crafted with care for a school competition to support a dedicated homeroom teacher. It shares inspiring information about the "Profession Time" program and the remarkable teacher Azhar Tanatovna, delivering responses in Kazakh through both text and voice. Built swiftly yet thoughtfully, it aims to motivate students in their career exploration journey.
✨ Features

🇰🇿 Kazakh-language responses about "Profession Time," professions, or Azhar Tanatovna.
⏳ Short & inspiring replies (30-40 seconds) to spark motivation.
🎙️ Text-to-speech powered by Facebook MMS-TTS for natural Kazakh voice output.
🧠 AI-driven answers using Google Gemini API for meaningful, context-aware responses.
📩 Text and voice messages delivered seamlessly via Telegram.

🛠️ Tech Stack

Python: Core programming language.
google-generativeai: Integrates Gemini API for intelligent responses.
transformers (Hugging Face): Enables MMS-TTS for Kazakh voice synthesis.
python-telegram-bot: Powers smooth Telegram interactions.
torch & scipy: Supports audio processing and waveform generation.

🚀 Setup

Install Dependencies:pip install google-generativeai python-telegram-bot transformers torch scipy


Configure API Keys:
Set gemini_api with your Google Gemini API key in bot.py.
Set telegram_token with your Telegram bot token in bot.py.


Run the Bot:python bot.py



📱 Usage

Open Telegram and start the bot with /start.
Ask about "Profession Time", professions, or Azhar Tanatovna(indeed it can answer anything).
Receive a warm, inspiring response in text and a Kazakh voice message.

⚠️ Notes

🕒 Created rapidly for a school competition, prioritizing functionality.
🌐 Voice synthesis requires a stable internet connection and MMS-TTS model.
🔒 Secure your API keys: Avoid sharing gemini_api or telegram_token publicly. Consider using a .env file with .gitignore.

👩‍🎓 Author
Proudly created by a student to support their homeroom teacher’s vision in a school competition.
📜 License
This project is for educational purposes only, designed to inspire and educate.

Empowering students to dream big, one conversation at a time. 🌟
