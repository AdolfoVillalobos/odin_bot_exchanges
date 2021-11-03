
KRAKEN_RENAME_COINS = {
    "XXBT": "BTC",
    "XBT": "BTC",
    "XETH": "ETH",
    "ETH": "ETH",
    "DASH": "DASH",
    "ZUSD": "USD",
    "USD": "USDT",
    "USDT": "USDT",
    "XXRP": "XRP",
    "XRP": "XRP",
    "XXLM": "XLM",
    "XLM": "XLM",
    "XLTC": "LTC",
    "LTC": "LTC",
    "DAI": "DAI",
    "BCH": "BCH",
    "TRX": "TRX",
    "EOS": "EOS",
    "ZEUR": "EUR",
    "PAXG": "PAX",
    "DOT": "DOT",
    "USDC": "USDC",
}


KRAKEN_RENAME_PAIRS = {
    "EOSUSDT": "EOS/USDT",
    "XRPUSDT": "XRP/USDT",
    "XBTUSDT": "BTC/USDT",
    "ETHUSDT": "ETH/USDT",
    "XLTCUSDT": "LTC/USDT",
    "LTCUSDT": "LTC/USDT",
    "BCHUSDT": "BCH/USDT",
    "DAIUSDT": "DAI/USDT",
    "SOLUSDT": "SOL/USDT",
    "ATOMUSDT": "ATOM/USDT",
    "ADAUSDT": "ADA/USDT",
    "DOTUSDT": "DOT/USDT",
    "BCHUSDT": "BCH/USDT",
    "PAXGUSD": "PAX/USD",
    "USDCUSDT": "USDC/USDT",
    "XXLMZUSD": "XLM/USD",
    "TRXUSD": "TRX/USD",
    "XXRPZUSD": "XRP/USD",
    "XLTCZUSD": "LTC/USD",
    "DASHUSD": "DASH/USD",
    "XETHZUSD": "ETH/USD",
    "XXBTZUSD": "BTC/USD",
    "USDTZUSD": "USDT/USD",
    "USDCZUSD": "USDC/USD",
    "EOSUSD": "EOS/USD",
    "DAIUSD": "DAI/USD",
    "DOTUSD": "DOT/USD",
    "XDGUSD": "XDG/USD",
    "ADAZUSD": "ADA/USD",
    "ADAUSD": "ADA/USD",
    "ATOMUSD": "ATOM/USD",
    "SOLUSD": "SOL/USD",
    "BCHUSD": "BCH/USD",
    "USDCUSD": "USDC/USD",
    "USDTEUR": "USDT/EUR",
    "XXBTZEUR": "BTC/EUR",
    "USDTCAD": "USDT/CAD",
}


KRAKEN_RENAME_COINS_INV = {v: k for k, v in KRAKEN_RENAME_COINS.items()}

KRAKEN_MINIMUM = {
    "AAVE": 0.05,
    "ALGO": 15,
    "ANT": 2,
    "REP": 0.3,
    "BAL": 0.3,
    "BAT": 30,
    "XXBT": 0.0002,
    "XBT": 0.0002,
    "BCH": 0.02,
    "ADA": 25,
    "LINK": 0.5,
    "COMP": 0.05,
    "ATOM": 1,
    "CRV": 10,
    "DAI": 5,
    "DASH": 0.05,
    "EOS": 2.5,
    "XETH": 0.005,
    "ETH": 0.005,
    "ETH2.S": 0.02,
    "XLTC": 0.05,
    "LTC": 0.05,
    "XXRP": 20,
    "XRP": 20,
    "XXLM": 20,
    "XLM": 20,
    "USDT": 5,
    "TRX": 250,
    "DOT": 0.2,
}

MINIMUM_TO_TRADE = {"kraken": KRAKEN_MINIMUM}