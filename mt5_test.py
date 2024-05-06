import MetaTrader5 as mt5
import time
import os

# Conectar con MetaTrader 5
if not mt5.initialize():
    print("Error al conectar con MetaTrader 5")
    mt5.shutdown()
    quit()

# Obtener la cuenta actualmente conectada
#account_info = mt5.account_info()
#print("Cuenta:", account_info)

symbol = "XAUUSD"

while True:
    # Obtener la información del tick (precio actual) del activo
    tick_info = mt5.symbol_info_tick(symbol)
    if tick_info is None:
        print(f"No se pudo obtener la información del tick para {symbol}")
    else:
        thebid = tick_info.bid#int(tick_info.bid)#quitar decimales
        theask = tick_info.ask#int(tick_info.ask)#quitar decimales
        print(f"Precio actual de {symbol}: Bid={thebid}, Ask={theask}")

    time.sleep(1)
    os.system("cls")

# Cerrar la conexión con MetaTrader 5
mt5.shutdown()