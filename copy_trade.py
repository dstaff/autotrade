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

def check_signal(text):
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
    
    # Verfica el precio actual
    tick_info = mt5.symbol_info_tick(symbol)

    print(f"Precio actual de {symbol}: Bid={tick_info.bid}, Ask={tick_info.ask}")

    if match_sl and matches_tp and match_header:

        if tick_info is None:
            print(f"No se pudo obtener la información del tick para {symbol}")
        else:
            thebid = int(tick_info.bid)#quitar decimales
            theask = int(tick_info.ask)#quitar decimales
            #print(f"Precio actual de {symbol}: Bid={thebid}, Ask={theask}")

        if thebid == theask and check_direction(low_range,high_range,thebid,direction):
            launch_trade(thebid,direction,1984,sl,matches_tp[0])

def check_direction(lr,hr,price,dir):
    if dir == "SELL" and lr < hr and price >= lr and price <= hr:
        return True
    elif dir == "BUY" and lr > hr and price <= lr and price >= hr:
        return True
    else:
        return False

def launch_trade(price,dir,magic,stop_loss,take_profit):
    # Abrir una operación de compra

    the_direction = mt5.ORDER_TYPE_BUY if dir == "BUY" else mt5.ORDER_TYPE_SELL

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 1,
        "type": the_direction,
        "price": price,
        "sl": stop_loss,
        "tp": take_profit,
        "magic": magic,
        "comment": "MAGIC TRADE",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("Error al abrir la operación:", result)
        mt5.shutdown()
        quit()
    
    print("Operación abierta con éxito. Ticket:", result.order)
    ticket = result.order

    # Esperar a que la operación se cierre
    wait_for_trade(ticket)

def wait_for_trade(ticket):
    while True:
        order_info = mt5.order_get(ticket)
        if order_info.retcode != mt5.TRADE_RETCODE_DONE:
            # La operación aún no se ha cerrado
            print("Esperando que la operación se cierre...")
            time.sleep(10)  # Esperar 5 segundos antes de volver a verificar
        else:
            # La operación se ha cerrado
            print("La operación se ha cerrado.")
            break
    
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
                    limit=1,
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

                        check_signal(message.message)

                except Exception as e:
                    print(f"Error: {e}")
                    pass
                                
            print("#####FINALIZA#####")
            print(datetime.now())
            time.sleep(2)

if __name__ == '__main__':
    main()