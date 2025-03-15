import numpy as np

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans=0
        x1, y1 =points.pop()


        while points:
            x2, y2 =points.pop()
            ans+= max(abs(x2-x1),abs(y2-y1))
            x1, y1 = x2, y2
        
        return ans


        