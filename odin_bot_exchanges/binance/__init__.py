class BinanceExchange(ExchangeService):
    exchange: str = "binance"

    def __init__(self, credentials: Settings):
        self.client: AbstractClient = BinanceClient(credentials=credentials)
        self.wallet_parser: AbstractResponseParser = BinanceWalletResponseParser()
        self.transaction_parser: AbstractResponseParser = (
            BinanceTransactionResponseParser()
        )

    async def get_order_response(
        self, message: EntityMessage, session: aiohttp.ClientSession
    ) -> Order:
        response = self.client.get_order_response(
            message=message, session=session)
        order: Order = self.order_parser.parse_response(response=response)
        return order

    async def get_transaction_response(
        self, message: EntityMessage, session: aiohttp.ClientSession
    ) -> Transaction:
        response = self.client.get_transaction_response(message=message)
        transaction = self.transaction_parser.parse_response(
            response=response, message=message
        )
        return transaction

    async def get_wallet_response(self, session: aiohttp.ClientSession) -> List[Wallet]:
        response = self.client.get_wallet_response()
        wallets = self.wallet_parser.parse_response(response=response)
        return wallets

    async def get_ticker_price_response(self):
        return await super().get_ticker_price_response()
