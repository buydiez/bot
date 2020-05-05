"""
Space
"""


def messageDelSpace(bot, event):
	# space
	delele_space = bot.send_text(chat_id=event.from_chat, text=" ")
	bot.delete_messages(chat_id=event.from_chat, msg_id=delele_space)


# def messageDelSpaces(bot, event, count):
# 	# space
# 	for numbers in range(count):
# 		messageDelSpace(bot,event)
# 		continue
