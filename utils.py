#libraries
import json

#configuration
with open('config.json') as f:
    config = json.load(f)
    token = config['token']
    guild_id = config['guild_id']
    success_emoji = config['emojis']['success']
    error_emoji = config['emojis']['failure']

#welcome functions
def set_channel(channel_id):
    with open('database.json', 'r') as f:
        database = json.load(f)
    database['channel_id'] = channel_id
    with open('database.json', 'w') as f:
        json.dump(database, f, indent = 4)

def get_channel():
    with open('database.json', 'r') as f:
        database = json.load(f)
    return database['channel_id']

def set_message(message):
    with open('database.json', 'r') as f:
        database = json.load(f)
    database['message'] = message
    with open('database.json', 'w') as f:
        json.dump(database, f, indent = 4)


def get_message():
    with open('database.json', 'r') as f:
        database = json.load(f)
    return database['message']