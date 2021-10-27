import os
import asyncio
import aiohttp
from dotenv import load_dotenv

from odin_bot_exchanges.orionx import OrionXExchange


async def main():
    api_key = os.getenv("ORIONX_API_KEY")
    secret_key = os.getenv("ORIONX_API_SECRET")
    api_url = os.getenv("ORIONX_API_URL")

    ox = OrionXExchange(
        api_key=api_key, secret_key=secret_key, api_url=api_url)

    wallet = await ox.get_wallet_response()

    print(wallet)

    # # cancel = await ox.close_order_by_id(order_id="123")

    # # print(cancel)

    # open = await ox.get_open_orders_by_market(market="BTC/CLP", selling="true")

    # print(open)

    # open = await ox.close_orders_by_market(market="BTC/CLP", selling="true")

    # print(open)

    open = await ox.close_orders(order_ids=["123"])

    print(open)

load_dotenv(".env")
asyncio.run(main())
