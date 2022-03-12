from telethon.tl.functions.messages import GetAllStickersRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID
import time
import random
from telethon.sync import TelegramClient
from telethon import functions, types

#user choice list
session_list = ['user1', 'user2']

#delay timer list
time_ = [100, 250, 360, 560, 650]

#choose any one of first 5 sticker packs randomly
sticker_pack = [1, 2, 3, 4, 5]

while True:
 namechosen = random.choice(session_list)

 if namechosen == 'user1':
    api = ''      #user1 api and hash values
    api_hash = ''
 elif namechosen == 'user2' :
    api = ''   #insert api of your user2
    api_hash = ''   #insert hash of user2 from https://my.telegram.org/apps
 
 with  TelegramClient(namechosen, api, api_hash) as client:
    # Get all the sticker sets this user has
  sticker_sets = client(GetAllStickersRequest(0))

# Choose a sticker set
  sticker_set = sticker_sets.sets[random.choice(sticker_pack)]

# Get the stickers for this sticker set
  stickers = client(GetStickerSetRequest(
    stickerset=InputStickerSetID(
        id=sticker_set.id, access_hash=sticker_set.access_hash
    )
  ))
 
  chosen_sticker = random.choice(stickers.documents)
# Stickers are nothing more than files, so send that
  client.send_file('channel', chosen_sticker)
 time.sleep(random.choice(time_))
