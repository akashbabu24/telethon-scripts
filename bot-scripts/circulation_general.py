from telethon.sync import TelegramClient, events, types
import time

import os 
import random

my_list = os.listdir('/home/ec2-user/telethon/general-stuff')

session_list = ['user1', 'user2', 'user3']
time_ = [90, 180, 340, 900, 560]

while my_list:
 namechosen = random.choice(session_list)

 if namechosen == 'user1' :
    api = ''    #user1 api/hash here. Note even given here, additional otp authentication is there while executing the sctipt
    api_hash = ''
 elif namechosen == 'user2' :
    api = ''     #user2 api/hash here
    api_hash = ''    
 else:
    api = ''   #default or user3 api/hash here
    api_hash = ''

 with  TelegramClient(namechosen, api, api_hash) as client:    #user's api and hash taken based on random choice
  random_key = '/home/ec2-user/telethon/general-stuff/' + random.choice(my_list)
  client.send_file('channel', random_key)
 time.sleep(random.choice(time_))


