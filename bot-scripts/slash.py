from telethon.sync import TelegramClient, events, types
import time


slash = True
with  TelegramClient(session_name, telegram_api, telegram_hash) as client: #Replace session_name, api and hash with telegram user app config that created from https://my.telegram.org/apps

 # if start1 command is sent on chat, slogan repeat logic starts
 @client.on(events.NewMessage(pattern='(?i)start1'))
 async def handler(event):
    global slash
    print(slash)
    slash = True
    print(slash)
 
 # if stop1 command is sent on chat, slogan repeat logic stops
 @client.on(events.NewMessage(pattern='(?i)stop1'))
 async def handler(event):
    global slash
    print(slash)
    slash = False
    print(slash)

 # If the / slogan is raised by someone, repeat the same in given intervals
 @client.on(events.NewMessage(pattern='(?i)/SILENCE_BEFORE_STORM'))
 async def handler(event):
     global slash
     while(slash == True):
        for i in range(len(captions)):
          time.sleep(2)
          await event.respond('/SILENCE_BEFORE_STORM')
        if slash != True:
          break
        time.sleep(35)

 @client.on(events.NewMessage(pattern='(?i)/TO_MOON'))
 async def handler(event):
     global slash
     while(slash == True):
        for i in range(len(captions)):
          time.sleep(3)
          await event.respond('/TO_MOON')
        if slash != True:
          break
        time.sleep(30)
 
 # automatic greeting
 @client.on(events.NewMessage(pattern='(?i)hi|hello|hey'))
 async def handler(event):
    await event.respond('Hey! Welcome to LuckyShibaInu, one of the most promising projects on BSC')

 client.run_until_disconnected()    # run till disconnected

