from time import sleep


from bootstrap import getAllSubribe,setSubribe

def HandlerCoronaNews(bot, data):
# Print
	print("Зашёл в раздел - Корона Новости")
	print(data)


def HandlerSafety(bot,data):
	# Удаляем прошлое сообщение
    bot.delete_messages(chat_id=data['message']['chat']['chatId'], msg_id=data['message']['msgId'])
	# Создаем новое сообщение
    bot.send_text(chat_id=data['message']['chat']['chatId'], text="Вот пару советов как \n"
                                                        "обезопасить себя во время пандемии.")


# Event подписка на рассылку

def HandlerSubscribe(bot,data):
# Print
	print("Подпискалься на оповещения")
	bot.edit_text(chat_id=data['message']['chat']['chatId'],msg_id=data['message']['msgId'],text="Спасибо за подписку!")
	sleep(2)
	bot.delete_messages(chat_id=data['message']['chat']['chatId'],msg_id=data['message']['msgId'])
	# создаем подписку в базе
	setSubribe(data['message']['chat']['chatId'])
	#debug
	print(data['message']['chat']['chatId'])





# getAllSubribe()

