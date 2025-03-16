class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxp = 0

        while r != len(prices):
            
            if prices[l] < prices[r]:
                x = prices[r] - prices[l]
                maxp = max(maxp, x)
            else:
                l=r

            r+=1
        return maxp
