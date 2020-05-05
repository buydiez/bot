import logging

from bot.bot import Bot
from bot.handler import *
#bot config
from config import *

#from bootstrap import *

bot = Bot(token=TOKEN)


"""
Variable
"""


def recommendations(bot, event):
    user_firstname = bot.get_chat_info(chat_id=event.from_chat).json()['firstName']  # Имя пользователя
    chatId = event.data['chat']['chatId']
    print("Рекомендации")
    print(event)
    bot.send_text(chat_id=event.from_chat, text="Привет, я бот 🤖"
                                                "\nТебе нужна помощь во время карантина? 🤒")
    messageDelSpace(bot=bot, event=event)

    bot.send_file(chat_id=chatId, file_id=1)
    bot.send_text(chat_id=chatId, text=" ", inline_keyboard_markup="{}".format(json.dumps([[
        {"text": "🦠 Заказать тест \n на Covid19 🆓", "url": "https://help.yandex.ru/covid19-test", "style": "attention"},
        {"text": "💬 Часто задаваемые \n вопросы 🤧", "url": "https://стопкоронавирус.рф/faq/#faq25", "style": "primary"}
    ],
    ])))
    messageDelSpace(bot=bot, event=event)
    bot.send_text(chat_id=chatId, text="https://sun9-46.userapi.com/c858120/v858120469/1ea55b/clpiY6GNgX0.jpg", inline_keyboard_markup="{}".format(json.dumps([[
        {"text": "💻 Достоверные источники информации 💼 ", "url": "https://mel.fm/koronavirus/7618453-coronavirus_info", "style": "primary"}
    ],
    ])))
    #messageDelSpace(bot=bot, event=event)
    #bot.send_text(chat_id=chatId, text=" ", inline_keyboard_markup="{}".format(json.dumps([[
    #    {"text": "🚑 Экстренная кнопка 🆘 ", "callbackData": "call_back_id_1", "style": "attention"}],
    #])))
"""
 Main chat method [START]
"""

def start(bot, event) :
    chatId = event.data['chat']['chatId']
    #кнопки с рекомендациями
    recommendations(bot, event)
    help_command(bot, event)

    #allMember()
    # check = getMemberCheck(chatId=event.data['chat']['chatId'])
    # print(check)
    # if check:
    #     print("Если все успешно и пользователь авторизован +")
    # else:
    #     print("Если пользователь не авторизован")

from command.main import *


value = []

def answer_cb(bot, event):
    global value
    if event.text in value:
        bot.send_text(chat_id=event.from_chat, text='Congratulations!')
    else:
        bot.send_text(chat_id=event.from_chat, text='Используйте /help')

def buttons_answer_cb(bot, event):
    if event.data['callbackData'] == "call_back_id_1":
        bot.send_text(query_id=event.from_chat, text="Телефон горячей линии: +78002000112")
    elif event.data['callbackData'] == "call_back_id_2":
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text="💊 Список комманд: \n🆘 "
                 "Помощь в трудной ситуации, используйте  /sos "
                 "\n🧪  Пройти бесплатное обследование  /test",
            show_alert=True
        )


def buttons(bot, event):
    # Covid(Корона вирус) доставерные новости
    if event.data['callbackData'] == "call_button_command_test":
        test_command(bot,  event)

    elif event.data['callbackData'] == "call_button_command_ask":
        bot.send_text(chat_id=event.from_chat, text=event.text)

bot.dispatcher.add_handler(BotButtonCommandHandler(callback=buttons)) #buttonHandler

#bot.dispatcher.add_handler(MessageHandler(filters=Filter.regexp("/start*"), callback=message_cb)) #start *

#bot.dispatcher.add_handler(LeftChatMembersHandler(callback=last_members))
#   bot.dispatcher.add_handler(NewChatMembersHandler(callback=new_members)) # new member

bot.dispatcher.add_handler(StartCommandHandler(callback=start))
bot.dispatcher.add_handler(HelpCommandHandler(callback=help_command)) #/help command
bot.dispatcher.add_handler(UnknownCommandHandler(callback=unknown_command)) #not found command
bot.dispatcher.add_handler(BotButtonCommandHandler(callback=buttons_answer_cb))
#bot.dispatcher.add_handler(CommandHandler(callback=alerts_command, command="alerts"))
bot.dispatcher.add_handler(CommandHandler(callback=sos_command, command="sos"))
bot.dispatcher.add_handler(CommandHandler(callback=test_command, command="test"))
bot.dispatcher.add_handler(MessageHandler(filters=Filter.text, callback=answer_cb))
#poling server
print("Start Polling")
bot.start_polling()

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y.%m.%d %I:%M:%S %p',
                    level=logging.DEBUG)

#infinite
bot.idle()
