import telebot, time, os, random 
from bot_logic import gen_pass, gen_coin, gen_smile, get_duck_image_url, get_dog_image_url
 
bot = telebot.TeleBot("TOKEN")
tconv = lambda x: time.strftime("%H", time.localtime(x))    
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
        name = message.from_user.first_name
        bot.reply_to(message, f'Привет, {name}! Я бот {bot.get_me().first_name}! /start, /hello, /bye, /password, /coin, /heh, /mem, /duck, /dog')
    
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
    
@bot.message_handler(commands=['coin'])
def send_coin(message):
        bot.reply_to(message, gen_coin())
@bot.message_handler(commands=['heh'])
def send_heh(message):
        count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
        bot.reply_to(message, "he" * count_heh)
@bot.message_handler(commands=['mem'])
def send_mem(message):
    picture = random.choice(os.listdir('images'))
    with open(f'images/{picture}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 
@bot.message_handler(commands=['duck'])
def duck(message):
        image_url = get_duck_image_url()
        bot.reply_to(message, image_url)
@bot.message_handler(commands=['dog'])
def dog(message):
        image_url = get_dog_image_url()
        bot.reply_to(message, image_url)
@bot.message_handler(content_types=['text'])
def send_smile(message):
        r = tconv(message.date)
        emojies = ['(* ^ ω ^)', '(´ ∀ ` *)','(◕‿◕｡)۶','☆*:.｡.o(≧▽≦)o.｡.:*☆', '(o^▽^o)']
        if r == '18':
                bot.reply_to(message, emojies[0])
        elif r == '19':
                bot.reply_to(message, emojies[1])
        elif r == '20':
                bot.reply_to(message, emojies[2])
        elif r == '21':
                bot.reply_to(message, emojies[3])
        else:
                bot.reply_to(message, f'Сейчас {r}, эмодзи грузится') 
        print(r)
        #bot.reply_to(message, gen_smile(r))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)
    
bot.polling()