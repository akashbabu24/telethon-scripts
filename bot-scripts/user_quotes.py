from telethon.sync import TelegramClient, events, types
import time

import os 
import random

#user chat messages to automate for hype. If this is executed along with slash_2.py, then slogan hype works as well
general = [ "Hello guys! how are you fam! please explain the project I'm new :D",
          "/WHEN_LAMBO",
          "/WHEN_MOON",
            "what is the symbol. How to buy this project.",
        ]

session_list = ['user1', 'user2', 'user3']
time_ = [750, 1500, 920]
while True:
 namechosen = random.choice(session_list)
 if namechosen == 'user1' :
    api = ''   #user1 api and hash to be given for this and below variable declaration
    api_hash = ''
    client = TelegramClient(namechosen, api, api_hash)
 elif namechosen == 'user2' :
    api = ''    #user2 api and hash
    api_hash = ''
    client = TelegramClient(namechosen, api, api_hash)
 else:
    api = ''   #user3 or default user values
    api_hash = ''
    client = TelegramClient(namechosen, api, api_hash)
 #   client = TelegramClient(namechosen, api, api_hash)

 with  TelegramClient(namechosen, api, api_hash) as client:    # client object creation with chosen user
  caption_ = ""

  # randomly choose a caption for chosen image, based on image name category
  caption_ = random.choice(general)
  # based on caption is empty or not, file is sent
  if (len(caption_)):
     client.send_message('channel', caption_)

 time.sleep(random.choice(time_))


