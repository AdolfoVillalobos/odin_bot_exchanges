import unittest


from odin_bot_exchanges.binance import ExchangeInfo


class TestBuffer(unittest.TestCase):
    def setUp(self):
        self.exinfo = ExchangeInfo(
            min_notional=10.000, min_lot_size=0.1, precision=8, step_size=0.1)

    def test_filter_lot_size_success(self):
        quantity = 0.5
        self.assertTrue(self.exinfo.filter_lot_size(quantity))

    def test_filter_lot_size_failure(self):
        quantity = 0.05
        self.assertFalse(self.exinfo.filter_lot_size(quantity))

    def test_filter_min_notional_success(self):

        quantity = 3
        price = 3.7

        self.assertTrue(self.exinfo.filter_min_notional(
            quantity=quantity, price=price))

    def test_filter_min_notional_failure(self):

        quantity = 2
        price = 3.7

        self.assertFalse(self.exinfo.filter_min_notional(
            quantity=quantity, price=price))

    def test_get_amount(self):
        q1 = 10.1
        q2 = 10.12

        self.assertEqual(self.exinfo.get_amount(quantity=q1), 10.1)
        self.assertEqual(self.exinfo.get_amount(quantity=q2), 10.1)
