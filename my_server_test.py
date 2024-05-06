from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from datetime import datetime, timedelta
import difflib
import time
import requests

nombres_a_buscar = ['𝘿𝙍𝙀𝘼𝙈 𝙂𝙊𝙇𝘿 𝙀𝙓𝙋𝙀𝙍𝙏', 'GOLD SCALPER', 'GOLD KING VIP', 'XAUUSD GOLD SIGNAL', 'EXNESS CAREERS', 'FOREX KING', 
                    'FOREX FACTORY TRADING', 'EU Gold VIP', 'TRADING CARTEL OFFICIAL', 
                    'FREE FOREX SIGNALS', 'GOLD FOREX SIGNALS (Free)', 'NasGold Trade Signals','𝐓𝐑𝐀𝐃𝐈𝐍𝐆 𝐌𝐀𝐒𝐓𝐄𝐑', 'James Gold Master', 
                    'BLASTER TRADER', 'VIP Premium Scaping', 'UNIQUE FX', 'ForexKing', '𝐓𝐇𝐄 𝐆𝐎𝐋𝐃 𝐋𝐄𝐆𝐄𝐍𝐃', 'ERVINE GOLD MASTER', 
                    'XAUUSD/GOLD FREE SINGNAL']

api_id = '26931421'
api_hash = 'd16501751e313ecf52fed51ab74fe26f'
TOKEN = '5087546896:AAG97KvqT6PHcr1GnTyuikWi01vS2Amja0Y'
CHAT_ID = '@mispruebasdstaff'

def main():

    with TelegramClient('session_name', api_id, api_hash) as client:
    
        client.connect()

        end_date = datetime.now()
        start_date = end_date + timedelta(hours=5)

        print("#####INICIA#####")
        print(datetime.now())
            
        dialogs = client.get_dialogs()
            
        # Archivo de salida
        output_file = 'ultimos_mensajes.txt'
        with open(output_file, 'w', encoding='utf-8') as file:

            for dialog in dialogs:

                if dialog.is_group or dialog.is_channel:
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
                                nombres_similares = dialog.name in nombres_a_buscar
                                if nombres_similares:
                                    #print(f"TELEGRAM: {message.date}")
                                    current_message_date = message.date - timedelta(hours=5)

                                    if (message.message.lower().find("sl hit") != -1 
                                        or message.message.lower().find("recovery setup") != -1 
                                        or message.message.lower().find("invalidate") != -1
                                        or message.message.lower().find("recovery trade") != -1):
                                        
                                        print(f"NAME: {dialog.name}")
                                        print(f"{current_message_date}: {message.message}")
                                        
                                        messageToSend = dialog.name + " - LOCAL: " + str(current_message_date) + " - REMOTE: " + str(message.date) + " => " + message.message
                                        
                                        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={messageToSend}"
                                        r = requests.get(url)
                                            
                                        file.write(f"{dialog.name} - REMOTE: {message.date} | LOCAL: {current_message_date} - {message.message}\n")
                        except Exception as e:
                            print(f"Error: {e}")
                            pass

            print("#####FINALIZA#####")
            print(datetime.now())

if __name__ == '__main__':
    main()
