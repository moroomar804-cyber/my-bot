hereimport telebot

TOKEN = '8837023232:AAFloK7HfJ-IqPsH5ZHNXhItGZxhEZjDxVE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "البوت يعمل الآن!")

if __name__ == "__main__":
    print("البوت يعمل الآن...")
    bot.infinity_polling(none_stop=True, interval=0, timeout=20)
