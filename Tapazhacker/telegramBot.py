from telethon import TelegramClient, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 19855239
api_hash = 'def48dad2da9270981c6da76a77f1725'

client = TelegramClient('session_name', api_id, api_hash).start()

# Getting information about yourself
me = client.get_me()
print(me.stringify())

# Sending a message (you can use 'me' or 'self' to message yourself)
client.send_message('username', 'Hello World from Telethon!')

# Sending a file
#client.send_file('username', '/home/myself/Pictures/holidays.jpg')

# Retrieving messages from a chat
from telethon import utils
for message in client.iter_messages('username', limit=10):
    print(utils.get_display_name(message.sender), message.message)

# Listing all the dialogs (conversations you have open)
for dialog in client.get_dialogs(limit=10):
    print(dialog.name, dialog.draft.text)

# Downloading profile photos (default path is the working directory)
client.download_profile_photo('username')

# Once you have a message with .media (if message.media)
# you can download it using client.download_media(),
# or even using message.download_media():
messages = client.get_messages('username')
messages[0].download_media()