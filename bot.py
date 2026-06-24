import telebot
from telebot import types
import requests

# هذا هو التوكن الخاص بك كما طلبته
BOT_TOKEN = "8837023232:AAHnHHJplPJRFdJovdilrF_oewUYP7FQAHc"
SIM_API_KEY = "EyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE4MTM3OTkwMTMsImlhdCI6MTc4MjI2MzAxMywicmF5IjoiMjc3N2QwNzI5YmUyY2E3Yzg4N2Y3MDI1NzA0MzRmY2UiLCJzdWIiOjQyNDcyOTB9.w7F7enP2N6lz0Qv2s_QUYZfz_PzkB8Yh0ju_wPB1QTox9vM3bsDpB6qt2YjwReBER-7jGVp7_bvvoJPUCD5jA7UxBYvUNZ1M0El2w8gjtcdjW4eajsPVsW6aiMeif2QABPk7NMnDRgPOtSqEtQQdD1u-MxoGq-e6e9o3fe7lZV-zWR7WinStnRxOkbtkuJPI4Wrrd378b0YwIdyxd6W_uJgvf67GoNi0IWqXUJt3zGrnVec7UmJOP-eIG4Bpr4VVrAQLOTcFRjGdntbFxIBCKyo1IJw6W-FWZD54mJNUoidPHh-eDN7ZC42BUeKaRfxCgSiBuVkVipP2UvD9MENh9Q"
SUPPORT_USER = "@Smsteleteam"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("🛒 شراء أرقام", "💳 شحن الرصيد", "🎧 الدعم الفني")
    bot.send_message(message.chat.id, "أهلاً بك! البوت يعمل الآن بكامل طاقته.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_menu(message):
    if message.text == "💳 شحن الرصيد":
        bot.send_message(message.chat.id, "🆔 ID Cwallet: `91552675`\nارسل الـ TXID للمراجعة.", parse_mode="Markdown")
    
    elif message.text == "🛒 شراء أرقام":
        bot.send_message(message.chat.id, "جاري الاتصال بـ 5Sim...")
        try:
            res = requests.get("https://5sim.net/v1/user/prices?product=telegram", 
                               headers={'Authorization': f'Bearer {SIM_API_KEY}'}, timeout=10)
            bot.send_message(message.chat.id, f"✅ تم الاتصال. حالة السيرفر: {res.status_code}")
        except Exception as e:
            bot.send_message(message.chat.id, f"❌ فشل الاتصال: {e}")

    elif message.text == "🎧 الدعم الفني":
        bot.send_message(message.chat.id, f"تواصل مع: {SUPPORT_USER}")

if __name__ == "__main__":
    bot.polling(none_stop=True)
