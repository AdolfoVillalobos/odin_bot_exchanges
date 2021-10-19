class BinanceTransactionResponseParser(AbstractResponseParser):
    def parse_response(
        self, message: EntityMessage, response: dict
    ) -> List[Transaction]:
        try:
            currency_name, pair_currency_name = message.market.split("/")
            transaction_data = [
                {
                    "id": message.id,
                    "currency_name": currency_name,
                    "pair_currency_name": pair_currency_name,
                    "market": message.market,
                    "time": currency["time"],
                    "exchange": "binance",
                    "type": "b",
                    "fee": currency["commission"],
                    "currency_value": currency["qty"],
                    "pair_currency_value": float(currency["price"]),
                }
                for currency in response
            ]

            transactions = pydantic.parse_obj_as(
                List[Transaction], transaction_data)

            return transactions
        except Exception as err:
            logging.debug(err)
            raise ParserError("Binance Parser: Could not parse Transaction")


class BinanceWalletResponseParser(AbstractResponseParser):
    def parse_response(self, response: dict) -> List[Wallet]:
        try:
            wallet_data = {
                "exchange": "binance",
                "coins": {
                    currency["asset"]: {
                        "name": currency["asset"],
                        "amount": currency["free"],
                    }
                    for currency in response["balances"]
                    if currency["asset"] in currencies.BALANCE_COINS
                },
                "sign": -1.0,
                "time": time.time(),
                "date": datetime.now(),
            }

            wallet = [Wallet.parse_obj(wallet_data)]
            return wallet
        except Exception as err:
            logging.debug(err)
            raise ParserError("Binance Parser: Could not parse Wallet")
