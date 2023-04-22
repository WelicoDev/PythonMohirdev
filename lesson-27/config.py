from transliterate import to_cyrillic , to_latin
import telebot

TOKEN ="6050198594:AAF6vyA3QbpaT7PTlk3uzN649KX_NvGN8dw"
bot = telebot.TeleBot(TOKEN , parse_mode=None)

@bot.message_handler(commands=[ 'start'])
def send_welcome(message):
    javob = "Assalom aleykum . Xush kelibsiz !\n"
    javob +=" Matn kiriting : >>  "

    bot.reply_to(message , javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = кlambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message ,javob(msg))

bot.polling()