import telebot
from telebot import types

API_TOKEN = "5658948785:AAGOBJfD3veVdc_dwCTRA0T0jB6QN0q5j-I"

bot = telebot.TeleBot(API_TOKEN)

bot.set_my_commands([
    telebot.types.BotCommand("/start", "Запуск бота"),
])


def start_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Вопрос по заказу', callback_data='order_question')
    item2 = types.InlineKeyboardButton('Вопрос по товару', callback_data='product_question')
    item3 = types.InlineKeyboardButton('Вопрос по доставке', callback_data='delivery_question')
    item4 = types.InlineKeyboardButton('Вопрос по возврату', callback_data='money_back_question')
    markup.add(item1, item2, item3, item4)
    return markup



def order_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Опция 1 по заказу', callback_data='order_question')
    item2 = types.InlineKeyboardButton('Опция 2 по заказу', callback_data='product_question')
    item3 = types.InlineKeyboardButton('Опция 3 по заказу', callback_data='delivery_question')
    item4 = types.InlineKeyboardButton('Опция 4 по заказу', callback_data='money_back_question')
    item5 = types.InlineKeyboardButton('Назад', callback_data='back_to_start')
    markup.add(item1, item2, item3, item4, item5)
    return markup



def product_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Опция 1 по товару', callback_data='order_question')
    item2 = types.InlineKeyboardButton('Опция 2 по товару', callback_data='product_question')
    item3 = types.InlineKeyboardButton('Опция 3 по товару', callback_data='delivery_question')
    item4 = types.InlineKeyboardButton('Опция 4 по товару', callback_data='money_back_question')
    item5 = types.InlineKeyboardButton('Назад', callback_data='back_to_start')
    markup.add(item1, item2, item3, item4, item5)
    return markup


def delivery_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Опция 1 по доставке', callback_data='order_question')
    item2 = types.InlineKeyboardButton('Опция 2 по доставке', callback_data='product_question')
    item3 = types.InlineKeyboardButton('Опция 3 по доставке', callback_data='delivery_question')
    item4 = types.InlineKeyboardButton('Опция 4 по доставке', callback_data='money_back_question')
    item5 = types.InlineKeyboardButton('Назад', callback_data='back_to_start')
    markup.add(item1, item2, item3, item4, item5)
    return markup


def money_back_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Опция 1 по возврату', callback_data='order_question')
    item2 = types.InlineKeyboardButton('Опция 2 по возврату', callback_data='product_question')
    item3 = types.InlineKeyboardButton('Опция 3 по возврату', callback_data='delivery_question')
    item4 = types.InlineKeyboardButton('Опция 4 по возврату', callback_data='money_back_question')
    item5 = types.InlineKeyboardButton('Назад', callback_data='back_to_start')
    markup.add(item1, item2, item3, item4, item5)
    return markup




@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 
                     'Здравствуйте, я ваш онлайн помощник! Ниже выберите тему вашего вопроса.', 
                     reply_markup=start_markup())

@bot.callback_query_handler(func=lambda call:True)
def callback_start(call):
    if call.message:
        if call.data == 'order_question':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text= 'Выберите тему вашего вопроса по заказу:', 
                                  reply_markup=order_markup())
        elif call.data == 'product_question':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text= 'Выберите тему вашего вопроса по товару:', 
                                  reply_markup=product_markup())
        elif call.data == 'delivery_question':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text= 'Выберите тему вашего вопроса по доставке:', 
                                  reply_markup=delivery_markup())
        elif call.data == 'money_back_question':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text= 'Выберите тему вашего вопроса по возврату:', 
                                  reply_markup=money_back_markup())
        elif call.data == 'back_to_start':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text= 'Здравствуйте, я ваш онлайн помощник! Ниже выберите тему вашего вопроса.', 
                                  reply_markup=start_markup())

bot.infinity_polling(timeout=10, long_polling_timeout=5)
