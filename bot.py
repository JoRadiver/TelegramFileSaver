import telepot
import os
import config
import time

def authenticate(user):
	if user == config.admin:
		print('user is admin')
		return True
	return False

def handle(msg):
	msg_type, chat_type, chat_id = telepot.glance(msg) 
	user_id = msg['from']['id']
	if authenticate(user_id):
		print('received message')
		if msg_type == 'document':
			name = msg['document']['file_name']
			file_id = msg['document']['file_id']
			if name != None:
				bot.download_file(file_id, config.path)
				return
		bot.sendMessage(chat_id, "Only Files accepted")
	
	
bot = telepot.Bot(config.telegram_token)
bot.message_loop(handle)
print('running')
while 1:
	time.sleep(1)