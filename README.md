
# 🌟 Profession Time Telegram Bot

A Kazakh-language Telegram bot built with love and purpose for a school competition, aimed at inspiring students in their career journeys. It delivers motivating, context-aware responses — both in text and voice — about the **"Profession Time"** program and the beloved teacher **Azhar Tanatovna**.

---

## 📖 Overview

This bot was developed to support a dedicated homeroom teacher by sharing meaningful, motivational information in Kazakh. Whether students are curious about professions, life paths, or Azhar Tanatovna herself, the bot is here to respond — thoughtfully and warmly.

---

## ✨ Features

* 🇰🇿 **Kazakh-Language Responses**
  Answers questions in Kazakh about "Profession Time", professions, and Azhar Tanatovna.

* ⏳ **Short & Inspiring Replies**
  Responses are designed to be motivational and last around 30–40 seconds.

* 🎙️ **Text-to-Speech Integration**
  Uses Facebook MMS-TTS to generate natural Kazakh voice messages.

* 🧠 **AI-Powered Intelligence**
  Powered by Google Gemini API to generate meaningful and context-aware answers.

* 📩 **Seamless Telegram Delivery**
  Sends both text and voice messages directly in Telegram chat.

---

## 🛠️ Tech Stack

| Component             | Purpose                                         |
| --------------------- | ----------------------------------------------- |
| **Python**            | Core programming language                       |
| `google-generativeai` | Integrates Gemini API for intelligent responses |
| `transformers`        | Uses MMS-TTS from Hugging Face for TTS          |
| `python-telegram-bot` | Handles Telegram bot communication              |
| `torch`, `scipy`      | Audio waveform processing for TTS               |

---

## 🚀 Setup

### 1. Install Dependencies

```bash
pip install google-generativeai python-telegram-bot transformers torch scipy
```

### 2. Configure API Keys

In your `main.py` file:

```python
gemini_api = "YOUR_GEMINI_API_KEY"
telegram_token = "YOUR_TELEGRAM_BOT_TOKEN"
```


### 3. Run the Bot

```bash
python main.py
```

---

## 📱 Usage

1. Open Telegram and start a chat with the bot.
2. Use `/start` to begin.
3. Ask about:

   * "Profession Time"
   * Any profession
   * Azhar Tanatovna (or anything else!)
4. Receive:

   * A short, warm motivational **text response**
   * A **Kazakh voice message** with the same content

---

## ⚠️ Notes

* 🕒 Built quickly for a school competition — focus was on core functionality.
* 🌐 TTS requires a stable internet connection and a preloaded MMS-TTS model.
* 🔒 Keep your API keys secure. Avoid hardcoding secrets in public repositories.

---

## 👩‍🎓 Author

Created by a passionate student to support their homeroom teacher’s mission and uplift fellow classmates.


---

## 📜 License

This project is for **educational purposes only** — designed to inspire, educate, and encourage exploration.


