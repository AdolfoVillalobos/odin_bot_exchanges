
import aiohttp
import logging
from typing import List

from orionx_python_client import OrionXClient
from odin_bot_entities.trades import Order
from odin_bot_exchanges.exchange import ExchangeService
from .responses import OrionXOrderResponseParser, OrionXTradeHistoryResponseParser, OrionXWalletResponseParser, OrionXTransactionFromOrderResponseParser


class OrionXExchange(ExchangeService):
    exchange: str = "orionX"

    def __init__(self, api_url: str, api_key: str, secret_key: str):
        self.client = OrionXClient(
            api_key=api_key, api_url=api_url, secret_key=secret_key)
        self.wallet_parser = OrionXWalletResponseParser()
        self.order_parser = OrionXOrderResponseParser()
        self.trade_history_parser = OrionXTradeHistoryResponseParser()
        self.transaction_from_order_parser = OrionXTransactionFromOrderResponseParser()

    async def get_order_response(
        self, order_id: str, market_code: str
    ):
        try:
            async with aiohttp.ClientSession() as session:
                response = await self.client.get_order(order_id=order_id, market_code=market_code, session=session)
                order = self.order_parser.parse_response(
                    order_id=order_id,
                    market_code=market_code,
                    response=response)
            return order
        except Exception as err:
            logging.error(err)
            return None

    async def get_transaction_from_order_response(self, order_id: str, market_code: str) -> Order:
        try:
            async with aiohttp.ClientSession() as session:
                response = await self.client.get_order(order_id=order_id, market_code=market_code, session=session)
                order = self.transaction_from_order_parser.parse_response(
                    order_id=order_id,
                    market_code=market_code,
                    response=response)
            return order
        except Exception as err:
            logging.debug(err)
            raise err

    async def get_wallet_response(self):
        try:
            async with aiohttp.ClientSession() as session:
                response = await self.client.get_balance(session=session)
                wallet = self.wallet_parser.parse_response(response=response)
            return wallet
        except Exception as err:
            logging.error(err)
            return None