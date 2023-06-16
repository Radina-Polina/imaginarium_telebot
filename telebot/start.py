import telebot

token='5978769746:AAEKTBfNvf_hRtIZZ4Ew4jPi_2CKAcD7vQw'
bot=telebot.TeleBot(token)

if __name__ == '__main__':
    from functions import bot
    bot.polling(none_stop=True)
