
import telebot
from config import API_TOKEN, key, secret_key
from df import Text2ImageAPI


bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\Привет я бот ии генерирующий картинки\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    zapros = message.text
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', key, secret_key)
    model_id = api.get_model()
    uuid = api.generate(zapros, model_id)
    images = api.check_generation(uuid)
    name = Text2ImageAPI.base64_to_image(images[0])

    photo = open(name, 'rb')
    bot.send_photo(message.chat.id, photo)

  


bot.infinity_polling()