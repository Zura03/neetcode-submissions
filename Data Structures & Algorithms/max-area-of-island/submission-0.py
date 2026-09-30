class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # ROWS, COLS = len(grid), len(grid[0])
        # area = 0

        # def bfs(r, c):
        #     q = deque()
        #     grid[r][c] = 0
        #     q.append((r, c))
        #     res = 1

        #     while q:
        #         row, col = q.popleft()  
        #         for dr, dc in directions:
        #             nr, nc = dr + row, dc + col
        #             if (nr < 0 or nc < 0 or nr >= ROWS or
        #                 nc >= COLS or grid[nr][nc] == 0
        #             ):
        #                 continue
        #             q.append((nr, nc))
        #             grid[nr][nc] = 0
        #             res += 1
        #     return res

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 1:
        #             area = max(area, bfs(r, c))

        # return area

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        maxArea = 0

        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS) or
                grid[r][c] == 0 or (r, c) in visit):
                return 0
            
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1) 
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(dfs(r, c), maxArea)
        
        return maxArea