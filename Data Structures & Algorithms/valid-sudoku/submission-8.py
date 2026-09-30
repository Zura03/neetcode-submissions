class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            visited1=set()
            visited2=set()
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in visited1:
                        return False
                    visited1.add(board[i][j])
                if board[j][i]!='.':
                    if board[j][i] in visited2:
                        return False
                    visited2.add(board[j][i])
        # trios=[[0,3],[0,6],[0,0],[3,3],[3,6],[3,0],[6,0],[6,3],[6,6]]
        for rows in range(0,9,3):
            for columns in range(0,9,3):
                visited=set()
                for i in range(rows,rows+3):
                    for j in range(columns,columns+3):
                        if board[i][j]!='.':
                            if board[i][j] in visited:
                                return False
                            visited.add(board[i][j])
        # for i,j in trios:
        #     visited=set()
        #     for a in range(i,i+3):
        #         for b in range(j,j+3):
        #             if board[a][b]!='.':
        #                 if board[a][b] in visited:
        #                     return False
        #                 visited.add(board[a][b])
        return True