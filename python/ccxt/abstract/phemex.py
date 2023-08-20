from ccxt.base.types import Entry


class ImplicitAPI:
    public_get_cfg_v2_products = publicGetCfgV2Products = Entry('cfg/v2/products', 'public', 'GET', {'cost': 5})
    public_get_cfg_fundingrates = publicGetCfgFundingRates = Entry('cfg/fundingRates', 'public', 'GET', {'cost': 5})
    public_get_products = publicGetProducts = Entry('products', 'public', 'GET', {'cost': 5})
    public_get_nomics_trades = publicGetNomicsTrades = Entry('nomics/trades', 'public', 'GET', {'cost': 5})
    public_get_md_kline = publicGetMdKline = Entry('md/kline', 'public', 'GET', {'cost': 5})
    public_get_md_v2_kline_list = publicGetMdV2KlineList = Entry('md/v2/kline/list', 'public', 'GET', {'cost': 5})
    public_get_md_v2_kline = publicGetMdV2Kline = Entry('md/v2/kline', 'public', 'GET', {'cost': 5})
    public_get_md_v2_kline_last = publicGetMdV2KlineLast = Entry('md/v2/kline/last', 'public', 'GET', {'cost': 5})
    public_get_md_orderbook = publicGetMdOrderbook = Entry('md/orderbook', 'public', 'GET', {'cost': 5})
    public_get_md_trade = publicGetMdTrade = Entry('md/trade', 'public', 'GET', {'cost': 5})
    public_get_md_spot_ticker_24hr = publicGetMdSpotTicker24hr = Entry('md/spot/ticker/24hr', 'public', 'GET', {'cost': 5})
    public_get_exchange_public_cfg_chain_settings = publicGetExchangePublicCfgChainSettings = Entry('exchange/public/cfg/chain-settings', 'public', 'GET', {'cost': 5})
    v1_get_md_orderbook = v1GetMdOrderbook = Entry('md/orderbook', 'v1', 'GET', {'cost': 5})
    v1_get_md_trade = v1GetMdTrade = Entry('md/trade', 'v1', 'GET', {'cost': 5})
    v1_get_md_ticker_24hr = v1GetMdTicker24hr = Entry('md/ticker/24hr', 'v1', 'GET', {'cost': 5})
    v1_get_md_ticker_24hr_all = v1GetMdTicker24hrAll = Entry('md/ticker/24hr/all', 'v1', 'GET', {'cost': 5})
    v1_get_md_spot_ticker_24hr = v1GetMdSpotTicker24hr = Entry('md/spot/ticker/24hr', 'v1', 'GET', {'cost': 5})
    v1_get_md_spot_ticker_24hr_all = v1GetMdSpotTicker24hrAll = Entry('md/spot/ticker/24hr/all', 'v1', 'GET', {'cost': 5})
    v1_get_exchange_public_products = v1GetExchangePublicProducts = Entry('exchange/public/products', 'v1', 'GET', {'cost': 5})
    v1_get_api_data_public_data_funding_rate_history = v1GetApiDataPublicDataFundingRateHistory = Entry('api-data/public/data/funding-rate-history', 'v1', 'GET', {'cost': 5})
    v2_get_md_v2_orderbook = v2GetMdV2Orderbook = Entry('md/v2/orderbook', 'v2', 'GET', {'cost': 5})
    v2_get_md_v2_trade = v2GetMdV2Trade = Entry('md/v2/trade', 'v2', 'GET', {'cost': 5})
    v2_get_md_v2_ticker_24hr = v2GetMdV2Ticker24hr = Entry('md/v2/ticker/24hr', 'v2', 'GET', {'cost': 5})
    v2_get_md_v2_ticker_24hr_all = v2GetMdV2Ticker24hrAll = Entry('md/v2/ticker/24hr/all', 'v2', 'GET', {'cost': 5})
    v2_get_api_data_public_data_funding_rate_history = v2GetApiDataPublicDataFundingRateHistory = Entry('api-data/public/data/funding-rate-history', 'v2', 'GET', {'cost': 5})
    private_get_spot_orders_active = privateGetSpotOrdersActive = Entry('spot/orders/active', 'private', 'GET', {'cost': 1})
    private_get_spot_orders = privateGetSpotOrders = Entry('spot/orders', 'private', 'GET', {'cost': 1})
    private_get_spot_wallets = privateGetSpotWallets = Entry('spot/wallets', 'private', 'GET', {'cost': 5})
    private_get_exchange_spot_order = privateGetExchangeSpotOrder = Entry('exchange/spot/order', 'private', 'GET', {'cost': 5})
    private_get_exchange_spot_order_trades = privateGetExchangeSpotOrderTrades = Entry('exchange/spot/order/trades', 'private', 'GET', {'cost': 5})
    private_get_exchange_order_v2_orderlist = privateGetExchangeOrderV2OrderList = Entry('exchange/order/v2/orderList', 'private', 'GET', {'cost': 5})
    private_get_exchange_order_v2_tradinglist = privateGetExchangeOrderV2TradingList = Entry('exchange/order/v2/tradingList', 'private', 'GET', {'cost': 5})
    private_get_accounts_accountpositions = privateGetAccountsAccountPositions = Entry('accounts/accountPositions', 'private', 'GET', {'cost': 1})
    private_get_g_accounts_accountpositions = privateGetGAccountsAccountPositions = Entry('g-accounts/accountPositions', 'private', 'GET', {'cost': 1})
    private_get_accounts_positions = privateGetAccountsPositions = Entry('accounts/positions', 'private', 'GET', {'cost': 25})
    private_get_api_data_futures_funding_fees = privateGetApiDataFuturesFundingFees = Entry('api-data/futures/funding-fees', 'private', 'GET', {'cost': 5})
    private_get_api_data_g_futures_funding_fees = privateGetApiDataGFuturesFundingFees = Entry('api-data/g-futures/funding-fees', 'private', 'GET', {'cost': 5})
    private_get_api_data_futures_orders = privateGetApiDataFuturesOrders = Entry('api-data/futures/orders', 'private', 'GET', {'cost': 5})
    private_get_api_data_g_futures_orders = privateGetApiDataGFuturesOrders = Entry('api-data/g-futures/orders', 'private', 'GET', {'cost': 5})
    private_get_api_data_futures_orders_by_order_id = privateGetApiDataFuturesOrdersByOrderId = Entry('api-data/futures/orders/by-order-id', 'private', 'GET', {'cost': 5})
    private_get_api_data_g_futures_orders_by_order_id = privateGetApiDataGFuturesOrdersByOrderId = Entry('api-data/g-futures/orders/by-order-id', 'private', 'GET', {'cost': 5})
    private_get_api_data_futures_trades = privateGetApiDataFuturesTrades = Entry('api-data/futures/trades', 'private', 'GET', {'cost': 5})
    private_get_api_data_g_futures_trades = privateGetApiDataGFuturesTrades = Entry('api-data/g-futures/trades', 'private', 'GET', {'cost': 5})
    private_get_api_data_futures_trading_fees = privateGetApiDataFuturesTradingFees = Entry('api-data/futures/trading-fees', 'private', 'GET', {'cost': 5})
    private_get_api_data_g_futures_trading_fees = privateGetApiDataGFuturesTradingFees = Entry('api-data/g-futures/trading-fees', 'private', 'GET', {'cost': 5})
    private_get_g_orders_activelist = privateGetGOrdersActiveList = Entry('g-orders/activeList', 'private', 'GET', {'cost': 1})
    private_get_orders_activelist = privateGetOrdersActiveList = Entry('orders/activeList', 'private', 'GET', {'cost': 1})
    private_get_exchange_order_list = privateGetExchangeOrderList = Entry('exchange/order/list', 'private', 'GET', {'cost': 5})
    private_get_exchange_order = privateGetExchangeOrder = Entry('exchange/order', 'private', 'GET', {'cost': 5})
    private_get_exchange_order_trade = privateGetExchangeOrderTrade = Entry('exchange/order/trade', 'private', 'GET', {'cost': 5})
    private_get_phemex_user_users_children = privateGetPhemexUserUsersChildren = Entry('phemex-user/users/children', 'private', 'GET', {'cost': 5})
    private_get_phemex_user_wallets_v2_depositaddress = privateGetPhemexUserWalletsV2DepositAddress = Entry('phemex-user/wallets/v2/depositAddress', 'private', 'GET', {'cost': 5})
    private_get_phemex_user_wallets_tradeaccountdetail = privateGetPhemexUserWalletsTradeAccountDetail = Entry('phemex-user/wallets/tradeAccountDetail', 'private', 'GET', {'cost': 5})
    private_get_phemex_user_order_closedpositionlist = privateGetPhemexUserOrderClosedPositionList = Entry('phemex-user/order/closedPositionList', 'private', 'GET', {'cost': 5})
    private_get_exchange_margins_transfer = privateGetExchangeMarginsTransfer = Entry('exchange/margins/transfer', 'private', 'GET', {'cost': 5})
    private_get_exchange_wallets_confirm_withdraw = privateGetExchangeWalletsConfirmWithdraw = Entry('exchange/wallets/confirm/withdraw', 'private', 'GET', {'cost': 5})
    private_get_exchange_wallets_withdrawlist = privateGetExchangeWalletsWithdrawList = Entry('exchange/wallets/withdrawList', 'private', 'GET', {'cost': 5})
    private_get_exchange_wallets_depositlist = privateGetExchangeWalletsDepositList = Entry('exchange/wallets/depositList', 'private', 'GET', {'cost': 5})
    private_get_exchange_wallets_v2_depositaddress = privateGetExchangeWalletsV2DepositAddress = Entry('exchange/wallets/v2/depositAddress', 'private', 'GET', {'cost': 5})
    private_get_api_data_spots_funds = privateGetApiDataSpotsFunds = Entry('api-data/spots/funds', 'private', 'GET', {'cost': 5})
    private_get_api_data_spots_orders = privateGetApiDataSpotsOrders = Entry('api-data/spots/orders', 'private', 'GET', {'cost': 5})
    private_get_api_data_spots_orders_by_order_id = privateGetApiDataSpotsOrdersByOrderId = Entry('api-data/spots/orders/by-order-id', 'private', 'GET', {'cost': 5})
    private_get_api_data_spots_pnls = privateGetApiDataSpotsPnls = Entry('api-data/spots/pnls', 'private', 'GET', {'cost': 5})
    private_get_api_data_spots_trades = privateGetApiDataSpotsTrades = Entry('api-data/spots/trades', 'private', 'GET', {'cost': 5})
    private_get_api_data_spots_trades_by_order_id = privateGetApiDataSpotsTradesByOrderId = Entry('api-data/spots/trades/by-order-id', 'private', 'GET', {'cost': 5})
    private_get_assets_convert = privateGetAssetsConvert = Entry('assets/convert', 'private', 'GET', {'cost': 5})
    private_get_assets_transfer = privateGetAssetsTransfer = Entry('assets/transfer', 'private', 'GET', {'cost': 5})
    private_get_assets_spots_sub_accounts_transfer = privateGetAssetsSpotsSubAccountsTransfer = Entry('assets/spots/sub-accounts/transfer', 'private', 'GET', {'cost': 5})
    private_get_assets_futures_sub_accounts_transfer = privateGetAssetsFuturesSubAccountsTransfer = Entry('assets/futures/sub-accounts/transfer', 'private', 'GET', {'cost': 5})
    private_get_assets_quote = privateGetAssetsQuote = Entry('assets/quote', 'private', 'GET', {'cost': 5})
    private_post_spot_orders = privatePostSpotOrders = Entry('spot/orders', 'private', 'POST', {'cost': 1})
    private_post_orders = privatePostOrders = Entry('orders', 'private', 'POST', {'cost': 1})
    private_post_g_orders = privatePostGOrders = Entry('g-orders', 'private', 'POST', {'cost': 1})
    private_post_positions_assign = privatePostPositionsAssign = Entry('positions/assign', 'private', 'POST', {'cost': 5})
    private_post_exchange_wallets_transferout = privatePostExchangeWalletsTransferOut = Entry('exchange/wallets/transferOut', 'private', 'POST', {'cost': 5})
    private_post_exchange_wallets_transferin = privatePostExchangeWalletsTransferIn = Entry('exchange/wallets/transferIn', 'private', 'POST', {'cost': 5})
    private_post_exchange_margins = privatePostExchangeMargins = Entry('exchange/margins', 'private', 'POST', {'cost': 5})
    private_post_exchange_wallets_createwithdraw = privatePostExchangeWalletsCreateWithdraw = Entry('exchange/wallets/createWithdraw', 'private', 'POST', {'cost': 5})
    private_post_exchange_wallets_cancelwithdraw = privatePostExchangeWalletsCancelWithdraw = Entry('exchange/wallets/cancelWithdraw', 'private', 'POST', {'cost': 5})
    private_post_exchange_wallets_createwithdrawaddress = privatePostExchangeWalletsCreateWithdrawAddress = Entry('exchange/wallets/createWithdrawAddress', 'private', 'POST', {'cost': 5})
    private_post_assets_transfer = privatePostAssetsTransfer = Entry('assets/transfer', 'private', 'POST', {'cost': 5})
    private_post_assets_spots_sub_accounts_transfer = privatePostAssetsSpotsSubAccountsTransfer = Entry('assets/spots/sub-accounts/transfer', 'private', 'POST', {'cost': 5})
    private_post_assets_futures_sub_accounts_transfer = privatePostAssetsFuturesSubAccountsTransfer = Entry('assets/futures/sub-accounts/transfer', 'private', 'POST', {'cost': 5})
    private_post_assets_universal_transfer = privatePostAssetsUniversalTransfer = Entry('assets/universal-transfer', 'private', 'POST', {'cost': 5})
    private_post_assets_convert = privatePostAssetsConvert = Entry('assets/convert', 'private', 'POST', {'cost': 5})
    private_put_spot_orders_create = privatePutSpotOrdersCreate = Entry('spot/orders/create', 'private', 'PUT', {'cost': 1})
    private_put_spot_orders = privatePutSpotOrders = Entry('spot/orders', 'private', 'PUT', {'cost': 1})
    private_put_orders_replace = privatePutOrdersReplace = Entry('orders/replace', 'private', 'PUT', {'cost': 1})
    private_put_g_orders_replace = privatePutGOrdersReplace = Entry('g-orders/replace', 'private', 'PUT', {'cost': 1})
    private_put_positions_leverage = privatePutPositionsLeverage = Entry('positions/leverage', 'private', 'PUT', {'cost': 5})
    private_put_g_positions_leverage = privatePutGPositionsLeverage = Entry('g-positions/leverage', 'private', 'PUT', {'cost': 5})
    private_put_g_positions_switch_pos_mode_sync = privatePutGPositionsSwitchPosModeSync = Entry('g-positions/switch-pos-mode-sync', 'private', 'PUT', {'cost': 5})
    private_put_positions_risklimit = privatePutPositionsRiskLimit = Entry('positions/riskLimit', 'private', 'PUT', {'cost': 5})
    private_delete_spot_orders = privateDeleteSpotOrders = Entry('spot/orders', 'private', 'DELETE', {'cost': 2})
    private_delete_spot_orders_all = privateDeleteSpotOrdersAll = Entry('spot/orders/all', 'private', 'DELETE', {'cost': 2})
    private_delete_orders_cancel = privateDeleteOrdersCancel = Entry('orders/cancel', 'private', 'DELETE', {'cost': 1})
    private_delete_orders = privateDeleteOrders = Entry('orders', 'private', 'DELETE', {'cost': 1})
    private_delete_orders_all = privateDeleteOrdersAll = Entry('orders/all', 'private', 'DELETE', {'cost': 3})
    private_delete_g_orders_cancel = privateDeleteGOrdersCancel = Entry('g-orders/cancel', 'private', 'DELETE', {'cost': 1})
    private_delete_g_orders = privateDeleteGOrders = Entry('g-orders', 'private', 'DELETE', {'cost': 1})
    private_delete_g_orders_all = privateDeleteGOrdersAll = Entry('g-orders/all', 'private', 'DELETE', {'cost': 3})
