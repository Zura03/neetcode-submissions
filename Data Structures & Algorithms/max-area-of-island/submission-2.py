class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            nonlocal res
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            area = 0
            while q:
                row, col = q.popleft()
                area += 1
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr not in range(ROWS) or
                        nc not in range(COLS) or
                        grid[nr][nc] == 0):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
            res = max(res, area)

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    bfs(r, c)
        return res