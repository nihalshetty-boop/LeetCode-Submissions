class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        rows, cols= len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in dir:
                    r, c= row + dr,  col + dc
                    if r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == "1":
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands
            