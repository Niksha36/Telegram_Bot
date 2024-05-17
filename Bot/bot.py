import telebot
from telebot import types

with open("Token.txt", "r") as file:
    token = file.read()

bot = telebot.TeleBot(token)

# Set the list of commands
bot.set_my_commands([
    types.BotCommand(command="/start", description="Запустить бота"),
    types.BotCommand(command="/description", description="Описание бота"),
])

# Define a command handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Типы ML")
    item2 = types.KeyboardButton("Архитектуры ML")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Добропожаловать! Выберите интересующий вас раздел. Чтобы узнать описание введите /description", reply_markup=markup)

# Define a command handler for the /description command
@bot.message_handler(commands=['description'])
def send_description(message):
    bot.send_message(message.chat.id, "Этот бот создан для обучения основам машинного обучения. Вы можете выбрать раздел Типы ML или Архитектуры ML для получения информации.")

# Define a message handler
@bot.message_handler(func=lambda message: message.text == "Типы ML")
def send_ml_types(message):
    bot.send_message(message.chat.id, "Здесь будут типы ML")

@bot.message_handler(func=lambda message: message.text == "Архитектуры ML")
def send_ml_types(message):
    bot.send_message(message.chat.id, "Здесь будут Архитектуры ML")

# Start the bot
bot.polling()