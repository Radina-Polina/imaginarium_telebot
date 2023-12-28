from telebot import types

from start import bot

count_of_players = 0  # количество игроков
player_chose_color = 1
counter_of_players = None
players_data = {1: {"color": None, "point": 0},  # словарь с данными участников
                2: {"color": None, "point": 0},
                3: {"color": None, "point": 0}}
colors = ["Красный", "Оранжевый", "Жёлтый", "Зелёный", "Синий", "Белый", "Чёрный"]  # список цветов игры
game_ready = False
finish_flag = False
counter = 1
keyboard = None
count_of_pushes = {}


def chose_color(colors_list, d):
    colors_keyboard = types.InlineKeyboardMarkup()
    for key in colors_list:
        colors_keyboard.add(types.InlineKeyboardButton(text=key, callback_data=key + d))
    return colors_keyboard


@bot.message_handler(commands=['start'])
def start(message):
    global count_of_players,player_chose_color,counter_of_players ,players_data,colors,game_ready,finish_flag,counter,keyboard,count_of_pushes
    count_of_players = 0  # количество игроков
    player_chose_color = 1
    counter_of_players = None
    players_data = {1: {"color": None, "point": 0},  # словарь с данными участников
                    2: {"color": None, "point": 0},
                    3: {"color": None, "point": 0}}
    colors = ["Красный", "Оранжевый", "Жёлтый", "Зелёный", "Синий", "Белый", "Чёрный"]  # список цветов игры
    game_ready = False
    finish_flag = False
    counter = 1
    keyboard = None
    count_of_pushes = {}
    bot.send_message(chat_id=message.chat.id, text="*Приветик, маленький игрок*.\nДавай поиграем.\nВо что будем играть?",parse_mode="Markdown")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Имаджинариум"))
    bot.send_message(message.chat.id, text="Каков твой выбор?", reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply_numbers(message):  # функция для выбора кол-ва участников
    if message.text == "Имаджинариум":
        bot.send_message(chat_id=message.chat.id, text="Выбирай количество участников.")
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        for i in range(3, 8):
            keyboard.add(types.InlineKeyboardButton(text=i, callback_data=str(i)))
        bot.send_message(message.chat.id, "Сделай свой выбор", reply_markup=keyboard)

@bot.message_handler(content_types=['sticker'])
def sticker(message):
    stiker_id=message.sticker.file_id
    print(stiker_id)
@bot.callback_query_handler(func=lambda call: True)
def calling_button(call):
    """
    функция для обработки
    :param call:
    :return:
    """
    global count_of_players, player_chose_color, players_data, counter_of_players, finish_flag, keyboard, counter, count_of_pushes
    if call.data in "345678":
        count_of_players = int(call.data)
        bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
                         reply_markup=chose_color(colors, "a"))
        counter_of_players = count_of_players

    elif call.data == 'finish':
        bot.send_sticker(chat_id=call.message.chat.id,sticker='CAACAgIAAxkBAAIIDmVOdeALG7YDHnNuTmyFxMPca4oUAAJnAANlogMsURQqjKHC7BEzBA')
        finish_flag = True
        game2(players_data, call)
        game(players_data, call)
        bot.send_sticker(chat_id=call.message.chat.id,sticker='CAACAgIAAxkBAAIH_WVOdNzzcGdPFBN8FdNY9IJUjCPBAALiCAACbDtBKF15tvP7aUBoMwQ')
        bot.send_sticker(chat_id=call.message.chat.id, sticker='CAACAgIAAxkBAAIH_mVOdOHWk_3ULzYpzB-jieETPR2KAALnCAACbDtBKD4BbMYzXur9MwQ')
        bot.send_sticker(chat_id=call.message.chat.id, sticker='CAACAgIAAxkBAAIH_2VOdOXFgs6HISlqAAFDPi3kFkP2kAAC7AgAAmw7QShysmBUnDIVmzME')

    elif '@' in call.data:
        player = call.data[0]
        players_data[int(player)]['point'] += 1

    elif call.data=='start':
        start(call.message)

    elif '$' in call.data:

        player = call.data[0]
        if not count_of_pushes[player]:
            players_data[int(player)]['point'] += 3
            count_of_pushes[player] = True


    elif call.data == 'next':
        vedychi = counter - 1
        if vedychi == -0:
            vedychi = len(players_data)
        print(sum(count_of_pushes.values()))
        print(len(players_data))
        if sum(count_of_pushes.values()) != len(players_data) - 1:
            players_data[vedychi]['point'] += 3 * sum(count_of_pushes.values())

        bot.send_sticker(chat_id=call.message.chat.id,sticker='CAACAgIAAxkBAAIIDmVOdeALG7YDHnNuTmyFxMPca4oUAAJnAANlogMsURQqjKHC7BEzBA')
        game2(players_data, call)
        game(players_data, call)






    elif call.data[:-1] in colors:

        counter_of_players -= 1
        players_data[player_chose_color] = {"color": call.data[:-1], "point": 0}
        colors.remove(call.data[:-1])
        player_chose_color += 1
        if counter_of_players > 0:

            bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
                             reply_markup=chose_color(colors, "a"))
        else:
            bot.send_message(chat_id=call.message.chat.id, text="Цвета выбраны")
            game2(players_data, call)
            game(players_data,call)
        print(players_data, counter_of_players, count_of_players)


def game(data, call):
    global finish_flag, player_chose_color, counter, keyboard, count_of_pushes

    if finish_flag:
        text = ""
        for key, value in data.items():
            text += f"{players_data[key]['color']}-{value['point']}\n"
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Заново', callback_data='start'))
        bot.send_message(chat_id=call.message.chat.id, text=f'Спасибо за игру!\n{text}', reply_markup=keyboard)


        return
    else:
        if counter > len(data):
            counter = 1
        keyboard_players = [i for i in data if i != counter]
        keyboard = types.InlineKeyboardMarkup()
        count_of_pushes = {}
        for key in keyboard_players:
            keyboard.add(types.InlineKeyboardButton(text=f"Игрок-{players_data[key]['color']}", callback_data=(str(key) + '$')))
            count_of_pushes[str(key)] = False
        keyboard.add(types.InlineKeyboardButton(text='Далее', callback_data='next'))
        keyboard.add(types.InlineKeyboardButton(text="Конец игры", callback_data='finish'))
        bot.send_message(chat_id=call.message.chat.id, text=f'ведущий-{counter}', reply_markup=keyboard)
        counter += 1
        return


def game2(data, call):
    global finish_flag, player_chose_color, counter, keyboard, count_of_pushes
    if finish_flag:
        pass
    else:
        keyboard_players = [i for i in data if i != counter]
        keyboard = types.InlineKeyboardMarkup()
        for key in keyboard_players:
            keyboard.add(
                types.InlineKeyboardButton(text=f"{players_data[key]['color']}", callback_data=(str(key) + '@')))
        bot.send_message(chat_id=call.message.chat.id, text=f'Кого угадали', reply_markup=keyboard)

