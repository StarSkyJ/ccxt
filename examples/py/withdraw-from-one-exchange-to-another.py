import ccxt
import sys
from pprint import pprint

print('python', sys.version)
print('CCXT Version:', ccxt.__version__)

binance = ccxt.binance({
    "apiKey": 'YOUR_BINANCE_API_KEY',
    "secret": 'YOUR_BINANCE_SECRET',
    'options': {
        'fetchCurrencies': True,
    },
})
binance.verbose = True

kucoin = ccxt.kucoin({
    'apiKey': 'YOUR_KUCOIN_API_KEY',
    'secret': 'YOUR_KUCOIN_SECRET',
    'password': 'YOUR_KUCOIN_API_PASSWORD',
})
kucoin.verbose = True

binance.load_markets()
kucoin.load_markets()

code = 'USDT'
amount = 40

deposit = binance.fetchDepositAddress(code, {'network': 'TRX'})

print('-----------------------------------------------------------')
print(deposit)
print('-----------------------------------------------------------')

withdrawal = kucoin.withdraw(
    code, amount, deposit['address'], deposit['tag'], {'chain': 'TRC20'})

print('-----------------------------------------------------------')

pprint(withdrawal)
