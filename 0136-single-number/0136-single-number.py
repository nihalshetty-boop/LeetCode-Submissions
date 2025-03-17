class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bwor = 0
        for i in nums:
            bwor ^= i
        
        return bwor