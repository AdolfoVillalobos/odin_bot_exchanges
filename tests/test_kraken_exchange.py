# import unittest
# import aiohttp
# from typing import List
# from dotenv import load_dotenv


# import nest_asyncio

# nest_asyncio.apply()


# logging.basicConfig(level=logging.DEBUG,
#                     format="%(levelname)s:%(asctime)s:%(message)s")


# class TestKrakenExchange(unittest.IsolatedAsyncioTestCase):
#     async def asyncSetUp(self):
#         load_dotenv(".env")
#         credentials = KrakenEnv()
#         self.exchange = KrakenExchange(credentials=credentials)

#     async def test_get_transaction_response_valid(self):

#         message = EntityMessage(
#             id="OSTEUX-KWZUX-2XET45",
#             market="XBT/USDT",
#             exchange="kraken",
#             order_type="b",
#         )

#         async with aiohttp.ClientSession() as session:
#             transaction = await self.exchange.get_transaction_response(
#                 session=session, message=message
#             )
# #
#             self.assertTrue(transaction is not None)
#             self.assertEqual(transaction.id, message.id)
#             self.assertEqual(transaction.currency_name, "BTC")
#             self.assertEqual(transaction.pair_currency_name, "USDT")
#             self.assertEqual(transaction.market, "BTC/USDT")
#             self.assertEqual(transaction.type, "buy")
#             self.assertEqual(transaction.exchange, "kraken")

#     async def test_get_transaction_response_invalid(self):

#         message = EntityMessage(
#             id="invalid-id",
#             market="XBT/USDT",
#             exchange="kraken",
#             order_type="b",
#         )

#         async with aiohttp.ClientSession() as session:
#             with self.assertRaises(ResponseError):
#                 await self.exchange.get_transaction_response(
#                     session=session, message=message
#                 )

#     async def test_get_wallet_response_valid(self):
#         async with aiohttp.ClientSession() as session:
#             wallets: List[Wallet] = await self.exchange.get_wallet_response(session)

#             self.assertTrue(len(wallets) == 1)
#             self.assertEqual(wallets[0].exchange, "kraken")
#             self.assertEqual(wallets[0].sign, 1)

#     async def test_get_ticker_response_valid(self):
#         message = EntityMessage(
#             id="OSTEUX-KWZUX-2XET45",
#             market="XBT/USDT",
#             exchange="kraken",
#             order_type="b",
#         )
#         async with aiohttp.ClientSession() as session:
#             ticker = await self.exchange.get_ticker_price_response(
#                 session=session, message=message
#             )
#             self.assertTrue(ticker is not None)
