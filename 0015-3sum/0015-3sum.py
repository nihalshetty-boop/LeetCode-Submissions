class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = []
        nums.sort()

        for i, num in enumerate(nums):
            if (i!=0 and nums[i]==nums[i-1]):
                continue

            l, r = i+1, len(nums)-1

            while l<r:
                ts = num + nums[l] + nums[r]
                if (ts > 0):
                    r-=1
                elif (ts < 0):
                    l+=1
                else:
                    a.append([num, nums[l], nums[r]])
                    l+=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1 
        return a