class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for  i in piles:
                hours += math.ceil(i/k)
            
            if hours <= h:
                ans = min(ans, k)
                r = k - 1
            else:
                l = k + 1
        return ans


