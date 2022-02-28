import telebot 
import wildber
bot = telebot.TeleBot('5107243266:AAGCPndiARlwga4h3Bg4gHD6WLYagO1KFUY')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет! Выбери одну из комманд")
    bot.send_message(message.chat.id,"/get_brand")
    bot.send_message(message.chat.id,"/get_title")

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/get_brand':
        bot.send_message(message.from_user.id, "Отправь артикул товара для получения названия бренда")
        bot.register_next_step_handler(message, brand)
    elif message.text == '/get_title':
        bot.send_message(message.from_user.id, "Отправь артикул товара для получения названия товара")
        bot.register_next_step_handler(message, title)
    else:
        bot.send_message(message.chat.id,"Выбери /get_brand или /get_title")

def brand(message):
    art = message.text
    if art.isdigit():
        url = 'https://www.wildberries.ru/catalog/' + str(art) + '/detail.aspx'
        inf = wildber.parser(url, 1)
        bot.send_message(message.from_user.id, 'Наименование бренда - "' + str(inf) + '"')
        bot.send_message(message.from_user.id, 'Нажмите /start, чтобы начать сначала')
    else:
        bot.send_message(message.from_user.id, 'Неверный артикул! Нажмите /start, чтобы начать сначала')
    
def title(message):
    art = message.text
    if art.isdigit():
        url = 'https://www.wildberries.ru/catalog/' + str(art) + '/detail.aspx'
        inf = wildber.parser(url, 2)
        bot.send_message(message.from_user.id, 'Наименование товара - "' + str(inf) + '"')
        bot.send_message(message.from_user.id, 'Нажмите /start, чтобы начать сначала')
    else:
        bot.send_message(message.from_user.id, 'Неверный артикул! Нажмите /start, чтобы начать сначала')

bot.infinity_polling()