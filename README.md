# Telegram-Api-Signal-Forwarder

pip install telethon 

To start off, you need to head to https://my.telegram.org and create an app which returns `app_id` and `app_hash`.


Now we can input these values into the config:

**app_id** - Integer

**api_hash** - String

**phone_num** - String, phone number used to sign in telegram

# telegram_chats 
- List of channel IDs you want to watch the messages

# telegram_recievers 
- List of channel IDs you want to relay to

Q: Wanna get the id's of the rooms?
A: Run getID.py

Q: How to run the relay?
A: Edit the config.json file and paste the id's in the telegram_chats and telegram_recievers
