from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from datetime import datetime, timedelta
import time
import telebot

#nombres_a_buscar = ['𝘿𝙍𝙀𝘼𝙈 𝙂𝙊𝙇𝘿 𝙀𝙓𝙋𝙀𝙍𝙏', 
                    #'GOLD SCALPER', 
                    #'GOLD KING VIP', 
                    #'XAUUSD GOLD SIGNAL', 
                    #'EXNESS CAREERS', 
                    #'𝐓𝐑𝐀𝐃𝐈𝐍𝐆 𝐌𝐀𝐒𝐓𝐄𝐑', 
                    #'James Gold Master', 
                    #'BLASTER TRADER', 
                    #'ForexKing', 
                    #'𝐓𝐇𝐄 𝐆𝐎𝐋𝐃 𝐋𝐄𝐆𝐄𝐍𝐃', 
                    #'ERVINE GOLD MASTER', 
                    #'XAUUSD/GOLD FREE SINGNAL']

nombres_a_buscar = ['FOREX KING⚡️',
                    'Gold Signals 98% Sure 😎',
                    'VINCENT GOLD TRADER VIP',
                    '💯 𝗫𝗔𝗨𝗨𝗦𝗗 𝗚𝗢𝗟𝗗 𝗣𝗘𝗥𝗙𝗘𝗖𝗧 𝗦𝗜𝗚𝗡𝗔𝗟𝗦💯',
                    'SMC SIGNAL™️',
                    'Sure VIP Signal (97% Confirm) Free Trial',
                    '📉XAUUSD GOLD SIGNAL📉',
                    'Technical Analyst™',
                    '𝙿𝚘𝚒𝚗𝚝 𝙱𝚘𝚜𝚜 𝚃𝚛𝚊𝚍𝚎𝚛',
                    'FOREX PIPS SEA™⛵',
                    'SMART MONEY TRADiNG(SMC) ™',
                    '𝑮𝑶𝑳𝑫 𝑨𝑵𝑨𝑳𝒀𝑺𝑰𝑺 𝑬𝑿𝑷𝑬𝑹𝑻',
                    '™𝙁𝙊𝙍𝙀𝙓⚡𝙑𝙄𝘾𝙏𝙊𝙍𝙔™',
                    'Forex Signals🔥💰 XAUUSD',
                    '𝙎𝙈𝘾 𝙏𝙀𝘼𝙈']
                    

api_id = '26931421'
api_hash = 'd16501751e313ecf52fed51ab74fe26f'
TOKEN = '5087546896:AAG97KvqT6PHcr1GnTyuikWi01vS2Amja0Y'
CHAT_ID = '@mispruebasdstaff'

bot = telebot.TeleBot(TOKEN)

def main():

    with TelegramClient('session_name', api_id, api_hash) as client:
    
        client.connect()

        while True:
            end_date = datetime.now()
            start_date = end_date + timedelta(hours=5)
            print("#####INICIA#####")
            print(datetime.now())
            
            dialogs = client.get_dialogs()

            for dialog in dialogs:
                #print(f"CHAT: {dialog.name}")
                nombres_similares = dialog.name in nombres_a_buscar
                #nombres_similares = dialog.name == "GOLD KING VIP"
                
                if (dialog.is_group or dialog.is_channel) and nombres_similares:
                    #print(f"CHAT: {dialog.name}")
                    history = client(GetHistoryRequest(
                        peer=dialog.id,
                        limit=5,
                        offset_date=start_date,
                        offset_id=0,
                        add_offset=0,
                        max_id=0,
                        min_id=0,
                        hash=0
                    ))

                    for message in history.messages:

                        try:
                            if not message.message is None:
                                #print(f"CHAT: {dialog.name}")
                                #print(f"MESSAGE TEXT: {message.message}")
                                current_message_date = message.date - timedelta(hours=5)

                                if (message.message.lower().find("sl hit") != -1 
                                or message.message.lower().find("recovery setup") != -1 
                                or message.message.lower().find("invalidate") != -1
                                or message.message.lower().find("recovery trade") != -1):
                                
                                #if (message.message.lower().find("GOLD SELL  TP2=40PIPS") != -1):
                                            
                                    print(f"NAME: {dialog.name}")
                                    print(f"{current_message_date}: {message.message}")

                                    #bot.send_message(CHAT_ID, f"CHAT: {dialog.name} \n- {current_message_date}: {message.message}")

                        except Exception as e:
                            print(f"Error: {e}")
                            pass
                                
            print("#####FINALIZA#####")
            print(datetime.now())
            time.sleep(60)

if __name__ == '__main__':
    main()