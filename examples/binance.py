import os
import asyncio
import aiohttp
from dotenv import load_dotenv

from odin_bot_exchanges.binance import BinanceExchange


async def main():
    api_key = os.getenv("BINANCE_API_KEY")
    secret_key = os.getenv("BINANCE_API_SECRET")

    ex = BinanceExchange(
        api_key=api_key, secret_key=secret_key)

    # wallet = await ex.get_wallet_response()

    # print(wallet)

    # p = await ex.get_symbol_price(symbol="BTCUSDT")

    # print(p)

    # info = await ex.get_exchange_info(symbol="BTCUSDT")

    # print(info)

    transaction = await ex.get_transaction_response(order_id="2687361210", market_code="EOS/USDT")

    print(transaction)

load_dotenv(".env")
asyncio.run(main())
