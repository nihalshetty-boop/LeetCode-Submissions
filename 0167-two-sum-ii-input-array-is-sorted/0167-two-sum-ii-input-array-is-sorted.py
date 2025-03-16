class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm={}

        for i,v in enumerate(numbers):
            if target-v in hm:
                return hm[target-v]+1, i+1
            else:
                hm[v]=i