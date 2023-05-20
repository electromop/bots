import telebot
from telebot import types

API_TOKEN = "5658948785:AAGOBJfD3veVdc_dwCTRA0T0jB6QN0q5j-I"

bot = telebot.TeleBot(API_TOKEN)

bot.set_my_commands([
    telebot.types.BotCommand("/start", "Запуск бота")
    # telebot.types.BotCommand("/AI break", "Запуск искуственного интелекта")
    ])

text_main_menu = '🔥 Привет! Я твой персональный защитник от пожара! 🔥 \n\nМоя цель - обеспечить безопасность и защиту твоего бизнеса и быта, предлагая широкий выбор противопожарных товаров. Что бы ты ни искал - я всегда здесь, чтобы помочь тебе. \n\nС моей помощью ты сможешь: \n🔹 Получать актуальные новости и статьи о пожарной безопасности. \n🔹 Получать рекомендации по выбору и установке противопожарных товаров. \n🔹 Оформлять заказы и получать информацию о наличии товаров. \n🔹 Получать уведомления о специальных предложениях и скидках. \n\nНе трать время на поиск информации – просто задай мне свой вопрос, и я с радостью помогу тебе в решении любых вопросов, связанных с противопожарной защитой. Доверь свою безопасность профессионалу! Со мной ты всегда будешь в надежных руках. \n\nПоехали! 🚀'

text_news = {'news1': 'wildfire', 'news2': 'laws', 'news3': 'fireman', 'news4': 'random'}
text_order = {'order1': 'status', 'order2': 'repeat', 'order3': 'seller', 'order4': 'money_back', 'order5': 'another'}
text_recomendation = {'rec1': 'recomendation1', 'rec2': 'recomendation2', 'rec3': 'recomendation3'}
text_catalog = {'catalog1': 'extinguisher', 'catalog2': 'fire_cranes', 'catalog3': 'fire_inventory', 'catalog4': 'bedspreads', 'catalog5': 'fire_cabinets', 'catalog6': 'fire_shields'}
text_sales = {'sales1': 'product_promotions', 'sales2': 'promotions_services'}
prev_step = ['back_to_start', 'second_option']

def start_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Мой заказ', callback_data='order_question') 
    item2 = types.InlineKeyboardButton('Актуальные новости', callback_data='news_question')
    item3 = types.InlineKeyboardButton('Каталог продуктов', callback_data='catalog_question')
    item4 = types.InlineKeyboardButton('Рекомендации', callback_data='recomendation_question')
    item5 = types.InlineKeyboardButton('Скидки и акции', callback_data='discounts_promotions_questions')
    item6 = types.InlineKeyboardButton('Мини-игра', callback_data='game_questions')
    markup.add(item1, item2, item3, item4, item5, item6)
    return markup


def news_markup():
    markup = types.InlineKeyboardMarkup(row_width=4)
    item1 = types.InlineKeyboardButton('Новости про пожары', callback_data=text_news.get('news1'))
    item2 = types.InlineKeyboardButton('Новые законы', callback_data=text_news.get('news2'))
    item3 = types.InlineKeyboardButton('"В мире пожарников"', callback_data=text_news.get('news3'))
    item4 = types.InlineKeyboardButton('Случайная новость', callback_data=text_news.get('news4'))
    item5 = types.InlineKeyboardButton('Назад', callback_data='back')
    item6 = types.InlineKeyboardButton('На главное меню', callback_data='back_to_start')
    markup.add(item1, item2, item3, item4, item5, item6)
    return markup


def order_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Статус заказа', callback_data=text_order.get('order1'))
    item2 = types.InlineKeyboardButton('Повторить заказ', callback_data=text_order.get('order2'))
    item3 = types.InlineKeyboardButton('Связаться с продавцом', callback_data=text_order.get('order3'))
    item4 = types.InlineKeyboardButton('Оформить возврат', callback_data=text_order.get('order4'))
    item5 = types.InlineKeyboardButton('Другой вопрос', callback_data=text_order.get('order5'))
    item6 = types.InlineKeyboardButton('Назад', callback_data='back')
    item7 = types.InlineKeyboardButton('На главное меню', callback_data='back_to_start')
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    return markup



def catalog_markup():
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Огнетушители', callback_data=text_catalog.get('catalog1'))
    item2 = types.InlineKeyboardButton('Пожарные краны  ', callback_data=text_catalog.get('catalog2'))
    item3 = types.InlineKeyboardButton('Пожарный инвентарь', callback_data=text_catalog.get('catalog3'))
    item4 = types.InlineKeyboardButton('Покрывала', callback_data=text_catalog.get('catalog4'))
    item5 = types.InlineKeyboardButton('Пожарные шкафы', callback_data=text_catalog.get('catalog5'))
    item6 = types.InlineKeyboardButton('Пожарные щиты', callback_data=text_catalog.get('catalog6'))
    item7 = types.InlineKeyboardButton('Назад', callback_data='back')
    item8 = types.InlineKeyboardButton('На главное меню', callback_data='back_to_start')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
    return markup


def recomendation_markup():
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Рекомендация №1', callback_data=text_recomendation.get('rec1'))
    item2 = types.InlineKeyboardButton('Рекомендация №2', callback_data=text_recomendation.get('rec2'))
    item3 = types.InlineKeyboardButton('Назад', callback_data='back')
    item4 = types.InlineKeyboardButton('На главное меню', callback_data='back_to_start')
    markup.add(item1, item2, item3, item4)
    return markup


def sales_markup():
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Акции по товарам', callback_data=text_sales.get('sales1'))
    item2 = types.InlineKeyboardButton('Акции по услугам', callback_data=text_sales.get('sales2'))
    item3 = types.InlineKeyboardButton('Назад', callback_data='back')
    item4 = types.InlineKeyboardButton('На главное меню', callback_data='back_to_start')
    markup.add(item1, item2, item3, item4)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 
                     text_main_menu, 
                     reply_markup=start_markup())

@bot.callback_query_handler(func=lambda call:True)
def callback_start(call):
    if call.message:
        if call.data == 'back':
            call.data = prev_step[0]
            print(call.data)
        if call.data == 'order_question':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text= 'Выберите тему вашего вопроса по заказу:', 
                                reply_markup=order_markup())
            prev_step[1] = 'order_question'
        elif call.data == 'news_question':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text= 'О чем почитаем сегодня: ', 
                                reply_markup=news_markup())
            prev_step[1] = 'news_question'
        elif call.data == 'catalog_question':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text= 'Что вас интересует в мире пожарной-техники?', 
                                reply_markup=catalog_markup())
            prev_step[1] = 'catalog_question'
        elif call.data == 'recomendation_question':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text= 'О каких методах правильной защиты вы бы хотели узнать?', 
                                reply_markup=recomendation_markup())
            prev_step[1] = 'recomendation_question'
        elif call.data == 'discounts_promotions_questions':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text= 'Представляем вашему вниманию список наших акций: ', 
                                reply_markup=sales_markup())
            prev_step[1] = 'discounts_promotions_questions'
        elif call.data == 'back_to_start':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.id, 
                                text= text_main_menu, 
                                reply_markup=start_markup())
            prev_step[1] = 'back_to_start'


bot.infinity_polling(timeout=10, long_polling_timeout=5)
