import logging
import os
import asyncio
from dotenv import load_dotenv

from odin_bot_exchanges.orionx import OrionXExchange


async def main():
    api_key = os.getenv("ORIONX_API_KEY")
    secret_key = os.getenv("ORIONX_API_SECRET")
    api_url = os.getenv("ORIONX_API_URL")

    ox = OrionXExchange(
        api_key=api_key, secret_key=secret_key, api_url=api_url)

    CEROS = {
        "USDT": 8,
        "BTC": 8,
        "DAI": 8,
        "ETH": 8,
        "BNB": 8,
        "LTC": 8,
        "BCH": 8,
        "CHA": 8,
        "LUK": 8,
        "DASH": 8,
        "XLM": 7,
        "XRP": 6,
        "TRX": 6,
        "DOT": 8,
        "ADA": 6,
        "CLP": 0,
        "EOS": 4,
        "USD": 2,
        "EUR": 2,
        "SOL": 8,
        "MATIC": 8,
    }

    wallet = ox.get_wallet_response(currency_ceros=CEROS)

    print(wallet)

    open = ox.close_orders(order_ids=["123"])

    print(open)

    o1 = ox.new_position(market_code="BTC/USDT", amount=0.0006,
                         limit_price=60000, selling="true")

    print(o1)

    o2 = ox.new_position(market_code="BTC/CLP", amount=0.0006,
                         limit_price=60000000, selling="true")

    print(o2)

load_dotenv(".env")
asyncio.run(main())
