class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = maxa = 0
        l, r = 0, len(height)-1

        while l<r:
            area = min(height[l], height[r]) * (r-l)
            maxa = max(maxa, area)

            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1

        return maxa
