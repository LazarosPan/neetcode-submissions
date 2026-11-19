class StockSpanner:
    """Returns stock-price spans using a monotonic decreasing stack."""

    def __init__(self):
        # Each entry is (price, span) for a previous day.
        self.stack = []

    def next(self, price: int) -> int:
        """Return the number of consecutive days with price <= today's price."""
        current_span = 1

        # Merge all previous spans whose prices are <= today's price.
        while self.stack and self.stack[-1][0] <= price:
            _, previous_span = self.stack.pop()
            current_span += previous_span

        # Keep only useful prices: stack remains strictly decreasing.
        self.stack.append((price, current_span))

        return current_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)