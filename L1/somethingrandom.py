import time


class sexyTime:
    def __init__(self, price):
        super().__init__(price)
        self.data = {}

    def update(self, newPrice):
        orders = {}
        for ticker in self.data:
            curr = self.data[ticker]
            if newPrice[ticker] > curr:
                orders.add(ticker, "SELL")
            elif newPrice[ticker] < curr:
                orders.add(ticker, "BUY")

        return self.orders

    def dummy(self, dk):
        return {"APPL": "BUY"}
