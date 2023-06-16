from start import bot
import telebot
from telebot import types

color_begin = []
count = 0
chetchik = 1
number_of_person = {1: {"color": None, "point": 0},
                    2: {"color": None, "point": 0},
                    3: {"color": None, "point": 0}}
colors = []


def keyboard(call):  # функция для создания клавиатуры с цветами
    keyboard = types.InlineKeyboardMarkup()
    for keys in colors:
        keyboard.add(types.InlineKeyboardButton(text=keys, callback_data=keys))
    # markup1 = types.InlineKeyboardButton(text="Красный", callback_data="Красный")
    # markup2 = types.InlineKeyboardButton(text="Зелёный", callback_data="Зелёный")
    # markup3 = types.InlineKeyboardButton(text="Синий", callback_data="Синий")
    # markup4 = types.InlineKeyboardButton(text="Жёлтый", callback_data="Жёлтый")
    # markup5 = types.InlineKeyboardButton(text="Оранжевый", callback_data="Оранжевый")
    # markup6 = types.InlineKeyboardButton(text="Белый", callback_data="Белый")
    # markup7 = types.InlineKeyboardButton(text="Чёрный", callback_data="Чёрный")
    # keyboard.add(markup1, markup2, markup3, markup4, markup5, markup6, markup7)
    bot.send_message(call.message.chat.id, "<b>Чёрный выбран автоматически</b>", reply_markup=keyboard,
                     parse_mode="html")


@bot.message_handler(commands=['start'])
def start(message):
    global colors
    bot.send_message(chat_id=message.chat.id, text="Приветик, маленький игрок")
    bot.send_message(chat_id=message.chat.id, text="Давай поиграем")
    bot.send_message(chat_id=message.chat.id, text="Во что будем играть?")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Имаджинариум")
    markup.add(item1)
    bot.send_message(message.chat.id, text="Каков твой выбор?", reply_markup=markup)
    colors = ["Красный", "Оранжевый", "Жёлтый", "Зелёный", "Синий", "Белый", "Чёрный"]


@bot.message_handler(content_types='text')
def message_reply_numbers(message):  # функция для выбора кол-ва участников
    if message.text == "Имаджинариум":
        bot.send_message(chat_id=message.chat.id, text="Выбирай количество участников.")
        keyboard = types.InlineKeyboardMarkup()
        markup30 = types.InlineKeyboardButton(text="3", callback_data="3")
        markup40 = types.InlineKeyboardButton(text="4", callback_data="4")
        markup50 = types.InlineKeyboardButton(text="5", callback_data="5")
        markup60 = types.InlineKeyboardButton(text="6", callback_data="6")
        markup70 = types.InlineKeyboardButton(text="7", callback_data="7")
        keyboard.add(markup30, markup40, markup50, markup60, markup70)
        bot.send_message(message.chat.id, "Сделай свой выбор", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def calling_button(call):
    global number_of_person, count, chetchik, colors

    kbd = types.InlineKeyboardMarkup()
    kbd.add(types.InlineKeyboardButton(text="Далее", callback_data="Далее"))

    if call.data == "3":
        number_of_person = {1: {"color": None, "point": 0},
                            2: {"color": None, "point": 0},
                            3: {"color": None, "point": 0}}
        bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
                         reply_markup=kbd)
        keyboard(call)
        count = 3
    elif call.data == "4":
        number_of_person = {1: {"color": None, "point": 0},
                            2: {"color": None, "point": 0},
                            3: {"color": None, "point": 0},
                            4: {"color": None, "point": 0}}
        bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
                         reply_markup=kbd)
        keyboard(call)
        count = 4
    elif call.data == "5":
        number_of_person = {1: {"color": None, "point": 0},
                            2: {"color": None, "point": 0},
                            3: {"color": None, "point": 0},
                            4: {"color": None, "point": 0},
                            5: {"color": None, "point": 0}}
        bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
                         reply_markup=kbd)
        keyboard(call)
        count = 5
    elif call.data == "6":
        number_of_person = {1: {"color": None, "point": 0},
                            2: {"color": None, "point": 0},
                            3: {"color": None, "point": 0},
                            4: {"color": None, "point": 0},
                            5: {"color": None, "point": 0},
                            6: {"color": None, "point": 0}}
        bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
                         reply_markup=kbd)
        keyboard(call)
        count = 6
    elif call.data == "7":
        number_of_person = {1: {"color": None, "point": 0},
                            2: {"color": None, "point": 0},
                            3: {"color": None, "point": 0},
                            4: {"color": None, "point": 0},
                            5: {"color": None, "point": 0},
                            6: {"color": None, "point": 0},
                            7: {"color": None, "point": 0}}
        bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
                         reply_markup=kbd)
        keyboard(call)
        count = 7


    elif call.data in colors and chetchik <= count:
        number_of_person[chetchik]["color"] = call.data
        chetchik += 1
        colors.remove(call.data)
        print(call.data)
        print(chetchik)
    print(number_of_person)


"""
    elif call.data == "Красный":
        if chetchik<count:
            number_of_person[chetchik]['color']="Красный"
            print(number_of_person)
            
msg = bot.send_message(message.chat.id, 'Text')
time.sleep(1)
bot.edit_message_text(chat_id = message.chat.id, message_id = msg.message_id, text = 'Edited text')
time.sleep(1)
bot.edit_message_text(chat_id = message.chat.id, message_id = msg.message_id, text = 'Edited one more time')

"""
