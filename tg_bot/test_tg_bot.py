import telebot
from telebot import types
import psycopg2
from psycopg2 import Error

API_TOKEN = "5658948785:AAGOBJfD3veVdc_dwCTRA0T0jB6QN0q5j-I"

bot = telebot.TeleBot(API_TOKEN)

bot.set_my_commands([
    telebot.types.BotCommand("/start", "Запуск бота"),
    telebot.types.BotCommand("/ai_break", "Запуск искуственного интелекта"),
    telebot.types.BotCommand("/support", "Запуск меню поддержки клиентов")
    ])

text_main_menu = '🔥 Привет! Я твой персональный защитник от пожара! 🔥 \n\nМоя цель - обеспечить безопасность и защиту твоего бизнеса и быта, предлагая широкий выбор противопожарных товаров. Что бы ты ни искал - я всегда здесь, чтобы помочь тебе. \n\nС моей помощью ты сможешь: \n🔹 Получать актуальные новости и статьи о пожарной безопасности. \n🔹 Получать рекомендации по выбору и установке противопожарных товаров. \n🔹 Оформлять заказы и получать информацию о наличии товаров. \n🔹 Получать уведомления о специальных предложениях и скидках. \n\nНе трать время на поиск информации – просто задай мне свой вопрос, и я с радостью помогу тебе в решении любых вопросов, связанных с противопожарной защитой. Доверь свою безопасность профессионалу! Со мной ты всегда будешь в надежных руках. \n\nПоехали! 🚀'

text_client_help = 'Добро пожаловать в наш чат поддержки клиентов! Мы рады приветствовать вас и готовы помочь вам решить любые вопросы или проблемы, с которыми вы столкнулись. \n\nМы понимаем, что каждый клиент уникален и имеет свои индивидуальные потребности. Поэтому наш чат-бот обучен и готов предоставить вам персонализированное обслуживание, которое поможет вам получить максимальную пользу от наших продуктов или услуг. \n\nБот доступен 24/7, чтобы помочь вам. Ваше удовлетворение - наш приоритет, и мы стремимся создать долгосрочные отношения с нашими клиентами, основанные на взаимном доверии и уважении. \n\nБлагодарим вас за выбор нашей компании. Мы ценим ваше доверие и готовы сделать все возможное, чтобы помочь вам достичь ваших целей и решить любые возникающие вопросы. Не стесняйтесь задавать вопросы - мы здесь, чтобы вам помочь! \n\nНомер горячей линии - xxx'


quest_ans_dict = {
    'Какие категории пожаров существуют?': 'Существуют четыре категории пожаров: А, Б, В и С. Категория А относится к пожарам в твердых веществах, категория Б - к пожарам в легковоспламеняющихся жидкостях, категория В - к пожарам в горючих газах, а категория С - к пожарам в электроустановках.',
    'Какие классы огнетушителей существуют?': 'Существуют классы огнетушителей A, B, C, D и K. Класс A предназначен для пожаров в твердых веществах, класс B - для пожаров в легковоспламеняющихся жидкостях, класс C - для пожаров в горючих газах, класс D - для пожаров в металлах, а класс K - для пожаров в кухонном жире и масле.',
    'Как правильно использовать огнетушитель?': 'Чтобы использовать огнетушитель, следуйте простому правилу, известному как ПАСС: приблизьтесь к огню на безопасное расстояние, схватите ручку огнетушителя, нажмите на рычаг, направьте струю на источник пламени и проводите перемещающиеся движения, охватывая всю площадь пожара.',
    'Какой срок службы у огнетушителей?': 'Срок службы огнетушителей обычно составляет 5-15 лет, в зависимости от типа огнетушителя. Однако, для поддержания работоспособности огнетушителя, регулярная проверка и обслуживание являются необходимыми.',
    'Где должны располагаться огнетушители?': 'Огнетушители должны располагаться на видных и доступных местах, вблизи потенциальных источников пожара. Рекомендуется устанавливать их на каждом этаже здания, вблизи кухонь, гаражей, электрощитов и других мест, где возможно возникновение пожара.',
    'Как часто следует проверять огнетушители?': 'Огнетушители должны проходить регулярную проверку. Рекомендуется осуществлять проверку как минимум раз в год. Кроме того, следует выполнять визуальные осмотры огнетушителей каждый месяц, чтобы убедиться в их наличии и готовности к использованию.',
    'Есть ли видеоинструкция по использованию огнетушителя?': 'Да, на нашем сайте доступна видеоинструкция по использованию огнетушителя. Вы можете просмотреть это видео, чтобы узнать подробности о правильном применении огнетушителя в случае пожара.',
    'Проводите ли вы тренировочные учения по пожаротушению?': 'Да, мы организуем тренировочные учения по пожаротушению для наших клиентов. Эти учения помогут вам освоить навыки безопасного использования огнетушителя и принятия правильных действий в случае пожара.',
    'Какие переносные огнетушители вы предлагаете?': 'Мы предлагаем широкий выбор переносных огнетушителей различных классов и емкостей. В нашем ассортименте есть огнетушители для пожаров в твердых веществах, жидкостях, газах, металлах, а также специальные огнетушители для кухонных пожаров.',
    'Какие пассивные средства пожаротушения вы рекомендуете?': 'Мы рекомендуем использовать пассивные средства пожаротушения, такие как огнезащитные покрытия, огнезащитные двери, дымовые и тепловые извещатели, автоматические системы пожаротушения и другие противопожарные меры. Эти средства помогут предотвратить распространение пожара и обеспечить безопасность в зданиях и сооружениях.'
}


