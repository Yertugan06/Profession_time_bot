import logging
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from transformers import VitsModel, AutoTokenizer
import torch
import scipy.io.wavfile
import uuid
import os


logging.basicConfig(level=logging.INFO)

gemini_api = ""
genai.configure(api_key=gemini_api)


try:
    tts_model = VitsModel.from_pretrained("facebook/mms-tts-kaz")
    tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-kaz")
except Exception as e:
    logging.error(f"MMS-TTS моделін жүктеу қатесі: {e}")
    raise

info_text = """
Мамандық тайм туралы: [«Мамандық тайм» бағдарламасы мектеп оқушыларына кәсіби бағытты анықтауға көмектесетін пайдалы жоба. Ол түрлі мамандықтарды тереңірек түсінуге және мансап таңдаудағы мифтерді жоюға бағытталған. Бағдарламаның күшті жағы – интерактивті формат: 11-сынып оқушылары спикер ретінде өз тәжірибелерімен, емтиханға дайындық, оқу орнын таңдау және мансаптық қадамдар туралы бөліседі. Ашық диалог пен талқылаулар оқушыларға сенімділік береді, ал өмірден алынған мысалдар ақпаратты есте қаларлық етеді. «Мамандық тайм» – ақпараттық шара ғана емес, оқушыларға саналы мансап таңдауға және шабыт алуға көмектесетін білім беру жобасы.]
Оналбекова Ажар Танатовна туралы: Оналбекова Ажар Танатовна — тәжірибелі, білікті және шабыттандырушы математика мұғалімі. Ол терең білімі, педагогикалық шеберлігі және жылы мінезі арқылы оқушылардың білімге қызығушылығын оятады. Ажар Танатовна қиын тақырыптарды түсінікті етіп жеткізеді, әр оқушыға жеке көңіл бөліп, сенімділік пен мотивация береді. Оның ерекшеліктері: ақылдылығы, мейірімділігі, кәсібилігі, инновациялық әдістері және шабыттандырушы мінезі. Ол — оқушыларға болашаққа сенімді қадам жасауға көмектесетін бағыттаушы тұлға.
"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Сәлеметсіз бе! 'Мамандық Time', 'Мамандықтар', 'Ажар Танатовна' туралы сұраңыз! 🌟")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    prompt = f"""
Сен қазақ тілінде жылы, шабыттандыратын көмекші боласың. Мына ақпаратты қолдан:
---
{info_text}
---
Пайдаланушы сұрағы: "{user_message}"
Қазақ тілінде мейірімді, анық әрі шабыттандыратын стильде жауап бер. Ең көп дегенде жауап ұзақтығы 30-40 сек болуы керек. Жауапты қазақ алфавитінің әріптерінен жауап бер. Сандарды әріппен жаз. 
"""
    try:
        model_gemini = genai.GenerativeModel('gemini-2.0-flash') 
        response = model_gemini.generate_content(prompt)
        bot_reply = response.text.strip()
    except Exception as e:
        logging.error(f"Gemini API қатесі: {e}")
        await update.message.reply_text("Қате шықты, сұрағыңызды қайта жіберіңіз!")
        return


    try:
        
        inputs = tokenizer(bot_reply, return_tensors="pt")
        with torch.no_grad():
            output = tts_model(**inputs).waveform

        filename = f"{uuid.uuid4().hex}.wav"
        scipy.io.wavfile.write(filename, rate=tts_model.config.sampling_rate, data=output.float().numpy().T)
    except Exception as e:
        logging.error(f"MMS-TTS қатесі: {e}")
        await update.message.reply_text("Дауыс жасауда қате шықты. Мәтінмен жауап беремін!")
        await update.message.reply_text(bot_reply)
        return


    try:
        await update.message.reply_text(bot_reply)
        with open(filename, 'rb') as voice_file:
            await update.message.reply_voice(voice_file)
        os.remove(filename)
    except Exception as e:
        logging.error(f"Telegram жіберу қатесі: {e}")
        await update.message.reply_text("Дауыс жіберуде қате шықты. Мәтінмен жауап беремін!")
        await update.message.reply_text(bot_reply)


def main():
    try:
        telegram_token = ""
        app = ApplicationBuilder().token(telegram_token).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        app.run_polling()
    except Exception as e:
        logging.error(f"Ботты іске қосу қатесі: {e}")
        raise

if __name__ == "__main__":
    main()