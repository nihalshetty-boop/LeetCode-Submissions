class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            ans = 0
            k = (l + r) // 2
            ans = sum([ceil(x/k) for x in piles])

            if ans <= h:
                r = k - 1
                res = k
                
            else:
                l = k + 1
            
        return res
