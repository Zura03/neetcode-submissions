class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh, rotten = 0, 0
        q = deque()
        #visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        def rot(r, c):
            nonlocal fresh
            if (r not in range(ROWS) or c not in range(COLS) or
                grid[r][c] != 1):
                return

            if grid[r][c] == 1:
                grid[r][c] = 2
                q.append([r, c])
                fresh -= 1


        time = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                #fresh -= 1 shouldnt be here cus it decrements for every rotten fruit including the ones which were initially rotten.
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)
            time += 1
        
        return time if fresh == 0 else -1
