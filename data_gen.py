import csv
import datetime
import time
import MetaTrader5 as mt5

tick = mt5.symbol_info_tick('PETR4')
tick2 = mt5.symbol_info_tick('PETR4F')

x_value = 0
acao = 0
frac = 0

fieldnames = ["x_value", "bid", "ask"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "bid": bid,
            "ask": ask
        }

        csv_writer.writerow(info)
        print(x_value, bid, ask)

        time_stamp = datetime.datetime.now()
        x_value = time_stamp.strftime('%Y-%m-%d %H:%M:%S')

        bid = tick.bid
        ask = tick.ask

    time.sleep(1)