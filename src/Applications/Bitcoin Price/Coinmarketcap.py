import requests
import time

api_key = 'b364252b-fd81-481f-98e7-56fc4cf7eb82'
threshold = 30000
time_interval = 5 * 60  # In Seconds


def get_btc_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }

    # make a request to the coinmarketcap api
    response = requests.get(url, headers=headers)
    response_json = response.json()  # extract the bitcoin price from the json data
    btc_price = response_json['data'][0]
    return btc_price['quote']['USD']['price']


print(get_btc_price())

