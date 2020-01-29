# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

import ccxtpro
import ccxt.async_support as ccxt
from ccxt.base.errors import ExchangeError


class bitfinex(ccxtpro.Exchange, ccxt.bitfinex):

    def describe(self):
        return self.deep_extend(super(bitfinex, self).describe(), {
            'has': {
                'watchTicker': True,
                'watchOrderBook': True,
            },
            'urls': {
                'api': {
                    'ws': {
                        'public': 'wss://api.bitfinex.com/ws/1',
                        'private': 'wss://api.bitfinex.com/ws/1',
                    },
                },
            },
        })

    async def watch_ticker(self, symbol, params={}):
        await self.load_markets()
        market = self.market(symbol)
        marketId = market['id']
        url = self.urls['api']['ws']['public']
        channel = 'ticker'
        request = {
            'event': 'subscribe',
            'channel': channel,
            'symbol': marketId,
        }
        messageHash = channel + ':' + marketId
        return await self.watch(url, messageHash, self.deep_extend(request, params), messageHash)

    def handle_ticker(self, client, message, subscription):
        #
        #     [
        #         1231,
        #         'hb',
        #     ]
        #
        if message[1] == 'hb':
            return  # skip ticker heartbeats
        #
        #     [
        #         2,             # 0 CHANNEL_ID integer Channel ID
        #         236.62,        # 1 BID float Price of last highest bid
        #         9.0029,        # 2 BID_SIZE float Size of the last highest bid
        #         236.88,        # 3 ASK float Price of last lowest ask
        #         7.1138,        # 4 ASK_SIZE float Size of the last lowest ask
        #         -1.02,         # 5 DAILY_CHANGE float Amount that the last price has changed since yesterday
        #         0,             # 6 DAILY_CHANGE_PERC float Amount that the price has changed expressed in percentage terms
        #         236.52,        # 7 LAST_PRICE float Price of the last trade.
        #         5191.36754297,  # 8 VOLUME float Daily volume
        #         250.01,        # 9 HIGH float Daily high
        #         220.05,        # 10 LOW float Daily low
        #     ]
        #
        timestamp = self.milliseconds()
        marketId = self.safe_string(subscription, 'pair')
        market = self.markets_by_id[marketId]
        symbol = market['symbol']
        channel = 'ticker'
        messageHash = channel + ':' + marketId
        last = self.safe_float(message, 7)
        change = self.safe_float(message, 5)
        open = None
        if (last is not None) and (change is not None):
            open = last - change
        result = {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_float(message, 9),
            'low': self.safe_float(message, 10),
            'bid': self.safe_float(message, 1),
            'bidVolume': None,
            'ask': self.safe_float(message, 3),
            'askVolume': None,
            'vwap': None,
            'open': open,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': change,
            'percentage': self.safe_float(message, 6),
            'average': None,
            'baseVolume': self.safe_float(message, 8),
            'quoteVolume': None,
            'info': message,
        }
        self.tickers[symbol] = result
        client.resolve(result, messageHash)

    async def watch_order_book(self, symbol, limit=None, params={}):
        if limit is not None:
            if (limit != 25) and (limit != 100):
                raise ExchangeError(self.id + ' watchOrderBook limit argument must be None, 25 or 100')
        await self.load_markets()
        market = self.market(symbol)
        marketId = market['id']
        url = self.urls['api']['ws']['public']
        channel = 'book'
        request = {
            'event': 'subscribe',
            'channel': channel,
            'symbol': marketId,
            # 'prec': 'P0',  # string, level of price aggregation, 'P0', 'P1', 'P2', 'P3', 'P4', default P0
            # 'freq': 'F0',  # string, frequency of updates 'F0' = realtime, 'F1' = 2 seconds, default is 'F0'
            # 'len': '25',  # string, number of price points, '25', '100', default = '25'
        }
        if limit is not None:
            request['len'] = str(limit)
        messageHash = channel + ':' + marketId
        future = self.watch(url, messageHash, self.deep_extend(request, params), messageHash)
        return await self.after(future, self.limit_order_book, symbol, limit, params)

    def limit_order_book(self, orderbook, symbol, limit=None, params={}):
        return orderbook.limit(limit)

    def handle_order_book(self, client, message, subscription):
        #
        # first message(snapshot)
        #
        #     [
        #         18691,  # channel id
        #         [
        #             [7364.8, 10, 4.354802],  # price, count, size > 0 = bid
        #             [7364.7, 1, 0.00288831],
        #             [7364.3, 12, 0.048],
        #             [7364.9, 3, -0.42028976],  # price, count, size < 0 = ask
        #             [7365, 1, -0.25],
        #             [7365.5, 1, -0.00371937],
        #         ]
        #     ]
        #
        # subsequent updates
        #
        #     [
        #         30,     # channel id
        #         9339.9,  # price
        #         0,      # count
        #         -1,     # size > 0 = bid, size < 0 = ask
        #     ]
        #
        marketId = self.safe_string(subscription, 'pair')
        market = self.markets_by_id[marketId]
        symbol = market['symbol']
        channel = 'book'
        messageHash = channel + ':' + marketId
        # if it is an initial snapshot
        if isinstance(message[1], list):
            limit = self.safe_integer(subscription, 'len')
            self.orderbooks[symbol] = self.counted_order_book({}, limit)
            orderbook = self.orderbooks[symbol]
            deltas = message[1]
            for i in range(0, len(deltas)):
                delta = deltas[i]
                amount = -delta[2] if (delta[2] < 0) else delta[2]
                side = 'asks' if (delta[2] < 0) else 'bids'
                bookside = orderbook[side]
                bookside.store(delta[0], amount, delta[1])
            client.resolve(orderbook, messageHash)
        else:
            orderbook = self.orderbooks[symbol]
            amount = -message[3] if (message[3] < 0) else message[3]
            side = 'asks' if (message[3] < 0) else 'bids'
            bookside = orderbook[side]
            bookside.store(message[1], amount, message[2])
            client.resolve(orderbook, messageHash)

    def handle_heartbeat(self, client, message):
        #
        # every second(approx) if no other updates are sent
        #
        #     {"event": "heartbeat"}
        #
        event = self.safe_string(message, 'event')
        client.resolve(message, event)

    def handle_system_status(self, client, message):
        #
        # todo: answer the question whether handleSystemStatus should be renamed
        # and unified as handleStatus for any usage pattern that
        # involves system status and maintenance updates
        #
        #     {
        #         event: 'info',
        #         version: 2,
        #         serverId: 'e293377e-7bb7-427e-b28c-5db045b2c1d1',
        #         platform: {status: 1},  # 1 for operative, 0 for maintenance
        #     }
        #
        return message

    def handle_subscription_status(self, client, message):
        #
        #     {
        #         event: 'subscribed',
        #         channel: 'book',
        #         chanId: 67473,
        #         symbol: 'tBTCUSD',
        #         prec: 'P0',
        #         freq: 'F0',
        #         len: '25',
        #         pair: 'BTCUSD'
        #     }
        #
        channelId = self.safe_string(message, 'chanId')
        client.subscriptions[channelId] = message
        return message

    def sign_message(self, client, messageHash, message, params={}):
        # todo: bitfinex signMessage not implemented yet
        return message

    def handle_message(self, client, message):
        # print(new Date(), message)
        if isinstance(message, list):
            channelId = str(message[0])
            subscription = self.safe_value(client.subscriptions, channelId, {})
            channel = self.safe_string(subscription, 'channel')
            methods = {
                'book': self.handle_order_book,
                # 'ohlc': self.handleOHLCV,
                'ticker': self.handle_ticker,
                # 'trade': self.handleTrades,
            }
            method = self.safe_value(methods, channel)
            if method is None:
                return message
            else:
                return method(client, message, subscription)
        else:
            # todo: add bitfinex handleErrorMessage
            #
            #     {
            #         event: 'info',
            #         version: 2,
            #         serverId: 'e293377e-7bb7-427e-b28c-5db045b2c1d1',
            #         platform: {status: 1},  # 1 for operative, 0 for maintenance
            #     }
            #
            event = self.safe_string(message, 'event')
            if event is not None:
                methods = {
                    'info': self.handle_system_status,
                    # 'book': 'handleOrderBook',
                    'subscribed': self.handle_subscription_status,
                }
                method = self.safe_value(methods, event)
                if method is None:
                    return message
                else:
                    return method(client, message)
