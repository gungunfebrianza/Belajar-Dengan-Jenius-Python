import asyncio
import os
import sys
from pprint import pprint
import ccxt.async_support as ccxt  # noqa: E402
import ccxt

ex = ccxt.binance({
    'enableRateLimit': True,
})
print(ex.fetchOrderBook('BTC/USDT'))  # print a list of all available exchange classes


