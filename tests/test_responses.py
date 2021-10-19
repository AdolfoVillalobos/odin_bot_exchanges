import unittest

from typing import List
from base.messages import EntityMessage
from base.responses import (
    BinanceTransactionResponseParser,
    BinanceWalletResponseParser,
    KrakenWalletResponseParser,
    KrakenTransactionResponseParser,
    OrionXOrderResponseParser,
    OrionXWalletResponseParser,
)
from base.entities import Transaction, Wallet
from base.errors import ParserError, ResponseError


class TestKrakenTransactionResponseParser(unittest.TestCase):
    def setUp(self):
        self.parser = KrakenTransactionResponseParser()

    def test_get_transaction_response_valid(self):
        message = EntityMessage(
            id="OSTEUX-KWZUX-2XET45",
            market="XBT/USDT",
            exchange="kraken",
            order_type="b",
        )

        response = {
            "error": [],
            "result": {
                "OSTEUX-KWZUX-2XET45": {
                    "refid": None,
                    "userref": None,
                    "status": "closed",
                    "reason": None,
                    "opentm": 1628609615.1429,
                    "closetm": 1628609615.1432,
                    "starttm": 0,
                    "expiretm": 0,
                    "descr": {
                        "pair": "XBTUSDT",
                        "type": "buy",
                        "ordertype": "market",
                        "price": "0",
                        "price2": "0",
                        "leverage": "none",
                        "order": "buy 0.00405057 XBTUSDT @ market",
                        "close": "",
                    },
                    "vol": "0.00405057",
                    "vol_exec": "0.00405057",
                    "cost": "181.9",
                    "fee": "0.2",
                    "price": "44920.1",
                }
            },
        }

        transaction = self.parser.parse_response(
            response=response, message=message)

        self.assertEqual(transaction.id, message.id)
        self.assertEqual(transaction.currency_name, "BTC")
        self.assertEqual(transaction.pair_currency_name, "USDT")
        self.assertEqual(transaction.currency_value, 0.00405057)
        self.assertGreater(transaction.pair_currency_value, 0)

    def test_get_transaction_response_invalid(self):

        message = EntityMessage(
            id="invalid",
            market="XBT/USDT",
            exchange="kraken",
            order_type="b",
        )

        response = {"error": ["EOrder:Invalid order"]}

        with self.assertRaises(ResponseError):
            self.parser.parse_response(response=response, message=message)


class TestKrakenWalletResponseParser(unittest.TestCase):
    def setUp(self):
        self.parser = KrakenWalletResponseParser()

    def test_get_wallet_response_valid(self):
        response = {
            "error": [],
            "result": {
                "ZUSD": "18052.0919",
                "ZEUR": "0.0000",
                "XXBT": "0.1892088400",
                "XXRP": "3359.89431877",
                "XLTC": "47.0770887900",
                "XXLM": "0.00000308",
                "XETH": "0.2948604300",
                "USDT": "264161.65556129",
                "DASH": "4.3277913400",
                "EOS": "1756.2920098700",
                "BCH": "0.1249347200",
                "DAI": "0.0000061400",
                "TRX": "0.00000093",
                "DOT": "0.2000000000",
            },
        }
        wallets: List[Transaction] = self.parser.parse_response(
            response=response)
        self.assertTrue(wallets is not None)
        self.assertTrue(wallets[0].exchange == "kraken")
        self.assertTrue(len(wallets[0].coins.keys()),
                        len(response["result"].keys()))
        self.assertAlmostEqual(wallets[0].coins["USD"].amount, 18052.09)


