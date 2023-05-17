import telebot

API_TOKEN = "5658948785:AAGOBJfD3veVdc_dwCTRA0T0jB6QN0q5j-I"

bot = telebot.TeleBot(API_TOKEN)

bot.set_my_commands([
    telebot.types.BotCommand("/start", "Запуск бота"),
])

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте, я-бот, отправьте мне в ответ любое число')
    bot.register_next_step_handler(message, answer_rndm_msg)
def answer_rndm_msg(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, f"Сообщение '{message.text}' не является числом")
    else:
        bot.send_message(message.chat.id, "Спасибо")

bot.infinity_polling(timeout=10, long_polling_timeout=5)
