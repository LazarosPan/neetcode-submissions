class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Bottom-up DP: fill the same states from the last day backward.

        best_profit[day][0] = best profit from `day` onward while not holding.
        best_profit[day][1] = best profit from `day` onward while holding.
        Time O(n), space O(n).
        """
        total_days = len(prices)
        NOT_HOLDING, HOLDING = 0, 1
        best_profit = [[0, 0] for _ in range(total_days + 1)]  # row total_days is the base case (0)

        for day in range(total_days - 1, -1, -1):
            best_profit[day][NOT_HOLDING] = max(
                best_profit[day + 1][NOT_HOLDING],  # skip
                -prices[day] + best_profit[day + 1][HOLDING],  # buy
            )
            best_profit[day][HOLDING] = max(
                best_profit[day + 1][HOLDING],  # skip
                prices[day] + best_profit[day + 1][NOT_HOLDING],  # sell
            )

        return best_profit[0][NOT_HOLDING]  # start on day 0 without stock