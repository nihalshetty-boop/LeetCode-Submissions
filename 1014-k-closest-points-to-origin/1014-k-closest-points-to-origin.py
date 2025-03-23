class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for (x, y) in points:
            d = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (d, x, y))
            else:
                heapq.heappush(heap, (d, x, y))
        
        return [(x, y) for (d, x, y) in heap]
