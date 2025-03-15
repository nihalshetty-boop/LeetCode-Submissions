class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n1=sorted(nums)
        d1={}
        ans=[]
        
        for i,v in enumerate(n1):
            if v not in d1:
                d1[v]=i

        for v in nums:
            ans.append(d1[v])

        return ans 

        