import datetime
import pandas as pd
import time
from pandas.plotting import register_matplotlib_converters
import MetaTrader5 as mt5

def valor_acao():
    tempo = time.time() + 10
    while time.time() < tempo:
        tick = mt5.symbol_info_tick('PETR4')
    return tick.last

for step in range(1,101):
    price=[]
    col =[]
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime('%Y-%m-%d %H:%M:%S')
    time.sleep(2)
    tick = mt5.symbol_info_tick('PETR4')
    price.append(tick.last)

    col = [time_stamp]
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('real time stock data.csv', mode ='a', header=False)
    print(col)