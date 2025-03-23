class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
         
        for num in nums:            #count = Counter(nums)
            if num in count:
                count[num] += 1
            else:
                count[num] = 1 

        for num, freq in count.items():
            if len(heap) < k: 
                heapq.heappush(heap, (freq, num))
            elif freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, num))
        
        topk = [num for freq, num in heap]
        return topk