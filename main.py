import telebot
from bot_logic import gen_pass
  
bot = telebot.TeleBot("TOKEN")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
        bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
        bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['password'])
def send_password(message):
        bot.reply_to(message, 'Введите количество символов')
        bot.register_next_step_handler(message, new_password)
def new_password(message):
        len_password = int(message.text)
        bot.reply_to(message, f'Ваш сгенерированный пароль: {gen_pass(len_password)}')    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)
    
bot.polling()