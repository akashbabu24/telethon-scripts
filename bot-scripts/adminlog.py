from telethon.sync import TelegramClient
from telethon import functions, types

#get kicked user list
#populate api and hash and session name below
with TelegramClient(name, api, hash) as client3:
    result = client3(functions.channels.GetAdminLogRequest(
        channel='channel_name',
        q='',
        max_id=0,
        min_id=0,
        limit=100,
        #admins=(types.InputChannel(user_id=210944655)),
        events_filter=types.ChannelAdminLogEventsFilter(
            kick=True,
            unkick=True,
        )
    ))
    print(result.stringify())