class TestOrionXOrderResponseParser(unittest.TestCase):
    def setUp(self):
        self.parser = OrionXOrderResponseParser()

    def test_get_order_response_valid(self):
        message = EntityMessage(
            id="iroFHo5yRzKeTrYf2",
            market="BTC/CLP",
            exchange="orionX",
            amount=0.00405057,
            status="open",
            order_type="buy",
        )

        response = {
            "data": {
                "order": {
                    "amount": 46284008,
                    "type": "limit",
                    "sell": True,
                    "transactions": [
                        {
                            "id": "kXC3dWTyodxqX2zNC",
                            "currency": {"code": "CLP"},
                            "pairCurrency": {"code": "BTC"},
                            "amount": 142984,
                            "type": "trade-in",
                            "price": 35335000,
                            "adds": True,
                            "commission": 143,
                            "cost": 405057,
                            "date": 1628609614327,
                        },
                        {
                            "id": "xijRZY6drZ3Pdfd8m",
                            "currency": {"code": "BTC"},
                            "pairCurrency": {"code": "CLP"},
                            "amount": 405057,
                            "type": "trade-out",
                            "price": 35335000,
                            "adds": False,
                            "commission": 0,
                            "cost": 142984,
                            "date": 1628609614330,
                        },
                    ],
                }
            }
        }

        order = self.parser.parse_response(message=message, response=response)

        self.assertEqual(len(order.transactions), 1)

    def test_get_order_response_invalid(self):
        message = EntityMessage(
            id="lalalal",
            market="BTC/CLP",
            exchange="orionX",
            amount=0.00405057,
            status="open",
            order_type="buy",
        )

        response = {
            "data": {"order": None},
            "errors": [
                {"message": "Cannot read property 'userId' of null",
                    "path": ["order"]}
            ],
        }

        with self.assertRaises(ResponseError):
            self.parser.parse_response(response=response, message=message)


class TestOrionXWalletResponseParser(unittest.TestCase):
    def setUp(self):
        self.parser = OrionXWalletResponseParser()

    def test_get_wallet_response_valid(self):
        response = {
            "data": {
                "me": {
                    "wallets": [
                        {
                            "currency": {"code": "CLP"},
                            "balance": 8162751,
                            "availableBalance": 7139651,
                            "loanLimit": None,
                            "loanUsedAmount": None,
                            "unconfirmedBalance": 0,
                        },
                        {
                            "currency": {"code": "USDT"},
                            "balance": 5840469811012,
                            "availableBalance": 1419020691152,
                            "loanLimit": 12998000000000,
                            "loanUsedAmount": 7998000000000,
                            "unconfirmedBalance": 0,
                        },
                        {
                            "currency": {"code": "BTC"},
                            "balance": 248287790,
                            "availableBalance": 6321995,
                            "loanLimit": 500000000,
                            "loanUsedAmount": 267200000,
                            "unconfirmedBalance": 0,
                        },
                        {
                            "currency": {"code": "DAI"},
                            "balance": 1327975151100,
                            "availableBalance": 102103771567,
                            "loanLimit": 2000000000000,
                            "loanUsedAmount": 2000000000000,
                            "unconfirmedBalance": 0,
                        },
                        {
                            "currency": {"code": "ETH"},
                            "balance": 1413513957,
                            "availableBalance": 146611757,
                            "loanLimit": 2000000000,
                            "loanUsedAmount": 1443000000,
                            "unconfirmedBalance": 0,
                        },
                        {
                            "currency": {"code": "BNB"},
                            "balance": 0,
                            "availableBalance": 0,
                            "loanLimit": 10000000000,
                            "loanUsedAmount": 0,
                            "unconfirmedBalance": 0,
                        },
                        {
                            "currency": {"code": "LTC"},
                            "balance": 10292091121,
                            "availableBalance": 887054052,
                            "loanLimit": 15000000000,
                            "loanUsedAmount": 15000000000,
                            "unconfirmedBalance": 0,
                        },
                        {
                            "currency": {"code": "XRP"},
                            "balance": 21630065681,
                            "availableBalance": 1989959995,
                            "loanLimit": 25000000000,
                            "loanUsedAmount": 25000000000,
                            "unconfirmedBalance": 0,
                        },
                        {
                            "currency": {"code": "XLM"},
                            "balance": 299999989969,
                            "availableBalance": 29999989969,
                            "loanLimit": 300000000000,
                            "loanUsedAmount": 300000000000,
                            "unconfirmedBalance": 0,
                        },
                        {
                            "currency": {"code": "BCH"},
                            "balance": 1987506528,
                            "availableBalance": 79037433,
                            "loanLimit": 2000000000,
                            "loanUsedAmount": 2000000000,
                            "unconfirmedBalance": 0,
                        },
                        {
                            "currency": {"code": "CHA"},
                            "balance": 1097900000,
                            "availableBalance": 1097900000,
                            "loanLimit": None,
                            "loanUsedAmount": None,
                            "unconfirmedBalance": 0,
                        },
                        {
                            "currency": {"code": "LUK"},
                            "balance": 231115894,
                            "availableBalance": 231115894,
                            "loanLimit": None,
                            "loanUsedAmount": None,
                            "unconfirmedBalance": 0,
                        },
                        {
                            "currency": {"code": "DASH"},
                            "balance": 2569579850,
                            "availableBalance": 302358694,
                            "loanLimit": 3000000000,
                            "loanUsedAmount": 3000000000,
                            "unconfirmedBalance": 0,
                        },
                        {
                            "currency": {"code": "TRX"},
                            "balance": 299757557440,
                            "availableBalance": 9757557440,
                            "loanLimit": 300000000000,
                            "loanUsedAmount": 300000000000,
                            "unconfirmedBalance": 0,
                        },
                        {
                            "currency": {"code": "EOS"},
                            "balance": 82427080,
                            "availableBalance": 3966613,
                            "loanLimit": 154388200,
                            "loanUsedAmount": 100000000,
                            "unconfirmedBalance": 0,
                        },
                    ]
                }
            }
        }

        wallets: List[Wallet] = self.parser.parse_response(response=response)
        self.assertTrue(wallets is not None)
        self.assertTrue(len(wallets) == 2)


