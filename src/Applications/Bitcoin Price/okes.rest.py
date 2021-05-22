import json
import datetime
import os
import okex.Account_api as Account
import okex.Market_api as Market


def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"


time = get_timestamp()

if __name__ == '__main__':

    api_key = "7b7d4471-dc15-4891-b017-e5ffdd2b7284"
    secret_key = "4C49046150E81FAFDB93560F02F5334F"
    passphrase = "lamborGhini2019"
    flag = '1'  # 模拟盘 demo trading
    # flag = '0'  # 实盘 real trading
accountAPI = Account.AccountAPI(api_key, secret_key, passphrase, False, flag)
result = accountAPI.get_position_risk('SWAP')

marketAPI = Market.MarketAPI(api_key, secret_key, passphrase, False, flag)
# result = marketAPI.get_tickers('SPOT')
print(result)
