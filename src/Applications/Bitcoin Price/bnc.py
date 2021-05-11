from binance.client import Client

api_key = "KWtCRlBZvgKTYF9GGj29WDGB2Pyl4IpLKySuIy89XYwlD8NgFmuYJgzeX5p4w3ef"
api_secret = "RtqWaTVphzdYgLsyERUKN7dZsoOm4ajAfqhu6kI4BdeIwcpBLoGIpO8F98K87olY"

client = Client(api_key, api_secret)
prices = client.get_all_tickers()
print(prices)
