import re
from telethon import TelegramClient, events, utils
import logging
import json

logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M',
                    level=logging.INFO)

logger = logging.getLogger("telerelay")

with open("config.json") as config:
    config = json.load(config)
try:
    phone = config["tg"]["phone_num"]
    api_id = config["tg"]["app_id"]
    api_hash = config["tg"]["app_hash"]
    channelIds = config["tg"]["telegram_chats"]
    recievers = config["tg"]["telegram_recievers"]
except:
    logger.error("There seems to be something wrong with the config!")

client = TelegramClient(phone, api_id, api_hash).start(phone)

crypto_currencies = [
    "AUDCAD",
    "AUDCHF",
    "AUDHKD",
    "AUDJPY",
    "AUDNZD",
    "AUDSGD",
    "AUDUSD",
    "CADCHF",
    "CADHKD",
    "CADJPY",
    "CADSGD",
    "CHFHKD",
    "CHFJPY",
    "CHFZAR",
    "EURAUD",
    "EURCAD",
    "EURCHF",
    "EURCZK",
    "EURDKK",
    "EURGBP",
    "EURHKD",
    "EURHUF",
    "EURJPY",
    "EURNOK",
    "EURNZD",
    "EURPLN",
    "EURSEK",
    "EURSGD",
    "EURTRY",
    "EURUSD",
    "EURZAR",
    "GBPAUD",
    "GBPCAD",
    "GBPCHF",
    "GBPHKD",
    "GBPJPY",
    "GBPNZD",
    "GBPPLN",
    "GBPSGD",
    "GBPUSD",
    "GBPZAR",
    "HKDJPY",
    "NZDCAD",
    "NZDCHF",
    "NZDHKD",
    "NZDJPY",
    "NZDSGD",
    "NZDUSD",
    "SGDCHF",
    "SGDHKD",
    "SGDJPY",
    "TRYJPY",
    "USDCAD",
    "USDCHF",
    "USDCNH",
    "USDCZK",
    "USDDKK",
    "USDHKD",
    "USDHUF",
    "USDJPY",
    "USDMXN",
    "USDNOK",
    "USDPLN",
    "USDSAR",
    "USDSEK",
    "USDSGD",
    "USDTHB",
    "USDTRY",
    "USDZAR",
    "ZARJPY",
    "BTCUSD"
]

currencies = [
    "AUDCAD",
    "AUDCHF",
    "AUDHKD",
    "AUDJPY",
    "AUDNZD",
    "AUDSGD",
    "AUDUSD",
    "CADCHF",
    "CADHKD",
    "CADJPY",
    "CADSGD",
    "CHFHKD",
    "CHFJPY",
    "CHFZAR",
    "EURAUD",
    "EURCAD",
    "EURCHF",
    "EURCZK",
    "EURDKK",
    "EURGBP",
    "EURHKD",
    "EURHUF",
    "EURJPY",
    "EURNOK",
    "EURNZD",
    "EURPLN",
    "EURSEK",
    "EURSGD",
    "EURTRY",
    "EURUSD",
    "EURZAR",
    "GBPAUD",
    "GBPCAD",
    "GBPCHF",
    "GBPHKD",
    "GBPJPY",
    "GBPNZD",
    "GBPPLN",
    "GBPSGD",
    "GBPUSD",
    "GBPZAR",
    "HKDJPY",
    "NZDCAD",
    "NZDCHF",
    "NZDHKD",
    "NZDJPY",
    "NZDSGD",
    "NZDUSD",
    "SGDCHF",
    "SGDHKD",
    "SGDJPY",
    "TRYJPY",
    "USDCAD",
    "USDCHF",
    "USDCNH",
    "USDCZK",
    "USDDKK",
    "USDHKD",
    "USDHUF",
    "USDJPY",
    "USDMXN",
    "USDNOK",
    "USDPLN",
    "USDSAR",
    "USDSEK",
    "USDSGD",
    "USDTHB",
    "USDTRY",
    "USDZAR",
    "ZARJPY"

]


"""RECIEVING THE MESSAGES"""

