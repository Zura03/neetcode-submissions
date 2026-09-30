class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            res = 1
            grid[r][c] = 0

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr not in range(ROWS) or nc not in range(COLS)
                        or grid[nr][nc] == 0):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(bfs(r, c), maxArea)
        
        return maxArea
        # ROWS, COLS = len(grid), len(grid[0])
        # visit = set()
        # maxArea = 0

        # def dfs(r, c):
        #     if (r not in range(ROWS) or c not in range(COLS) or
        #         grid[r][c] == 0 or (r, c) in visit):
        #         return 0
            
        #     visit.add((r, c))
        #     return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1) 
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 1 and (r, c) not in visit:
        #             maxArea = max(dfs(r, c), maxArea)
        
        # return maxArea