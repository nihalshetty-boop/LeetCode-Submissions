class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        rect = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, ht = stack.pop()
                rect = max(rect, ht * (i - idx))
                start = idx
            stack.append((start, h))

        for i, h in stack:
            rect = max(rect, h * (len(heights) - i))
        
        return rect
                
            
            

