class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n1 = set(nums)
        maxl = 0

        for n in n1:
            l = 0
            if (n-1) not in n1:
                while (n+l) in n1:
                    l += 1
                maxl = max(l, maxl)
        
        return maxl
        