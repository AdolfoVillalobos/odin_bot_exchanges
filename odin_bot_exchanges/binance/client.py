import logging
import aiohttp


from binance.spot import Spot
from dataclasses import dataclass


logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)s:%(asctime)s:%(message)s")


@dataclass
class BinanceClient:
    api_key: str
    secret_key: str

    def __post_init__(self):
        self.client = Spot(
            key=self.api_key, secret=self.secret_key
        )

    def get_order_response(
        self, order_id: str, market_code: str
    ):
        response = self.client.get_order(
            symbol=market_code, orderId=order_id
        )
        return response

    def get_transaction_response(self, order_id: str, market_code: str):
        try:
            response = self.client.my_trades(
                symbol=market_code, orderId=int(order_id)
            )
            logging.info(response)
            return response
        except Exception as err:
            logging.debug(err)
            raise err

    def get_wallet_response(self):
        response = self.client.account()
        return response