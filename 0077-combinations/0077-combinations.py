class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def bt(start, path):
            if len(path)==k:
                res.append(path[:])
                return

            for i in range(start, n+1):
                path.append(i)
                bt(i+1, path)
                path.pop()
        
        res = []
        bt(1, [])
        return res