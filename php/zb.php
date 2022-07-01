<?php

namespace ccxtpro;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

use Exception; // a common import
use \ccxt\ExchangeError;

class zb extends \ccxt\async\zb {

    use ClientTrait;

    public function describe() {
        return $this->deep_extend(parent::describe (), array(
            'has' => array(
                'ws' => true,
                'watchOrderBook' => true,
                'watchTicker' => true,
                'watchTrades' => true,
            ),
            'urls' => array(
                'api' => array(
                    'ws' => 'wss://api.{hostname}/websocket',
                ),
            ),
            'options' => array(
                'tradesLimit' => 1000,
                'ordersLimit' => 1000,
                'OHLCVLimit' => 1000,
            ),
        ));
    }

    public function watch_public($name, $symbol, $method, $params = array ()) {
        yield $this->load_markets();
        $market = $this->market($symbol);
        $messageHash = $market['baseId'] . $market['quoteId'] . '_' . $name;
        $url = $this->implode_hostname($this->urls['api']['ws']);
        $request = array(
            'event' => 'addChannel',
            'channel' => $messageHash,
        );
        $message = array_merge($request, $params);
        $subscription = array(
            'name' => $name,
            'symbol' => $symbol,
            'marketId' => $market['id'],
            'messageHash' => $messageHash,
            'method' => $method,
        );
        return yield $this->watch($url, $messageHash, $message, $messageHash, $subscription);
    }

    public function watch_ticker($symbol, $params = array ()) {
        return yield $this->watch_public('ticker', $symbol, array($this, 'handle_ticker'), $params);
    }

    public function handle_ticker($client, $message, $subscription) {
        //
        //     {
        //         date => '1624398991255',
        //         $ticker => array(
        //             high => '33298.38',
        //             vol => '56375.9469',
        //             last => '32396.95',
        //             low => '28808.19',
        //             buy => '32395.81',
        //             sell => '32409.3',
        //             turnover => '1771122527.0000',
        //             open => '31652.44',
        //             riseRate => '2.36'
        //         ),
        //         dataType => 'ticker',
        //         $channel => 'btcusdt_ticker'
        //     }
        //
        $symbol = $this->safe_string($subscription, 'symbol');
        $channel = $this->safe_string($message, 'channel');
        $market = $this->market($symbol);
        $data = $this->safe_value($message, 'ticker');
        $data['date'] = $this->safe_value($message, 'date');
        $ticker = $this->parse_ticker($data, $market);
        $ticker['symbol'] = $symbol;
        $this->tickers[$symbol] = $ticker;
        $client->resolve ($ticker, $channel);
        return $message;
    }

    public function watch_trades($symbol, $since = null, $limit = null, $params = array ()) {
        $trades = yield $this->watch_public('trades', $symbol, array($this, 'handle_trades'), $params);
        if ($this->newUpdates) {
            $limit = $trades->getLimit ($symbol, $limit);
        }
        return $this->filter_by_since_limit($trades, $since, $limit, 'timestamp', true);
    }

    public function handle_trades($client, $message, $subscription) {
        //
        //     {
        //         $data => array(
        //             array( date => 1624537147, amount => '0.0357', price => '34066.11', trade_type => 'bid', type => 'buy', tid => 1718857158 ),
        //             array( date => 1624537147, amount => '0.0255', price => '34071.04', trade_type => 'bid', type => 'buy', tid => 1718857159 ),
        //             array( date => 1624537147, amount => '0.0153', price => '34071.29', trade_type => 'bid', type => 'buy', tid => 1718857160 )
        //         ),
        //         dataType => 'trades',
        //         $channel => 'btcusdt_trades'
        //     }
        //
        $channel = $this->safe_value($message, 'channel');
        $symbol = $this->safe_string($subscription, 'symbol');
        $market = $this->market($symbol);
        $data = $this->safe_value($message, 'data');
        $trades = $this->parse_trades($data, $market);
        $tradesArray = $this->safe_value($this->trades, $symbol);
        if ($tradesArray === null) {
            $limit = $this->safe_integer($this->options, 'tradesLimit', 1000);
            $tradesArray = new ArrayCache ($limit);
        }
        for ($i = 0; $i < count($trades); $i++) {
            $tradesArray->append ($trades[$i]);
        }
        $this->trades[$symbol] = $tradesArray;
        $client->resolve ($tradesArray, $channel);
    }

