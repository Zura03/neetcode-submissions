class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minH = [[grid[0][0], 0, 0]]
        visit = set()
        res = 0
        while True:
            t, r, c = heapq.heappop(minH)
            res = max(res, t)
            if r == ROWS - 1 and c == COLS - 1:
                return res
            visit.add((r, c))
            for dr, dc in directions:
                rr, cc = r + dr, c + dc
                if (rr not in range(ROWS) or cc not in range(COLS)
                    or (rr, cc) in visit):
                    continue
                heapq.heappush(minH, [grid[rr][cc], rr, cc])