class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        mins = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        def rot(r, c):
            nonlocal fresh
            if (r not in range(rows) or c not in range(cols) or
                grid[r][c] != 1):
                return

            fresh -= 1
            grid[r][c] = 2
            q.append((r, c))

        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                rot(row + 1, col)
                rot(row - 1, col)
                rot(row, col + 1)
                rot(row, col - 1)
            mins += 1

        return mins if fresh == 0 else -1