class TestBinanceTransactionResponseParser(unittest.TestCase):
    def setUp(self):
        self.parser = BinanceTransactionResponseParser()

    def test_get_transaction_response_valid(self):
        message = EntityMessage(
            id="44012152",
            market="PAXG/USDT",
            exchange="binance",
            order_type="b",
        )
        response = [
            {
                "symbol": "PAXGUSDT",
                "id": 3829254,
                "orderId": 44012152,
                "orderListId": -1,
                "price": "1819.76000000",
                "qty": "0.02000000",
                "quoteQty": "36.39520000",
                "commission": "0.03639520",
                "commissionAsset": "USDT",
                "time": 1627853461732,
                "isBuyer": False,
                "isMaker": False,
                "isBestMatch": True,
            }
        ]

        transactions = self.parser.parse_response(
            response=response, message=message)
        self.assertTrue(transactions is not None)


class TestBinanceWalletResponseParser(unittest.TestCase):
    def setUp(self):
        self.parser = BinanceWalletResponseParser()

    def test_get_wallet_response_valid(self):
        response = {
            "makerCommission": 10,
            "takerCommission": 10,
            "buyerCommission": 0,
            "sellerCommission": 0,
            "canTrade": True,
            "canWithdraw": True,
            "canDeposit": True,
            "updateTime": 1630259630891,
            "accountType": "SPOT",
            "balances": [
                {"asset": "BTC", "free": "0.04376896", "locked": "0.00000000"},
                {"asset": "LTC", "free": "0.27297000", "locked": "0.00000000"},
                {"asset": "ETH", "free": "0.27333116", "locked": "0.00000000"},
                {"asset": "NEO", "free": "0.84400000", "locked": "0.00000000"},
                {"asset": "BNB", "free": "0.40352640", "locked": "0.00000000"},
                {"asset": "QTUM", "free": "0.00000000", "locked": "0.00000000"},
                {"asset": "EOS", "free": "9.18000000", "locked": "0.00000000"},
                {"asset": "SNT", "free": "0.00000000", "locked": "0.00000000"},
                {"asset": "BNT", "free": "0.00000000", "locked": "0.00000000"},
                {"asset": "GAS", "free": "0.00000000", "locked": "0.00000000"},
                {"asset": "BCC", "free": "0.00000000", "locked": "0.00000000"},
                {"asset": "USDT", "free": "0.01443112", "locked": "0.00000000"},
                {"asset": "HSR", "free": "0.00000000", "locked": "0.00000000"},
                {"asset": "OAX", "free": "0.00000000", "locked": "0.00000000"},
            ],
            "permissions": ["SPOT"],
        }

        wallets: List[Wallet] = self.parser.parse_response(response=response)
        self.assertTrue(wallets is not None)
        self.assertTrue(len(wallets) == 1)
