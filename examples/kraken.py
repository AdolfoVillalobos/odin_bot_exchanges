import os
import asyncio
import aiohttp
from datetime import datetime, tzinfo
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

        start = datetime(2021, 10, 1).timestamp()
        end = datetime(2021, 10, 21).timestamp()

        ledger = await ox.get_ledger_history_response(type="deposit", start=start, end=end, session=session)

        print(ledger)


load_dotenv(".env")
asyncio.run(main())
