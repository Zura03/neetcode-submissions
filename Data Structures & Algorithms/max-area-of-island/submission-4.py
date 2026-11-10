class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        res = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            temp = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r not in range(rows) or c not in range(cols) or
                        grid[r][c] == 0 or (r, c) in visit):
                        continue
                    q.append((r, c))
                    visit.add((r, c))
                    temp += 1

            return temp

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    res = max(res, bfs(r, c))

        return res