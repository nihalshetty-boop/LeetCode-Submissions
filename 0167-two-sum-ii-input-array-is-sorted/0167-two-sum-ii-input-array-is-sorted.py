class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm={}
        l, r = 0, len(numbers)-1

        for i,v in enumerate(numbers):
            if (numbers[l] + numbers[r] > target):
                r-=1
            elif (numbers[l] + numbers[r] < target):
                l+=1
            else:
                return l+1, r+1