import os
import asyncio
import aiohttp
import logging

from datetime import datetime, timezone
from dotenv import load_dotenv

from odin_bot_exchanges.kraken import KrakenExchange
from odin_bot_exchanges.kraken.currency import KRAKEN_RENAME_PAIRS

logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)s:%(asctime)s:%(message)s")


async def main():
    api_key = os.getenv("KRAKEN_API_KEY")
    secret_key = os.getenv("KRAKEN_SECRET_KEY")
    api_url = os.getenv("KRAKEN_API_URL")

    ox = KrakenExchange(
        api_key=api_key, secret_key=secret_key, api_url=api_url)

    # wallet = await ox.get_wallet_response(session=session)

    start = datetime(2021, 9, 1, tzinfo=timezone.utc).timestamp()
    end = datetime(2021, 12, 15, tzinfo=timezone.utc).timestamp()

    # ledger = await ox.get_ledger_history_response(asset="all", type="all", start=start, end=end)

    # print(ledger[0].asset)

    trades = await ox.get_trades_history_response(start=start, end=end, rename_market_map=KRAKEN_RENAME_PAIRS)
    print(trades)


load_dotenv(".env")
asyncio.run(main())
