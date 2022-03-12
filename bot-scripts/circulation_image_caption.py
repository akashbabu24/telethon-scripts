from telethon.sync import TelegramClient, events, types
import time

import os 
import random

#below are sample captions. replcae with your captions to be sent along with images. This script attaches one of the captions from below category based on name of the image saved in the given directory. 
burn = ["aggravated burn - true defaltionary token",
        "A share of rewards will be sent to the burn address",

draw = ["Weekly lucky draws for holders. Just hold tokens and get a chance to earn millions. "
        "No extra effort needed. Just Buy or HOLD tokens to win HUGE lucky giveaways"]

reward = ["Just HOLD token and receive auto-yield with every trade on pancakes!",
          "Native auto-staking that benefits holders"
        ]

general = ["Liquidity pool increases from auto-liquidity. 1% of every trade",
           "Highly secure and stabilized token. Secured from snipper bots, dumps, and liquidity disruption",
        ]
my_list = os.listdir('/home/ec2-user/telethon/s3-list')

# User session swapping dynamically
session_list = ['name', 'name1', 'name3']

#Time interval chosen randomly from given list
time_ = [300, 900, 120, 420, 1200]
while my_list:
 namechosen = random.choice(session_list)

 if namechosen == 'name' :
    api = ''    #give user1 api token here
    api_hash = ''   #user2 hash
 elif namechosen == 'name2' :
    api = ''    #user2 api
    api_hash = ''   #user2 hash token    
 else:
    api = ''    #default api or name3/user3
    api_hash = ''    #default hash for name3/user3

#with TelegramClient('name2', '11499359', '29b41ff92ab1491b4704b4faed754da1') as client:     # francis
 with  TelegramClient(namechosen, api, api_hash) as client:    # xavier britto
  filename = random.choice(my_list)
  random_key = '/home/ec2-user/telethon/s3-list/' + filename
  caption_ = ""

  # randomly choose a caption for chosen image, based on image name category
  if "burn" in filename.casefold():
    caption_ = random.choice(burn)

  elif "reward" in filename.casefold():
    caption_ = random.choice(reward)
  elif "draw" in filename.casefold():
    caption_ = random.choice(draw)
  elif "general" in filename.casefold():
    caption_ = random.choice(general)
  # based on caption is empty or not, file is sent
  if (len(caption_)):
     client.send_file('channel', random_key, caption=caption_)

  else:
     client.send_file('channel', random_key)
 time.sleep(random.choice(time_))

