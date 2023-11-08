from secret import token
import telebot
from telebot import types

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("OZON", url='https://www.ozon.ru/seller/my-style-1228186/products/?miniapp=seller_1228186')
    button2 = types.InlineKeyboardButton("АВИТО", url='https://www.avito.ru')
    markup.add(button1, button2)
    # то что увижу я
    print("У меня начался рабочий день!")
    user_sms = f'<b>Добро пожаловать <i><u>{message.from_user.first_name}</u></i>! ' \
               f'В нашем Телеграм боте, вы узнаете где можно приобретсти наш товар!</b>'
    # то что увидит пользователь
    bot.send_message(
        message.chat.id,
        user_sms,
        parse_mode='html',
        reply_markup=markup)



@bot.message_handler()
def user_text(message):
    print('Болтаем.')
    if message.text == 'Привет':
        bot.send_message(
            message.chat.id,
            'Привет!',
            parse_mode='html', )
    else:
        bot.send_message(
            message.chat.id,
            'Прости, я тебя не понимаю!',
            parse_mode='html', )


bot.polling(none_stop=True)

