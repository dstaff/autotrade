from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from datetime import datetime, timedelta
import MetaTrader5 as mt5
import time
import re

if not mt5.initialize():
    print("Error al conectar con MetaTrader 5")
    mt5.shutdown()
    quit()

# Obtener la cuenta actualmente conectada
account_info = mt5.account_info()
print("Cuenta:", account_info)

symbol = "XAUUSD"

api_id = '26931421'
api_hash = 'd16501751e313ecf52fed51ab74fe26f'

def start_trade(text):
    # Extract GOLD/SELL or GOLD/CALL and range
    pattern_header = re.compile(r'GOLD (SELL|CALL) (\d+\.\d+)-(\d+\.\d+)')
    match_header = pattern_header.search(text)
    if match_header:
        direction = match_header.group(1)
        low_range = match_header.group(2)
        high_range = match_header.group(3)
        print(f"Direction: {direction}")
        print(f"Low Range: {low_range}")
        print(f"High Range: {high_range}")

    # Extract target prices (TP)
    pattern_tp = re.compile(r'TP=(\d+\.\d+)')
    matches_tp = pattern_tp.findall(text)
    if matches_tp:
        print("\nTarget Prices:")
        print("TP1: ",matches_tp[0])
        print("TP2: ",matches_tp[1])
        print("TP3: ",matches_tp[2])
        #for tp in matches_tp:
            #print(tp)

    # Extract stop loss (SL)
    pattern_sl = re.compile(r'SL=(\d+\.\d+)')
    match_sl = pattern_sl.search(text)
    if match_sl:
        sl = match_sl.group(1)
        print(f"\nStop Loss: {sl}")

    if match_sl and matches_tp and match_header:
        print("Trade Launched")

def main():

    with TelegramClient('session_name', api_id, api_hash) as client:
    
        client.connect()
        while True:
            end_date = datetime.now()
            start_date = end_date + timedelta(hours=5)
            print("#####INICIA#####")
            print(datetime.now())
            
            history = client(GetHistoryRequest(
                    peer=-1001691932266,
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

                        start_trade(message.message)

                except Exception as e:
                    print(f"Error: {e}")
                    pass
                                
            print("#####FINALIZA#####")
            print(datetime.now())
            time.sleep(10)

if __name__ == '__main__':
    main()