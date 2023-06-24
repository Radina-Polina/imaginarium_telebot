# elif call.data == "Красный!" and call.data[:-1] != now_playing:
#     try:
#         for key, value in number_of_person.items():
#             if value["color"] == "Красный":
#                 value["point"] += 3
#                 chetchik2 += 1
#         print(number_of_person)
#
#     except:
#         raise Exception("ПЕРЕДЕЛЫВАЙ!")
#
#
# elif call.data == "Оранжевый!" and call.data[:-1] != now_playing:
#     try:
#         for key, value in number_of_person.items():
#             if value["color"] == "Оранжевый":
#                 value["point"] += 3
#                 chetchik2 += 1
#         print(number_of_person)
#     except:
#         raise Exception("ПЕРЕДЕЛЫВАЙ!")
# elif call.data == "Жёлтый!" and call.data[:-1] != now_playing:
#     try:
#         for key, value in number_of_person.items():
#             if value["color"] == "Жёлтый":
#                 value["point"] += 3
#                 chetchik2 += 1
#         print(number_of_person)
#     except:
#         raise Exception("ПЕРЕДЕЛЫВАЙ!")
# elif call.data == "Зелёный!" and call.data[:-1] != now_playing:
#     try:
#         for key, value in number_of_person.items():
#             if value["color"] == "Зелёный":
#                 value["point"] += 3
#                 chetchik2 += 1
#         print(number_of_person)
#     except:
#         raise Exception("ПЕРЕДЕЛЫВАЙ!")
# elif call.data == "Синий!" and call.data[:-1] != now_playing:
#     try:
#         for key, value in number_of_person.items():
#             if value["color"] == "Синий":
#                 value["point"] += 3
#                 chetchik2 += 1
#         print(number_of_person)
#     except:
#         raise Exception("ПЕРЕДЕЛЫВАЙ!")
# elif call.data == "Белый!" and call.data[:-1] != now_playing:
#     try:
#         for key, value in number_of_person.items():
#             if value["color"] == "Белый":
#                 value["point"] += 3
#                 chetchik2 += 1
#         print(number_of_person)
#     except:
#         raise Exception("ПЕРЕДЕЛЫВАЙ!")
# elif call.data == "Чёрный!" and call.data[:-1] != now_playing:
#     try:
#         for key, value in number_of_person.items():
#             if value["color"] == "Чёрный":
#                 value["point"] += 3
#                 chetchik2 += 1
#         print(number_of_person)
#     except:
#         raise Exception("ПЕРЕДЕЛЫВАЙ!")
#
# elif call.data == "next":
#     if 0 < chetchik2 < count - 1:
#         number_of_person[prew_now]["point"] += 3
#     playing(call.message)
#     chetchik2=0
# if call.data == "3":
#     number_of_person = {1: {"color": None, "point": 0},
#                         2: {"color": None, "point": 0},
#                         3: {"color": None, "point": 0}}
#     bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
#                      reply_markup=kbd)
#
#     count = 3
# elif call.data == "4":
#     number_of_person = {1: {"color": None, "point": 0},
#                         2: {"color": None, "point": 0},
#                         3: {"color": None, "point": 0},
#                         4: {"color": None, "point": 0}}
#     bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
#                      reply_markup=kbd)
#
#     count = 4
# elif call.data == "5":
#     number_of_person = {1: {"color": None, "point": 0},
#                         2: {"color": None, "point": 0},
#                         3: {"color": None, "point": 0},
#                         4: {"color": None, "point": 0},
#                         5: {"color": None, "point": 0}}
#     bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
#                      reply_markup=kbd)
#     count = 5
# elif call.data == "6":
#     number_of_person = {1: {"color": None, "point": 0},
#                         2: {"color": None, "point": 0},
#                         3: {"color": None, "point": 0},
#                         4: {"color": None, "point": 0},
#                         5: {"color": None, "point": 0},
#                         6: {"color": None, "point": 0}}
#     bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
#                      reply_markup=kbd)
#     count = 6
# elif call.data == "7":
#     number_of_person = {1: {"color": None, "point": 0},
#                         2: {"color": None, "point": 0},
#                         3: {"color": None, "point": 0},
#                         4: {"color": None, "point": 0},
#                         5: {"color": None, "point": 0},
#                         6: {"color": None, "point": 0},
#                         7: {"color": None, "point": 0}}
#     bot.send_message(chat_id=call.message.chat.id, text="Выбирай цвета, которые будут участвовать в игре.",
#                      reply_markup=kbd)
#     count = 7