    public function watch_order_book($symbol, $limit = null, $params = array ()) {
        if ($limit !== null) {
            if (($limit !== 5) && ($limit !== 10) && ($limit !== 20)) {
                throw new ExchangeError($this->id . ' watchOrderBook $limit argument must be null, 5, 10 or 20');
            }
        } else {
            $limit = 5; // default
        }
        yield $this->load_markets();
        $market = $this->market($symbol);
        $name = 'quick_depth';
        $messageHash = $market['baseId'] . $market['quoteId'] . '_' . $name;
        $url = $this->urls['api']['ws'] . '/' . $market['baseId'];
        $request = array(
            'event' => 'addChannel',
            'channel' => $messageHash,
            'length' => $limit,
        );
        $message = array_merge($request, $params);
        $subscription = array(
            'name' => $name,
            'symbol' => $symbol,
            'marketId' => $market['id'],
            'messageHash' => $messageHash,
            'method' => array($this, 'handle_order_book'),
        );
        $orderbook = yield $this->watch($url, $messageHash, $message, $messageHash, $subscription);
        return $orderbook->limit ($limit);
    }

    public function handle_order_book($client, $message, $subscription) {
        //
        //     {
        //         lastTime => 1624524640066,
        //         dataType => 'quickDepth',
        //         $channel => 'btcusdt_quick_depth',
        //         currentPrice => 33183.79,
        //         listDown => array(
        //             array( 33166.87, 0.2331 ),
        //             array( 33166.86, 0.15 ),
        //             array( 33166.76, 0.15 ),
        //             array( 33161.02, 0.212 ),
        //             array( 33146.35, 0.6066 )
        //         ),
        //         market => 'btcusdt',
        //         listUp => array(
        //             array( 33186.88, 0.15 ),
        //             array( 33190.1, 0.15 ),
        //             array( 33193.03, 0.2518 ),
        //             array( 33195.05, 0.2031 ),
        //             array( 33199.99, 0.6066 )
        //         ),
        //         high => 34816.8,
        //         rate => '6.484',
        //         low => 32312.41,
        //         currentIsBuy => true,
        //         dayNumber => 26988.5536,
        //         totalBtc => 26988.5536,
        //         showMarket => 'btcusdt'
        //     }
        //
        $channel = $this->safe_string($message, 'channel');
        $limit = $this->safe_integer($subscription, 'limit');
        $symbol = $this->safe_string($subscription, 'symbol');
        $orderbook = $this->safe_value($this->orderbooks, $symbol);
        if ($orderbook === null) {
            $orderbook = $this->order_book(array(), $limit);
            $this->orderbooks[$symbol] = $orderbook;
        }
        $timestamp = $this->safe_integer($message, 'lastTime');
        $parsed = $this->parse_order_book($message, $symbol, $timestamp, 'listDown', 'listUp');
        $orderbook->reset ($parsed);
        $orderbook['symbol'] = $symbol;
        $client->resolve ($orderbook, $channel);
    }

    public function handle_message($client, $message) {
        //
        //
        //     {
        //         no => '0',
        //         code => 1007,
        //         success => false,
        //         $channel => 'btc_usdt_ticker',
        //         $message => 'Channel is empty'
        //     }
        //
        //     {
        //         date => '1624398991255',
        //         ticker => array(
        //             high => '33298.38',
        //             vol => '56375.9469',
        //             last => '32396.95',
        //             low => '28808.19',
        //             buy => '32395.81',
        //             sell => '32409.3',
        //             turnover => '1771122527.0000',
        //             open => '31652.44',
        //             riseRate => '2.36'
        //         ),
        //         $dataType => 'ticker',
        //         $channel => 'btcusdt_ticker'
        //     }
        //
        //     {
        //         data => array(
        //             array( date => 1624537147, amount => '0.0357', price => '34066.11', trade_type => 'bid', type => 'buy', tid => 1718857158 ),
        //             array( date => 1624537147, amount => '0.0255', price => '34071.04', trade_type => 'bid', type => 'buy', tid => 1718857159 ),
        //             array( date => 1624537147, amount => '0.0153', price => '34071.29', trade_type => 'bid', type => 'buy', tid => 1718857160 )
        //         ),
        //         $dataType => 'trades',
        //         $channel => 'btcusdt_trades'
        //     }
        //
        $dataType = $this->safe_string($message, 'dataType');
        if ($dataType !== null) {
            $channel = $this->safe_string($message, 'channel');
            $subscription = $this->safe_value($client->subscriptions, $channel);
            if ($subscription !== null) {
                $method = $this->safe_value($subscription, 'method');
                if ($method !== null) {
                    return $method($client, $message, $subscription);
                }
            }
            return $message;
        }
    }
}
