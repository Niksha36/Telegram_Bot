import os
import json
import telebot
import argparse

from telebot import types


def main():
    # Initialize parser
    msg = "Start telegram bot: MLWiki"
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument('token', type=str, help="Input token for the telegram bot. It can be obtained at BotFather")
    args = parser.parse_args()

    # Initialize bot
    bot = telebot.TeleBot(args.token)

    # Set the list of commands
    bot.set_my_commands([
        types.BotCommand(command="/start", description="Запустить бота"),
        types.BotCommand(command="/description", description="Описание бота"),
        types.BotCommand(command="/developers", description="Получить информацию о разработчиках"),
        types.BotCommand(command="/stop", description="Отключить бота"),
    ])


    # Define a command handler for the /start command
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Типы ML")
        item2 = types.KeyboardButton("Архитектуры ML")
        item3 = types.KeyboardButton("Ресурсы для изучения")
        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id,
                         "Добропожаловать! Выберите интересующий вас раздел. Чтобы узнать описание введите /description",
                         reply_markup=markup)


    # Define a command handler for the /description command
    @bot.message_handler(commands=['description'])
    def send_description(message):
        bot.send_message(message.chat.id,
                         "Этот бот создан для обучения основам машинного обучения.")


    # Define a command handler for the /developers command
    @bot.message_handler(commands=['developers'])
    def send_description(message):
        bot.send_message(message.chat.id,
                         "Разработчики:\n"
                         "Ганжа Эдуард Б9123-01.03.04мцм\n"
                         "Шурло Никита Б9123-01.03.04мцм\n"
                         "Нестеров Игорь Б9123-01.03.02сп")


    # Define a command handler for the /stop command
    @bot.message_handler(commands=['stop'])
    def stop_bot(message):
        bot.send_message(message.chat.id, "Бот отключен :(")
        bot.stop_polling()


    # Define a message handler
    @bot.message_handler(func=lambda message: message.text == "Типы ML")
    def send_ml_types(message):
        bot.send_message(message.chat.id, text["types"])


    @bot.message_handler(func=lambda message: message.text == "Архитектуры ML")
    def send_ml_types(message):
        bot.send_message(message.chat.id, text["architectures"])

    @bot.message_handler(func=lambda message: message.text == "Ресурсы для изучения")
    def send_ml_types(message):
        bot.send_message(message.chat.id, text["links"])

    bot.polling(none_stop=True)


# Start the bot
if __name__ == "__main__":
    with open(os.path.dirname(os.path.abspath(__file__)) + "\\message.json", 'r', encoding='utf-8') as f:
        text = json.load(f)

    while True:
        try:
            main()
        except Exception as e:
            time.sleep(3)
