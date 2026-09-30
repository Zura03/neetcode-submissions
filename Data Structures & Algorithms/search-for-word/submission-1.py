class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        n = len(word)
        visit = set()

        def dfs(r, c, i):
            if i == n:
                return True
            if (r not in range(ROWS) or c not in range(COLS) or
                board[r][c] != word[i] or board[r][c] in visit):
                return False
            
            board[r][c] = '#'
            res = (dfs(r+1, c, i + 1) or dfs(r, c + 1, i + 1)
                    or dfs(r - 1, c, i + 1) or dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                res = dfs(r, c, 0)
                if res:
                    return True
        return False