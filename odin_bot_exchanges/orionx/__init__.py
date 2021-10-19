
import aiohttp
import logging
from typing import List

from orionx_python_client import OrionXClient
from odin_bot_entities.trades import Transaction
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

    # async def get_transaction_from_order_response(
    #     self, message: EntityMessage, session: aiohttp.ClientSession
    # ) -> Order:
    #     try:
    #         query_str = get_order_query(message.id)
    #         payload = {"query": query_str, "variables": {}}
    #         response = await self.client.request("POST", "graphql", session, payload)
    #         order = self.transaction_from_order_parser.parse_response(
    #             response=response)
    #         return order
    #     except Exception as err:
    #         logging.debug(err)
    #         raise err

    async def get_wallet_response(self):
        try:
            async with aiohttp.ClientSession() as session:
                response = await self.client.get_balance(session=session)
                wallet = self.wallet_parser.parse_response(response=response)
            return wallet
        except Exception as err:
            logging.error(err)
            return None

    # async def get_wallet_response(self, session: aiohttp.ClientSession) -> List[Wallet]:
    #     try:
    #         query_str = get_balance_query()
    #         payload = {"query": query_str, "variables": {}}
    #         response = await self.client.request("POST", "graphql", session, payload)
    #         wallets = self.wallet_parser.parse_response(response=response)
    #         return wallets
    #     except Exception as err:
    #         logging.debug(err)
    #         raise err

    # async def get_trades_history_response(
    #     self, db, session: aiohttp.ClientSession
    # ) -> List[Transaction]:
    #     try:

    #         page = 1
    #         num_transactions = 0

    #         while True:
    #             query_str = get_orders_history_query(page_id=page)
    #             payload = {"query": query_str, "variables": {}}
    #             response = await self.client.request(
    #                 "POST", "graphql", session, payload
    #             )
    #             total_pages = response["data"]["orders"]["totalPages"]

    #             if page < total_pages or page < 10000:

    #                 transactions = self.trade_history_parser.parse_response(
    #                     response)

    #                 for tx in transactions:
    #                     db.add_transaction(transaction=tx)

    #                 page += 1
    #                 num_transactions += len(transactions)
    #                 logging.info(f"{page} -> tx: {len(transactions)}")
    #             else:
    #                 break

    #         return num_transactions

    #     except Exception as err:
    #         logging.debug(err)
    #         logging.debug(response)
    #         raise err

    # async def get_transaction_response(self):
    #     return await super().get_transaction_response()

    # async def get_ticker_price_response(self):
    #     return await super().get_ticker_price_response()
