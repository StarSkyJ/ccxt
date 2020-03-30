'use strict';

//  ---------------------------------------------------------------------------

const ccxt = require ('ccxt');

//  ---------------------------------------------------------------------------

module.exports = class hitbtc2 extends ccxt.hitbtc2 {
    describe () {
        return this.deepExtend (super.describe (), {
            'has': {
                'ws': true,
                'watchTicker': true,
                'watchTickers': false, // not available on exchange side
                'watchTrades': false, // not implemented yet
                'watchOrderBook': true,
                'watchBalance': false, // not implemented yet
                'watchOHLCV': false, // not implemented yet
            },
            'urls': {
                'api': {
                    'ws': 'wss://api.hitbtc.com/api/2/ws',
                },
            },
            'options': {
                'tradesLimit': 1000,
            },
        });
    }

    async watchOrderBook (symbol, limit = undefined, params = {}) {
        await this.loadMarkets ();
        const market = this.market (symbol);
        const url = this.urls['api']['ws'];
        const messageHash = 'orderbook:' + market['id'];
        const request = {
            'method': 'subscribeOrderbook',
            'params': {
                'symbol': market['id'],
            },
            'id': market['id'],
        };
        const future = this.watch (url, messageHash, request, market['id']);
        return await this.after (future, this.limitOrderBook, symbol, limit, params);
    }

    handleOrderBookSnapshot (client, message) {
        const messageData = this.safeValue (message, 'params');
        const marketId = this.safeValue (messageData, 'symbol');
        const market = this.markets_by_id[marketId];
        const symbol = market['symbol'];
        const timestamp = this.safeValue (messageData, 'timestamp');
        const nonce = this.safeValue (messageData, 'sequence');
        if (symbol in this.orderbooks) {
            delete this.orderbooks[symbol];
        }
        this.orderbooks[symbol] = this.orderBook (this.parseOrderBook (messageData, timestamp, 'bid', 'ask', 'price', 'size'));
        const orderbook = this.orderbooks[symbol];
        // Correction of iso8601
        orderbook['datetime'] = timestamp;
        orderbook['nonce'] = nonce;
        const messageHash = 'orderbook:' + marketId;
        client.resolve (orderbook, messageHash);
    }

    handleUpdateOrderbook (client, message) {
        const messageData = this.safeValue (message, 'params');
        const marketId = this.safeValue (messageData, 'symbol');
        const market = this.markets_by_id[marketId];
        const symbol = market['symbol'];
        const timestamp = this.safeValue (messageData, 'timestamp');
        const nonce = this.safeValue (messageData, 'sequence');
        const orderbook = this.orderbooks[symbol];
        this.updateOrders (orderbook['asks'], messageData['ask']);
        this.updateOrders (orderbook['bids'], messageData['bid']);
        orderbook['timestamp'] = timestamp;
        orderbook['datetime'] = timestamp;
        orderbook['nonce'] = nonce;
        this.orderbooks[symbol] = orderbook;
        const messageHash = 'orderbook:' + marketId;
        client.resolve (orderbook, messageHash);
    }

    updateOrders (bookside, data) {
        for (let i = 0; i < data.length; i++) {
            const delta = data[i];
            const price = parseFloat (delta['price']);
            const amount = parseFloat (delta['size']);
            bookside.store (price, amount);
        }
    }

    async watchTicker (symbol, params = {}) {
        await this.loadMarkets ();
        const market = this.market (symbol);
        const url = this.urls['api']['ws'];
        const messageHash = 'ticker:' + market['id'];
        const request = {
            'method': 'subscribeTicker',
            'params': {
                'symbol': market['id'],
            },
            'id': market['id'],
        };
        return await this.watch (url, messageHash, request, market['id']);
    }

    handleTicker (client, message) {
        const messageData = this.safeValue (message, 'params');
        const marketId = this.safeValue (messageData, 'symbol');
        const market = this.markets_by_id[marketId];
        const symbol = market['symbol'];
        const timestamp = this.safeValue (messageData, 'timestamp');
        const last = this.safeFloat (messageData, 'last');
        const open = this.safeFloat (messageData, 'open');
        const change = last - open;
        const average = this.sum (last, open) / 2;
        const percentage = change / open * 100;
        const result = {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': timestamp,
            'high': this.safeFloat (messageData, 'high'),
            'low': this.safeFloat (messageData, 'low'),
            'bid': this.safeFloat (messageData, 'bid'),
            'bidVolume': undefined,
            'ask': this.safeFloat (messageData, 'ask'),
            'askVolume': undefined,
            'vwap': undefined,
            'open': open,
            'close': last,
            'last': last,
            'previousClose': undefined,
            'change': change,
            'percentage': percentage,
            'average': average,
            'baseVolume': this.safeFloat (messageData, 'volume'),
            'quoteVolume': this.safeFloat (messageData, 'volumeQuote'),
            'info': messageData,
        };
        this.tickers[symbol] = result;
        const messageHash = 'ticker:' + marketId;
        client.resolve (result, messageHash);
    }

    signMessage (client, messageHash, message, params = {}) {
        // todo: implement hitbtc2 signMessage
        return message;
    }

    handleNotification (client, message) {
        // TODO
        return message;
    }

    handleMessage (client, message) {
        const methods = {
            'snapshotOrderbook': this.handleOrderBookSnapshot,
            'updateOrderbook': this.handleUpdateOrderbook,
            'ticker': this.handleTicker,
        };
        const event = this.safeString (message, 'method');
        const method = this.safeValue (methods, event);
        if (method === undefined) {
            this.handleNotification (client, message);
        } else {
            method.call (this, client, message);
        }
    }
};
