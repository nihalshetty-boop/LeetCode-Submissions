class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxl = maxr = 0
        watersum = 0

        while l<r:
            if height[l] < height[r]:
                if maxl < height[l]:
                    maxl = height[l]
                else:
                    watersum += maxl - height[l]
                l+=1
            else:
                if maxr < height[r]:
                    maxr = height[r]
                else:
                    watersum += maxr - height[r]
                r-=1
        
        return watersum


