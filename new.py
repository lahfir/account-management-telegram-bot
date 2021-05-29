from telethon import TelegramClient, sync

api_id = '4409139'
api_hash = 'b9fd8bddf0ade52b225a37a197701d41'

client = TelegramClient('xxx', api_id, api_hash).start()

# get all the channels that I can access
channels = {d.entity.username: d.entity
            for d in client.get_dialogs()
            if d.is_channel}

# choose the one that I want list users from
channel = channels["hellochannel1234"]

# get all the users and print them
for u in client.get_participants(channel):
    print(u.id, u.first_name, u.last_name, u.username)