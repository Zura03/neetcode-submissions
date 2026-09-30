class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 0
        maxprofit = 0

        while R < len(prices):
            if prices[R] <= prices[L]:
                L = R
            maxprofit = max(maxprofit, prices[R] - prices[L])
            R += 1
        
        return maxprofit