text_news = {'news1': 'wildfire', 'news2': 'laws', 'news3': 'fireman', 'news4': 'random'}
text_order = {'order1': 'status', 'order2': 'repeat', 'order3': 'seller', 'order4': 'money_back', 'order5': 'another'}
text_recomendation = {'rec1': 'recomendation1', 'rec2': 'recomendation2', 'rec3': 'recomendation3'}
text_catalog = {'catalog1': 'extinguisher', 'catalog2': 'fire_cranes', 'catalog3': 'fire_inventory', 'catalog4': 'bedspreads', 'catalog5': 'fire_cabinets', 'catalog6': 'fire_shields', 'catalog7': 'another_item'}
text_sales = {'sales1': 'product_promotions', 'sales2': 'promotions_services'}
text_cli_help = {'product': 'ans1', 'catalog': 'ans2', 'sales': 'ans3', 'rec': 'ans4', 'another': 'ans5'}


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

def cli_help():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Вопрос по товарам', callback_data=text_catalog.get('product'))
    item2 = types.InlineKeyboardButton('Вопрос по заказу', callback_data=text_cli_help.get('ctalog'))
    item3 = types.InlineKeyboardButton('Вопрос по акциям', callback_data=text_cli_help.get('sales'))
    item4 = types.InlineKeyboardButton('Вопрос по рекомендациям', callback_data=text_cli_help.get('rec'))
    item5 = types.InlineKeyboardButton('Другой вопрос', callback_data=text_cli_help.get('another'))
    markup.add(item1, item2, item3, item4, item5)
    return markup

def catalog_markup():
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Огнетушители', callback_data=text_catalog.get('catalog1'))
    item2 = types.InlineKeyboardButton('Пожарные краны  ', callback_data=text_catalog.get('catalog2'))
    item3 = types.InlineKeyboardButton('Пожарный инвентарь', callback_data=text_catalog.get('catalog3'))
    item4 = types.InlineKeyboardButton('Покрывала', callback_data=text_catalog.get('catalog4'))
    item5 = types.InlineKeyboardButton('Пожарные шкафы', callback_data=text_catalog.get('catalog5'))
    item6 = types.InlineKeyboardButton('Пожарные щиты', callback_data=text_catalog.get('catalog6'))
    item7 = types.InlineKeyboardButton('Другой товар', callback_data=text_catalog.get('catalog7'))
    item8 = types.InlineKeyboardButton('Назад', callback_data='back')
    item9 = types.InlineKeyboardButton('На главное меню', callback_data='back_to_start')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
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

def bd_test_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Вопрос', callback_data= )
    item2 = types.InlineKeyboardButton('Ответ', callback_data= )
    markup.add(item1, item2)
    return markup



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 
                     text_main_menu, 
                     reply_markup=start_markup())

@bot.message_handler(commands=['support'])
def start_support(message):
    bot.send_message(message.chat.id, 
                     text_client_help, 
                     reply_markup=cli_help())

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
        elif call.data == 'discounts_promotions_questions':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text= 'Представляем вашему вниманию список наших акций: ', 
                                  reply_markup=sales_markup())
        elif call.data == 'back_to_start':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text= text_main_menu, 
                                  reply_markup=start_markup())
        elif call.data == 'product':
            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text= text_main_menu, 
                                  reply_markup=start_markup())

bot.infinity_polling(timeout=10, long_polling_timeout=5)

