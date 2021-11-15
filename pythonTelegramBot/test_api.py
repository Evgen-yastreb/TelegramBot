import json
import requests
api_key = '5799f29fce6ae77fd2b697e79552d7e7'
base = 'USD'
symbols = 'USD,RUB,'


q = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR')




total_base = json.loads(q.content)
print(total_base)









# url='https://api.exchangeratesapi.io/v1/' + endpoint + '?access_key=' + access_key +'&from=' + from + '&to=' + to + '&amount=' + amount,