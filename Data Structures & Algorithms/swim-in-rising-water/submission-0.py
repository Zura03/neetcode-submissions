class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visit = set()
        q = [[grid[0][0], [0, 0]]] #time, [x, y]
        visit.add((0, 0))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            t, [x1, y1] = heapq.heappop(q)
            if x1 == ROWS - 1 and y1 == COLS - 1:
                return t

            for dr, dc in directions:
                row, col = x1 + dr, y1 + dc
                if (row not in range(ROWS) or col not in range(COLS) or
                    (row, col) in visit):
                    continue
                visit.add((row, col))
                heapq.heappush(q, [max(t, grid[row][col]), [row, col]])
        