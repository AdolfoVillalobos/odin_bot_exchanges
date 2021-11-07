import os
import asyncio
import aiohttp
import logging

from datetime import datetime, timezone
from dotenv import load_dotenv

from odin_bot_exchanges.kraken import KrakenExchange

logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)s:%(asctime)s:%(message)s")


async def main():
    api_key = os.getenv("KRAKEN_API_KEY")
    secret_key = os.getenv("KRAKEN_SECRET_KEY")
    api_url = os.getenv("KRAKEN_API_URL")

    ox = KrakenExchange(
        api_key=api_key, secret_key=secret_key, api_url=api_url)

    # wallet = await ox.get_wallet_response(session=session)

    start = datetime(2021, 10, 27, tzinfo=timezone.utc).timestamp()
    end = datetime(2021, 11, 2, tzinfo=timezone.utc).timestamp()

    # ledger = await ox.get_ledger_history_response(asset="XXBT", type="trade", start=start, end=end, session=session)

    # print(ledger[0].asset)

    trades = await ox.get_trades_history_response(start=start, end=end)
    # print(trades)


load_dotenv(".env")
asyncio.run(main())
