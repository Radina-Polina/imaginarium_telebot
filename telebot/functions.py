from start import bot
from telebot import types

count = 0
chetchik = 1
number_of_person = {1: {"color": None, "point": 0},
                    2: {"color": None, "point": 0},
                    3: {"color": None, "point": 0}}
colors = []
game_ready = None
now = 1
prew_now = 1
kbd2 = None
now_playing = None
chetchik2 = 0


def keyboard(call, player):  # функция для создания клавиатуры с цветами
    global kbd2
    kbd = types.InlineKeyboardMarkup()
    for keys in colors:
        kbd.add(types.InlineKeyboardButton(text=keys, callback_data=keys))
    # kbd2 = types.InlineKeyboardMarkup()
    # for keys in colors:
    #     kbd2.add(types.InlineKeyboardButton(text=keys, callback_data=str(keys) + "!"))
    bot.send_message(call.message.chat.id, f"Игрок {player} - выберите цвет", reply_markup=kbd,
                     parse_mode="html")


def playing(message):
    global number_of_person, colors, kbd, call, kbd2, now, now_playing, prew_now
    bot.send_message(message.chat.id, f"Сейчас ход {number_of_person[now]['color']}игрока")
    now_playing = number_of_person[now]['color']
    prew_now = now
    if now == count:
        now = 0
    now += 1
    bot.send_message(message.chat.id, "Выберите тех, кто угадал", reply_markup=kbd2)


@bot.message_handler(commands=['start'])
def start(message):
    global colors, game_ready
    bot.send_message(chat_id=message.chat.id, text="Приветик, маленький игрок\nДавай поиграем\nВо что будем играть?")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Имаджинариум"))
    bot.send_message(message.chat.id, text="Каков твой выбор?", reply_markup=markup)
    # создание переменных для игры
    colors = ["Красный", "Оранжевый", "Жёлтый", "Зелёный", "Синий", "Белый", "Чёрный"]
    game_ready = False


@bot.message_handler(content_types='text')
def message_reply_numbers(message):  # функция для выбора кол-ва участников
    global number_of_person, colors, kbd, call, kbd2, now, now_playing
    ck = 0
    ygadavshie = []
    if message.text == "Имаджинариум":
        bot.send_message(chat_id=message.chat.id, text="Выбирай количество участников.")
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        markup30 = types.InlineKeyboardButton(text="3", callback_data="3")
        markup40 = types.InlineKeyboardButton(text="4", callback_data="4")
        markup50 = types.InlineKeyboardButton(text="5", callback_data="5")
        markup60 = types.InlineKeyboardButton(text="6", callback_data="6")
        markup70 = types.InlineKeyboardButton(text="7", callback_data="7")
        keyboard.add(markup30, markup40, markup50, markup60, markup70)
        bot.send_message(message.chat.id, "Сделай свой выбор", reply_markup=keyboard)

    elif message.text == "ИГРАТЬ" and game_ready:
        playing(message)


@bot.callback_query_handler(func=lambda call: True)
def calling_button(call):
    global number_of_person, count, chetchik, colors, game_ready, kbd2, chetchik2, prew_now

    kbd = types.InlineKeyboardMarkup()
    kbd.add(types.InlineKeyboardButton(text="Далее", callback_data="Далее"))

    if call.data == "3":
        number_of_person = {1: {"color": None, "point": 0},
                            2: {"color": None, "point": 0},
                            3: {"color": None, "point": 0}}
        bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
                         reply_markup=kbd)

        count = 3
    elif call.data == "4":
        number_of_person = {1: {"color": None, "point": 0},
                            2: {"color": None, "point": 0},
                            3: {"color": None, "point": 0},
                            4: {"color": None, "point": 0}}
        bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
                         reply_markup=kbd)

        count = 4
    elif call.data == "5":
        number_of_person = {1: {"color": None, "point": 0},
                            2: {"color": None, "point": 0},
                            3: {"color": None, "point": 0},
                            4: {"color": None, "point": 0},
                            5: {"color": None, "point": 0}}
        bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
                         reply_markup=kbd)
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
        count = 7

    elif call.data == "Далее":
        keyboard(call, "1")

    elif call.data in colors and chetchik <= count:
        number_of_person[chetchik]["color"] = call.data
        chetchik += 1
        colors.remove(call.data)
        if chetchik <= count:
            keyboard(call, chetchik)
            print(call.data)
            print(chetchik)
        else:
            game_ready = True
            bot.send_message(chat_id=call.message.chat.id, text="Цвета выбраны. НАПИШИТЕ 'ИГРАТЬ'")
            kbd2 = types.InlineKeyboardMarkup()
            for key, value in number_of_person.items():
                kbd2.add(types.InlineKeyboardButton(text=value["color"],
                                                    callback_data=value["color"] + "!"))
            kbd2.add(types.InlineKeyboardButton(text="Передать ход",
                                                callback_data='next'))

    elif call.data == "Красный!" and call.data[:-1] != now_playing:
        try:
            for key, value in number_of_person.items():
                if value["color"] == "Красный":
                    value["point"] += 3
                    chetchik2 += 1
            print(number_of_person)

        except:
            raise Exception("ПЕРЕДЕЛЫВАЙ!")


    elif call.data == "Оранжевый!" and call.data[:-1] != now_playing:
        try:
            for key, value in number_of_person.items():
                if value["color"] == "Оранжевый":
                    value["point"] += 3
                    chetchik2 += 1
            print(number_of_person)
        except:
            raise Exception("ПЕРЕДЕЛЫВАЙ!")
    elif call.data == "Жёлтый!" and call.data[:-1] != now_playing:
        try:
            for key, value in number_of_person.items():
                if value["color"] == "Жёлтый":
                    value["point"] += 3
                    chetchik2 += 1
            print(number_of_person)
        except:
            raise Exception("ПЕРЕДЕЛЫВАЙ!")
    elif call.data == "Зелёный!" and call.data[:-1] != now_playing:
        try:
            for key, value in number_of_person.items():
                if value["color"] == "Зелёный":
                    value["point"] += 3
                    chetchik2 += 1
            print(number_of_person)
        except:
            raise Exception("ПЕРЕДЕЛЫВАЙ!")
    elif call.data == "Синий!" and call.data[:-1] != now_playing:
        try:
            for key, value in number_of_person.items():
                if value["color"] == "Синий":
                    value["point"] += 3
                    chetchik2 += 1
            print(number_of_person)
        except:
            raise Exception("ПЕРЕДЕЛЫВАЙ!")
    elif call.data == "Белый!" and call.data[:-1] != now_playing:
        try:
            for key, value in number_of_person.items():
                if value["color"] == "Белый":
                    value["point"] += 3
                    chetchik2 += 1
            print(number_of_person)
        except:
            raise Exception("ПЕРЕДЕЛЫВАЙ!")
    elif call.data == "Чёрный!" and call.data[:-1] != now_playing:
        try:
            for key, value in number_of_person.items():
                if value["color"] == "Чёрный":
                    value["point"] += 3
                    chetchik2 += 1
            print(number_of_person)
        except:
            raise Exception("ПЕРЕДЕЛЫВАЙ!")

    elif call.data == "next":
        if 0 < chetchik2 < count - 1:
            number_of_person[prew_now]["point"] += 3
        playing(call.message)
        chetchik2=0


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
