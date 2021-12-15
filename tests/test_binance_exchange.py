# import unittest
# import aiohttp
# from typing import List
# from dotenv.main import load_dotenv

# from base.messages import EntityMessage
# from base.entities import Transaction, Wallet
# from base.errors import ResponseError
# from async_pydantic_vault.typing import KrakenEnv, OrionXEnv, BinanceEnv
# from base.exchange_service import KrakenExchange, BinanceExchange, OrionXExchange
# import logging

# import nest_asyncio

# nest_asyncio.apply()


# logging.basicConfig(level=logging.DEBUG,
#                     format="%(levelname)s:%(asctime)s:%(message)s")


# class TestBinanceExchange(unittest.IsolatedAsyncioTestCase):
#     async def asyncSetUp(self):
#         load_dotenv(".env")
#         credentials = BinanceEnv()
#         self.exchange = BinanceExchange(credentials=credentials)

#     async def test_get_transaction_response_valid(self):

#         message = EntityMessage(
#             id="44012152",
#             market="PAXG/USDT",
#             exchange="binance",
#             order_type="b",
#         )

#         transactions: List[Transaction] = await self.exchange.get_transaction_response(
#             message
#         )
#         self.assertTrue(transactions != None)
#         self.assertEqual(transactions[0].id, "44012152")
#         self.assertEqual(transactions[0].currency_name, "PAXG")
#         self.assertEqual(transactions[0].pair_currency_name, "USDT")
#         self.assertEqual(transactions[0].exchange, "binance")
#         self.assertEqual(transactions[0].market, "PAXG/USDT")

#     async def test_get_transaction_response_invalid(self):

#         message = EntityMessage(
#             id="klalalala",
#             market="PAXG/USDT",
#             exchange="binance",
#             order_type="b",
#         )

#         with self.assertRaises(Exception):
#             transactions: List[
#                 Transaction
#             ] = await self.exchange.get_transaction_response(message)

#     async def test_get_wallet_response_valid(self):
#         async with aiohttp.ClientSession() as session:
#             wallets = await self.exchange.get_wallet_response(
#                 session=session,
#             )

#             wallets: List[Wallet] = await self.exchange.get_wallet_response(
#                 session=session
#             )
#             self.assertTrue(wallets != None)
#             self.assertEqual(len(wallets), 1)
#             self.assertEqual(wallets[0].exchange, "binance")
#             self.assertEqual(wallets[0].sign, 1)
