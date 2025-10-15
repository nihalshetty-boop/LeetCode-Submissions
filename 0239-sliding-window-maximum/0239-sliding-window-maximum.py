class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        l = r = 0
        op = []

        while r < len(nums):

            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            if l > dq[0]:
                dq.popleft()
            
            if r + 1 >= k:
                op.append(nums[dq[0]])
                l+=1
            r+=1

        return op
