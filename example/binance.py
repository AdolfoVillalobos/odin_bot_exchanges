import os
import asyncio
import aiohttp
from dotenv import load_dotenv

from odin_bot_exchanges.binance import BinanceExchange


async def main():
    api_key = os.getenv("BINANCE_API_KEY")
    secret_key = os.getenv("BINANCE_API_SECRET")

    ox = BinanceExchange(
        api_key=api_key, secret_key=secret_key)

    wallet = await ox.get_wallet_response()

    print(wallet)


load_dotenv(".env")
asyncio.run(main())
