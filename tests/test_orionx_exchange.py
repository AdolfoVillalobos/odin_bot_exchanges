import unittest
import aiohttp
from typing import List
from dotenv.main import load_dotenv

from base.messages import EntityMessage
from base.entities import Transaction, Wallet
from base.errors import ResponseError
from async_pydantic_vault.typing import KrakenEnv, OrionXEnv, BinanceEnv
from base.exchange_service import KrakenExchange, BinanceExchange, OrionXExchange
import logging

import nest_asyncio

nest_asyncio.apply()


logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)s:%(asctime)s:%(message)s")


class TestKrakenExchange(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        load_dotenv(".env")
        credentials = KrakenEnv()
        self.exchange = KrakenExchange(credentials=credentials)

    async def test_get_transaction_response_valid(self):

        message = EntityMessage(
            id="OSTEUX-KWZUX-2XET45",
            market="XBT/USDT",
            exchange="kraken",
            order_type="b",
        )

        async with aiohttp.ClientSession() as session:
            transaction = await self.exchange.get_transaction_response(
                session=session, message=message
            )

            self.assertTrue(transaction is not None)
            self.assertEqual(transaction.id, message.id)
            self.assertEqual(transaction.currency_name, "BTC")
            self.assertEqual(transaction.pair_currency_name, "USDT")
            self.assertEqual(transaction.market, "BTC/USDT")
            self.assertEqual(transaction.type, "buy")
            self.assertEqual(transaction.exchange, "kraken")

    async def test_get_transaction_response_invalid(self):

        message = EntityMessage(
            id="invalid-id",
            market="XBT/USDT",
            exchange="kraken",
            order_type="b",
        )

        async with aiohttp.ClientSession() as session:
            with self.assertRaises(ResponseError):
                await self.exchange.get_transaction_response(
                    session=session, message=message
                )

    async def test_get_wallet_response_valid(self):
        async with aiohttp.ClientSession() as session:
            wallets: List[Wallet] = await self.exchange.get_wallet_response(session)

            self.assertTrue(len(wallets) == 1)
            self.assertEqual(wallets[0].exchange, "kraken")
            self.assertEqual(wallets[0].sign, 1)

    async def test_get_ticker_response_valid(self):
        message = EntityMessage(
            id="OSTEUX-KWZUX-2XET45",
            market="XBT/USDT",
            exchange="kraken",
            order_type="b",
        )
        async with aiohttp.ClientSession() as session:
            ticker = await self.exchange.get_ticker_price_response(
                session=session, message=message
            )
            self.assertTrue(ticker is not None)


class TestOrionXExchange(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        load_dotenv(".env")
        credentials = OrionXEnv()
        self.exchange = OrionXExchange(credentials=credentials)

    async def test_get_order_response_valid(self):

        message = EntityMessage(
            id="iroFHo5yRzKeTrYf2",
            market="BTC/CLP",
            exchange="orionX",
            amount=0.00405057,
            status="open",
            order_type="buy",
        )

        async with aiohttp.ClientSession() as session:
            order = await self.exchange.get_order_response(
                session=session, message=message
            )

            self.assertEqual(order.id, "iroFHo5yRzKeTrYf2")
            self.assertEqual(order.amount, 0.00405057)
            self.assertEqual(order.market, "BTC/CLP")
            self.assertTrue(order.transactions is not None)

    async def test_get_order_response_invalid(self):

        message = EntityMessage(
            id="lalalal",
            market="BTC/CLP",
            exchange="orionX",
            amount=0.00405057,
            status="open",
            order_type="buy",
        )

        async with aiohttp.ClientSession() as session:
            with self.assertRaises(ResponseError):
                await self.exchange.get_order_response(session=session, message=message)

    async def test_get_wallet_response(self):
        async with aiohttp.ClientSession() as session:
            wallets = await self.exchange.get_wallet_response(
                session=session,
            )

            self.assertTrue(len(wallets) == 2)


class TestBinanceClient(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        load_dotenv(".env")
        credentials = BinanceEnv()
        self.exchange = BinanceExchange(credentials=credentials)

    async def test_get_transaction_response_valid(self):

        message = EntityMessage(
            id="44012152",
            market="PAXG/USDT",
            exchange="binance",
            order_type="b",
        )

        transactions: List[Transaction] = await self.exchange.get_transaction_response(
            message
        )
        self.assertTrue(transactions != None)
        self.assertEqual(transactions[0].id, "44012152")
        self.assertEqual(transactions[0].currency_name, "PAXG")
        self.assertEqual(transactions[0].pair_currency_name, "USDT")
        self.assertEqual(transactions[0].exchange, "binance")
        self.assertEqual(transactions[0].market, "PAXG/USDT")

    async def test_get_transaction_response_invalid(self):

        message = EntityMessage(
            id="klalalala",
            market="PAXG/USDT",
            exchange="binance",
            order_type="b",
        )

        with self.assertRaises(Exception):
            transactions: List[
                Transaction
            ] = await self.exchange.get_transaction_response(message)

    async def test_get_wallet_response_valid(self):
        async with aiohttp.ClientSession() as session:
            wallets = await self.exchange.get_wallet_response(
                session=session,
            )

            wallets: List[Wallet] = await self.exchange.get_wallet_response(
                session=session
            )
            self.assertTrue(wallets != None)
            self.assertEqual(len(wallets), 1)
            self.assertEqual(wallets[0].exchange, "binance")
            self.assertEqual(wallets[0].sign, 1)
