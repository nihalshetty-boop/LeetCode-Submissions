class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def bt(start, end):
            if start == end:
                res.append(nums[:])
                return
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                bt(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
        
        res = []
        bt(0, len(nums))
        return res