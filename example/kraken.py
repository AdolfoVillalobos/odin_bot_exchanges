import os
import asyncio
import aiohttp
from dotenv import load_dotenv

from odin_bot_exchanges.kraken import KrakenExchange


async def main():
    api_key = os.getenv("KRAKEN_API_KEY")
    secret_key = os.getenv("KRAKEN_SECRET_KEY")
    api_url = os.getenv("KRAKEN_API_URL")

    ox = KrakenExchange(
        api_key=api_key, secret_key=secret_key, api_url=api_url)

    async with aiohttp.ClientSession() as session:

        wallet = await ox.get_wallet_response(session=session)

        print(wallet)


load_dotenv(".env")
asyncio.run(main())
