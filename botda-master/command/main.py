import json

from utils import *





def unknown_command(bot, event):
    user = event.from_chat
    (command, command_body) = event.data["text"].partition(" ")[::2]
    bot.send_text(
        chat_id=user,
        text="🕳 Ой нечего не найдено. Используйте /help".format(
            source=user, message=command[1:], command_body=command_body
        )
    )


def help_command(bot, event):
    bot.send_text(chat_id=event.from_chat, text="💊 Список комманд: \n"
                                                "\n🆘  Помощь в трудной ситуации, используйте  /sos\n"
                                                "\n🧪  Пройти бесплатное обследование  /test \n")
                                                #"\n🗞  Настройка уведомлений  /alerts \n")
def sos_command(bot, event):
    bot.send_text(chat_id=event.from_chat, text="Телефон горячей линии: +78002000112")
def test_command(bot, event):
    bot.send_text(chat_id=event.from_chat, text="💊 Узнайте, нет ли у вас и ваших близких коронавируса"
                                                "\n— закажите бесплатное тестирование на дому.")
    bot.send_text(chat_id=event.from_chat, text="Медработник возьмёт анализ, и в течение "
                                                "\n3 рабочих дней вам сообщат результаты.")

    #space
    messageDelSpace(bot, event)
    #send site
    bot.send_text(chat_id=event.from_chat, text="Перейти к составлению заявки!",
                  inline_keyboard_markup="{}".format(json.dumps([[
                      {"text": "Открыть сайт", "url": "https://help.yandex.ru/covid19-test", "style": "primary"},
                  ]])))
    #space
    #delete_space = bot.send_text(chat_id=event.from_chat, text=" ")
    #bot.delete_messages(chat_id=event.from_chat, msg_id=delete_space)

    #service btn
    #bot.send_text(chat_id=event.from_chat, text=" ",
     #             inline_keyboard_markup="{}".format(json.dumps([[
      #                {"text": "🆘  Срочная помощь! ", "callbackData": "call_back_id_1", "style": "primary"},
       #               {"text": "💊  Команды! ", "callbackData": "call_back_id_2", "style": "primary"},
        #          ]])))


 # def alerts_command(bot, event):
 #    bot.send_text(chat_id=event.from_chat, text=" ",
 #                  inline_keyboard_markup="{}".format(json.dumps([[
 #                  {"text": "🆘  Срочная помощь! ", "callbackData": "call_back_id_1 ", "style": "primary"},
 #                  {"text": "💊  Команды! ", "callbackData": "call_back_id_2", "style": "primary"},
 #                  ]])))