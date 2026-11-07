class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        example 1:
        [1, 2, 3, 4, 5]
        [+1, +1, +1, +1]

        example 2:
        [7,1,5,3,6,4]
        [-6, +4, -2, +3, -2]
        """
        profit = 0

        for i in range(1, len(prices)):
            margin = prices[i] - prices[i-1]
            if margin > 0:
                profit += margin
                        
        return profit
