class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0

        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS) or
                (r, c) in visit or grid[r][c] == "0"):
                return 

            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

            # dfs(r + 1, c)
            # dfs(r - 1, c)
            # dfs(r, c + 1)
            # dfs(r, c -1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    print(r, c)
                    res += 1

        return res


