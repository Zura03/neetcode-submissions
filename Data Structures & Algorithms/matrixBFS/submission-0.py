class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))

        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[0,1],[0,-1],[1,0],[-1,0]]

                for dr, dc in neighbors:
                    rr, cc = r + dr, c + dc
                    if (min(rr,cc) < 0 or rr == ROWS or cc == COLS or
                        (rr,cc) in visit or grid[rr][cc] == 1):
                        continue

                    queue.append((rr,cc))
                    visit.add((rr,cc))
            length += 1
        return -1