class NumArray:

    def __init__(self, nums: List[int]):
        self.n2 = [0]
        
        for num in nums:
            self.n2.append(self.n2[-1] + num)
        

    def sumRange(self, left: int, right: int) -> int:
        return (self.n2[right + 1] - self.n2[left])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)