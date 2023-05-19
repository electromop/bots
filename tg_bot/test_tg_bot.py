import telebot
from telebot import types

API_TOKEN = "5658948785:AAGOBJfD3veVdc_dwCTRA0T0jB6QN0q5j-I"

bot = telebot.TeleBot(API_TOKEN)

bot.set_my_commands([
    telebot.types.BotCommand("/start", "Запуск бота")
    # telebot.types.BotCommand("/AI break", "Запуск искуственного интелекта")
])

text_1 = '🔥 Привет! Я твой персональный защитник от пожара! 🔥 \n\nМоя цель - обеспечить безопасность и защиту твоего бизнеса и быта, предлагая широкий выбор противопожарных товаров. Что бы ты ни искал - я всегда здесь, чтобы помочь тебе. \n\nС моей помощью ты сможешь: \n🔹 Получать актуальные новости и статьи о пожарной безопасности. \n🔹 Получать рекомендации по выбору и установке противопожарных товаров. \n🔹 Оформлять заказы и получать информацию о наличии товаров. \n🔹 Получать уведомления о специальных предложениях и скидках. \n\nНе трать время на поиск информации – просто задай мне свой вопрос, и я с радостью помогу тебе в решении любых вопросов, связанных с противопожарной защитой. Доверь свою безопасность профессионалу! Со мной ты всегда будешь в надежных руках. \n\nПоехали! 🚀'

def start_markup():
    markup = types.InlineKeyboardMarkup(row_width=2) #создаем клавиатуру, выставляем 2 кнопи в строке
    item1 = types.InlineKeyboardButton('Мой заказ', callback_data='order_question') #создаем кнопки, пишем текст, который в них будет и значение кол бека при нажатии на них
    item2 = types.InlineKeyboardButton('Актуальные новости', callback_data='news_question')
    item3 = types.InlineKeyboardButton('Каталог продуктов', callback_data='catalog_question')
    item4 = types.InlineKeyboardButton('Рекомендации', callback_data='recomendation_question')
    item5 = types.InlineKeyboardButton('Скидки и акции', callback_data='discounts_promotions_questions')
    item6 = types.InlineKeyboardButton('Мини-игра', callback_data='game_questions')
    markup.add(item1, item2, item3, item4, item5, item6)
    return markup


def news_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Новости про пожары', callback_data='order_option_1')
    item2 = types.InlineKeyboardButton('Новые законы', callback_data='product_question')
    item3 = types.InlineKeyboardButton('"В мире пожарников"', callback_data='delivery_question')
    item4 = types.InlineKeyboardButton('Случайная новость', callback_data='money_back_question')
    item5 = types.InlineKeyboardButton('Назад', callback_data='back_to_start')
    markup.add(item1, item2, item3, item4, item5)
    return markup


def order_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Статус заказа', callback_data='order_option_1')
    item2 = types.InlineKeyboardButton('Повторить заказ', callback_data='product_question')
    item3 = types.InlineKeyboardButton('Связаться с продавцом', callback_data='delivery_question')
    item4 = types.InlineKeyboardButton('Оформить возврат', callback_data='money_back_question')
    item5 = types.InlineKeyboardButton('Другой вопрос', callback_data='money_back_question')
    item6 = types.InlineKeyboardButton('Назад', callback_data='back_to_start')
    markup.add(item1, item2, item3, item4, item5, item6)
    return markup



def catalog_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Огнетушители', callback_data='order_question')
    item2 = types.InlineKeyboardButton('Пожарные краны  ', callback_data='product_question')
    item3 = types.InlineKeyboardButton('Пожарный инвентарь', callback_data='delivery_question')
    item4 = types.InlineKeyboardButton('Покрывала', callback_data='money_back_question')
    item5 = types.InlineKeyboardButton('Пожарные шкафы', callback_data='money_back_question')
    item6 = types.InlineKeyboardButton('Пожарные щиты', callback_data='money_back_question')
    item7 = types.InlineKeyboardButton('Противопожарные двери', callback_data='money_back_question')
    item8 = types.InlineKeyboardButton('Назад', callback_data='back_to_start')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
    return markup


def recomendation_markup():
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Тут', callback_data='order_question')
    item2 = types.InlineKeyboardButton('будут', callback_data='product_question')
    item3 = types.InlineKeyboardButton('рекомендации.', callback_data='delivery_question')
    item4 = types.InlineKeyboardButton('Поскольку их', callback_data='money_back_question')
    item5 = types.InlineKeyboardButton('очень много,', callback_data='back_to_start')
    item6 = types.InlineKeyboardButton('мы оставили', callback_data='back_to_start')
    item7 = types.InlineKeyboardButton('данный раздел', callback_data='back_to_start')
    item8 = types.InlineKeyboardButton('пока пустым.', callback_data='back_to_start')
    item9 = types.InlineKeyboardButton('Назад', callback_data='back_to_start')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
    return markup


def sales_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Акции по товарам', callback_data='order_question')
    item2 = types.InlineKeyboardButton('Акции по услугам', callback_data='product_question')
    item3 = types.InlineKeyboardButton('Назад', callback_data='back_to_start')
    markup.add(item1, item2, item3)
    return markup


# def option_order_1():
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     item1 = types.InlineKeyboardButton('Опция 1 по опции 1 заказа', callback_data='order_option_option_1')
#     item2 = types.InlineKeyboardButton('Опция 2 по опции 1 заказа', callback_data='order_option_option_2')
#     item5 = types.InlineKeyboardButton('Назад', callback_data='back_to_order')
#     markup.add(item1, item2,item5)
#     return markup



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 
                     text_1, 
                     reply_markup=start_markup())

@bot.callback_query_handler(func=lambda call:True)
def callback_start(call):
    if call.message:
        if call.data == 'order_question':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text= 'Выберите тему вашего вопроса по заказу:', 
                                  reply_markup=order_markup())
        elif call.data == 'news_question':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text= 'О чем почитаем сегодня: ', 
                                  reply_markup=news_markup())
        elif call.data == 'catalog_question':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text= 'Что вас интересует в мире пожарной-техники?', 
                                  reply_markup=catalog_markup())
        elif call.data == 'recomendation_question':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text= 'О каких методах правильной защиты вы бы хотели узнать?', 
                                  reply_markup=recomendation_markup())
        elif call.data == 'back_to_start':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text= text_1, 
                                  reply_markup=start_markup())
        elif call.data == 'discounts_promotions_questions':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text= 'Представляем вашему вниманию список наших акций: ', 
                                  reply_markup=sales_markup())
        # elif call.data == 'order_option_1':
        #     bot.edit_message_text(chat_id=call.message.chat.id, 
        #                           message_id=call.message.id, 
        #                           text= 'Выберите подопцию', 
        #                           reply_markup=option_order_1())

bot.infinity_polling(timeout=10, long_polling_timeout=5)
