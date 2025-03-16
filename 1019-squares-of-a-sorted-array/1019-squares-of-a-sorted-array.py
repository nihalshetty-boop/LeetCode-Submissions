class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = collections.deque()
        l = 0
        r = len(nums) - 1

        while l<=r:
            left, right = abs(nums[l]), abs(nums[r])
            if left>right:
                ans.appendleft(left**2)
                l+=1

            else:
                ans.appendleft(right**2)
                r-=1
            
        return list(ans)
