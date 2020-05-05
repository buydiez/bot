import logging
from threading import Thread
from sched import scheduler
from time import sleep
#bot
import requests

from bot.bot import Bot
from bot.handler import MessageHandler, StartCommandHandler


class MainBot:
	__slots__ = ('bot', 'docker', 'scheduler', 'events')

	def __init__(self, token):
		self.bot = Bot(token=token)
		self.scheduler = scheduler()
		self.events = {}

	def poll(event_id):

		params = {'lastEventId': str(event_id), 'pollTime': 300, 'token': token}

		reply = requests.get(f"{base_url}/events/get", params)

		if reply.status_code != requests.codes.ok:
			return None

		json = None
		try:
			json = reply.json()
		except Exception as e:
			logging.error('Invalid JSON from server: {}'.format(e))
			logging.error(reply.content)
			return None
		return json


	def get_start_callback(self):
		def callback(bot, event):
			chat_id = event.from_chat

			self.bot.send_text(chat_id=event.from_chat, text="Hello World")

			self.events[chat_id] = self.enter(10, 1, print_time)

		return callback

	def get_message_callback(self):
		def callback(bot, event):
			if event.text == '/start':
				return
			return callback

	def start(self):
		Thread(target=self.run_scheduler).start()

		self.bot.dispatcher.add_handler(
			StartCommandHandler(callback=self.get_start_callback()))

		self.bot.dispatcher.add_handler(
			MessageHandler(callback=self.get_message_callback()))

		self.bot.start_polling()
		self.bot.idle()



if __name__ == '__main__':
	token = "001.1623773992.2503076683:752164923"
	MainBot(token).start()
