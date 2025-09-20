# rest.coincap.io/v3/assets/bitcoin?apiKey=bd394852ae350a2f2a81807f5ad97dcb9f94200dbe7d5c54452e4ec8532f0e48

import sys
import requests

if len(sys.argv) == 2:
    try:
        asset = sys.argv[1]
    except ValueError:
        sys.exit('Command-line argument is not a number')

else:
    sys.exit('Missing command-line argument')

try:
    response = requests.get(f'https://rest.coincap.io/v3/assets/bitcoin?apiKey=bd394852ae350a2f2a81807f5ad97dcb9f94200dbe7d5c54452e4ec8532f0e48')
    response.raise_for_status()

except requests.RequestException:
    sys.exit('There was an exception while handling the api request')

api = response.json()

bit_one = api['bpi']
bit_two = bit_one['USD']
bit_three = bit_two['rate_float']

print(f'${bit_three*asset:,.4f}')









"""
import sys
import requests
import json

if len(sys.argv) == 2:
    try:
        asset = float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number')

else:
    sys.exit('Missing command-line argument')

try:
    response = requests.get(f'https://api.coindesk.com/v1/bpi/currentprice.json')


except requests.RequestException:
    sys.exit('There was an exception while handling the api request')

api = response.json()

bit_one = api['bpi']
bit_two = bit_one['USD']
bit_three = bit_two['rate_float']

print(f'${bit_three*asset:,.4f}')

"""