class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Tabulation keeping only the current day's two states.

        Each day depends only on the previous day, so two variables suffice.
        Time O(n), space O(1).
        """
        cash_without_stock = 0  # best profit so far, not holding
        cash_with_stock = float("-inf")  # best profit so far, holding (impossible before buying)

        for price_today in prices:
            previous_cash_without_stock = cash_without_stock  # needed by the buy transition
            cash_without_stock = max(
                cash_without_stock,  # stay out of the market
                cash_with_stock + price_today,  # sell today
            )
            cash_with_stock = max(
                cash_with_stock,  # keep holding
                previous_cash_without_stock - price_today,  # buy today
            )

        return cash_without_stock  # ending without stock is always at least as good