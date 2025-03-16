class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s1 = set()

        for i, num in enumerate(nums):
            if num in s1:
                return True
            s1.add(num)

            if len(s1)>k:
                s1.remove(nums[i-k])
        
        return False
            
        
        