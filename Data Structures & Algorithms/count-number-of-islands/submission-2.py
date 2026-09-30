class Solution:
    def numIslands(self, board: List[List[str]]) -> int:
        ROWS, COLS = len(board), len(board[0])

        visit = set()

        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS) or
                board[r][c] == "0"or (r, c) in visit):
                return

            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    res += 1
        return res

        