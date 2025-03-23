class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        heap = []
        waitq = deque()
        t = 0

        for num in tasks:            #count = Counter(nums)
            if num in count:
                count[num] += 1
            else:
                count[num] = 1 

        for c in count.values():
            heap.append(-c)

        heapq.heapify(heap)

        while heap or waitq:
            t+=1

            if heap:
                curr = heapq.heappop(heap)
                curr += 1

                if curr != 0:
                    waitq.append((curr, t+n))

            if waitq and waitq[0][1] == t:
                heapq.heappush(heap, waitq.popleft()[0])  

        return t