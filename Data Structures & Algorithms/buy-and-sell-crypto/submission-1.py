class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Lowest buying price seen so far.
        # Start with the price on the first day.
        lowest_price = prices[0]

        # Best profit found so far.
        # It remains 0 if no profitable transaction exists.
        max_profit = 0

        # Consider each price as a possible selling price.
        for current_price in prices[1:]:
            # Profit if we sell today after buying
            # at the lowest earlier price.
            current_profit = current_price - lowest_price

            # Keep the highest profit found.
            max_profit = max(max_profit, current_profit)

            # Update the lowest buying price for future days.
            lowest_price = min(lowest_price, current_price)

        return max_profit