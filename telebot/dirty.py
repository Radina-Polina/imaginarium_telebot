# @bot.callback_query_handler(func=lambda call: True)
# def message_reply(message):
#     if message.text=="Имаджинариум":
#         bot.send_message(chat_id=message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.")
#
#         keyboard = types.InlineKeyboardMarkup()
#         markup1= types.InlineKeyboardButton(text="Красный", callback_data="Красный")
#         markup2= types.InlineKeyboardButton(text="Зелёный",callback_data="Зелёный")
#         markup3= types.InlineKeyboardButton(text="Синий",callback_data="Синий")
#         markup4= types.InlineKeyboardButton(text="Жёлтый",callback_data="Желтый")
#         markup5= types.InlineKeyboardButton(text="Оранжевый",callback_data="Оранжевый")
#         markup6= types.InlineKeyboardButton(text="Белый",callback_data="Белый")
#         keyboard.add(markup1,markup2,markup3,markup4,markup5,markup6)
#         bot.send_message(message.chat.id, "Чёрный выбран автоматически", reply_markup=keyboard)
