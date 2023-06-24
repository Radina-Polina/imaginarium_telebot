from start import bot
from telebot import types

count = 0  # переменная для кол-ва участников
chetchik = 1  # переменная , используемая для создания клавиатуры
number_of_person = {1: {"color": None, "point": 0},  # словарь с данными участников
                    2: {"color": None, "point": 0},
                    3: {"color": None, "point": 0}}
colors = []  # список с цветами
game_ready = None  # флаг на начало игры
now = 1  # переменная для определения номера того, кто ходит
prew_now = 1  # переменная, используемая для добавления очков
kbd2 = None  # клавиатура вторая для счёта очков
now_playing = None
chetchik2 = 0  # для передачи хода переменная


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
def calling_button(call):  # обработка кнопок
    global number_of_person, count, chetchik, colors, game_ready, kbd2, chetchik2, prew_now

    kbd = types.InlineKeyboardMarkup()
    kbd.add(types.InlineKeyboardButton(text="Далее", callback_data="Далее"))

    if call.data in ['3', '4', '5', '6', '7']:  # создание словаря с цветами
        count = int(call.data)

        for i in range(count - 3):
            number_of_person[count] = {"color": None, "point": 0}
        bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
                         reply_markup=kbd)



    elif call.data == "Далее":  # кнопка далее
        keyboard(call, "1")

    elif call.data in colors and chetchik <= count:  # создание клавиатуры после кнопки далее, она меняется
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
                                                    callback_data=str(value["color"]) + "!"))
            kbd2.add(types.InlineKeyboardButton(text="Передать ход",
                                                callback_data='next'))


    elif call.data in ["Красный!", "Оранжевый!", "Жёлтый!", "Зелёный!", "Синий!", "Белый!",
                       "Чёрный!"]:  # если угадали + нажатие +3 балла
        try:
            for key, value in number_of_person.items():
                if value["color"] == call.data[:-1] and call.data[:-1] != number_of_person[now - 1]['color']:
                    value["point"] += 3
                    chetchik2 += 1
            print(number_of_person)
        except:
            raise Exception("ПЕРЕДЕЛЫВАЙ!")
    elif call.data == "next":
        if 0 < chetchik2 < count - 1:
            number_of_person[prew_now]["point"] += 3
        playing(call.message)
        chetchik2 = 0
