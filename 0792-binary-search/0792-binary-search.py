class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2

        while l <= r:
            if nums[mid] < target:
                l = mid + 1
                mid = (l + r) // 2
            elif nums[mid] > target:
                r = mid - 1 
                mid = (l + r) // 2
            else:
                return mid
        return -1