@client.on(events.NewMessage(chats=channelIds))
async def msg_handler(event):
    sender = await event.get_sender()
    name = utils.get_display_name(sender)
    msg = event.message.message

    logger.info(f"Message arrived from {name}\nMessage:\n{msg}\n\n")

    if ("Adjusting" in msg) or ("adjusting" in msg) or ("correction" in msg):

        if "Adjusting" in msg:

            if 'SL' in msg:
                try:
                    sep = [i for i in currencies if i in msg]
                    idx = msg.find(sep[0])
                    aa = msg[idx:]

                    msg2 = msg.find("Adjusting")
                    msg = msg[msg2:]
                    msg = msg.replace("Adjusting", "").replace(msg[idx:], aa).replace("to", "").replace("SL",
                                                                                                        "\nMOVE SL")
                    await client.send_message(recievers, msg)
                    print('Found the Filtered word in the message SL: \n' + msg)

                except Exception:
                    logger.error("Something happened while sending the relay message containing media\n{e}")

                    if "EA" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("EA", "EURAUD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message EA: \n' + msg)


                    elif "BTCUSD" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("BTCUSD", "BTCUSD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message BTCUSD: \n' + msg)


                    elif "XAGUSD" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("XAGUSD", "XAGUSD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message XAGUSD: \n' + msg)


                    elif "CJ" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("CJ", "CADJPY\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message CJ: \n' + msg)


                    elif "UADCAD" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("UADCAD", "USDCAD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message UADCAD: \n' + msg)


                    elif "EU" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("EU", "EURUSD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message EU: \n' + msg)


                    elif "NU" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("NU", "NZDUSD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message NU: \n' + msg)


                    elif "UJ" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("UJ", "USDJPY\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message UJ: \n' + msg)


                    elif "UCad" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("UCad", "USDCAD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message UCad: \n' + msg)


                    elif "EJ" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("EJ", "EURJPY\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message EJ: \n' + msg)


                    elif "GA" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("GA", "GBPAUD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message GA: \n' + msg)


                    elif "AJ" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("AJ", "AUDJPY\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message AJ: \n' + msg)


                    elif "AN" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("AN", "AUDNZD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message AN: \n' + msg)


                    elif "GU" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("GU", "GBPUSD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message GU: \n' + msg)

                    elif "Gold" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("Gold", "XAUUSD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message Gold: \n' + msg)


                    elif "AU" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("AU", "AUDUSD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message AU: \n' + msg)


                    elif "EN" in msg:
                        msg2 = msg.find("Adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("EN", "EURNZD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message EN: \n' + msg)


                    else:
                        await client.send_message(recievers, msg)

        if "adjusting" in msg:

            if 'SL' in msg:

                try:
                    sep = [i for i in currencies if i in msg]
                    idx = msg.find(sep[0])
                    aa = msg[idx:]

                    msg2 = msg.find("Adjusting")
                    msg = msg[msg2:]
                    msg = msg.replace("Adjusting", "").replace(msg[idx:], aa).replace("to", "").replace("SL",
                                                                                                        "\nMOVE SL")
                    print('Found the Filtered word in the message SL: \n' + msg)
                    await client.send_message(recievers, msg)


                except Exception:
                    logger.error("Something happened while sending the relay message\n{e}")

                    if "EA" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("EA", "EURAUD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message EA: \n' + msg)


                    elif "BTCUSD" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("BTCUSD", "BTCUSD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message BTCUSD: \n' + msg)


                    elif "XAGUSD" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("XAGUSD", "XAGUSD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message XAGUSD: \n' + msg)


                    elif "CJ" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("CJ", "CADJPY\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message CJ: \n' + msg)


                    elif "UADCAD" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("UADCAD", "USDCAD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message UADCAD: \n' + msg)


                    elif "EU" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("Adjusting", "").replace("EU", "EURUSD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message EU: \n' + msg)


                    elif "NU" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("NU", "NZDUSD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message NU: \n' + msg)


                    elif "UJ" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("UJ", "USDJPY\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message UJ: \n' + msg)


                    elif "UCad" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("UCad", "USDCAD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message UCad: \n' + msg)


                    elif "EJ" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("EJ", "EURJPY\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message EJ: \n' + msg)


                    elif "GA" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("GA", "GBPAUD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message GA: \n' + msg)


                    elif "AJ" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("AJ", "AUDJPY\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message AJ: \n' + msg)


                    elif "AN" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("AN", "AUDNZD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message AN: \n' + msg)


                    elif "GU" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("GU", "GBPUSD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message GU: \n' + msg)

                    elif "Gold" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("Gold", "XAUUSD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message Gold: \n' + msg)


                    elif "AU" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("AU", "AUDUSD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message AU: \n' + msg)


                    elif "EN" in msg:
                        msg2 = msg.find("adjusting")
                        msg = msg[msg2:]
                        msg = msg.replace("adjusting", "").replace("EN", "EURNZD\nMOVE").replace("to", "")
                        await client.send_message(recievers, msg)
                        print('Found the Filtered word in the message EN: \n' + msg)


                    else:
                        await client.send_message(recievers, msg)

        if "correction" in msg:

            if 'SL' in msg:
                msg = msg.replace("*correction*", "\nMOVE")
                await client.send_message(recievers, msg)
                print('Found the Filtered word in the message SL: \n' + msg)

    if ("🎯" in msg) and ("TP1" in msg):
        print("UN-PARSED SIGNAL MESSAGE =>\n" + msg)

        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   "]+", flags=re.UNICODE)

        no_emoji = emoji_pattern.sub(r'', msg)
        clean = no_emoji.replace('20 Pips', '').replace('40 Pips', '').replace('100 Pips', '')

        print("PARSED NO EMOJI SIGNAL MESSAGE =>\n" + clean)

        sep = [i for i in crypto_currencies if i in clean]

        idx = clean.find(sep[0])
        textc = clean[idx:]
        idxc2 = textc.find('*')
        final = textc[:idxc2]
        await client.send_message(recievers, final)
        print("FINAL PARSED SIGNAL MESSAGE =>\n" + final)




with client:
    client.run_until_disconnected()
