class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s1=set(nums)
        a1=[]

        for i in range(1,len(nums)+1):
            if i not in s1:
                a1.append(i)

        return a1