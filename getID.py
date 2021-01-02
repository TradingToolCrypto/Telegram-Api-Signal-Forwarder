from telethon import TelegramClient
import asyncio
import json

with open("config.json") as config:
    config = json.load(config)

try:
    phone = config["tg"]["phone_num"]
    api_id = config["tg"]["app_id"]
    api_hash = config["tg"]["app_hash"]
except:
    print("There seems to be something wrong with the config!")


async def main():
    client = TelegramClient(phone, api_id, api_hash)
    await client.start(phone)

    check_input = int(input("Type 1 for Groups/DMs/Chats etc. OR Type 2 for Username/Channel/Groups ID searching using tag: "))

    if check_input == 1:
        print("Telegram Entity ID Grabber")
        print("-------------------------------------------------------------")
        i = 0
        dialogs = await client.get_dialogs()
        for x in dialogs:
            print(f"{i}. {x.name}")
            i += 1
        print("-------------------------------------------------------------")
        choice = int(input("Which channel/group/DM do you want the ID of? Use the number! "))
        try:
            print(dialogs[choice].entity.id)
        except IndexError:
            print("You need to use the number assigned to the dialog name.")
    elif check_input == 2:
        getUsername = input("Enter the tag: ")
        getEntity = await client.get_entity(getUsername)
        print(f"Here is the ID {getEntity.id}")


asyncio.get_event_loop().run_until_complete(main())
