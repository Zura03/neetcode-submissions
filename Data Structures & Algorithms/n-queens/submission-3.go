func solveNQueens(n int) [][]string {
	col := make(map[int]bool)
    posDiag := make(map[int]bool)
    negDiag := make(map[int]bool)

    res := [][]string{}
    board := make([][]rune, n)
    for i := range board {
        board[i] = make([]rune, n)
        for j := range board[i] {
            board[i][j] = '.'
        }
    }

    var dfs func(r int)
    dfs = func(r int) {
        if r == n {
            sol := make([]string, n)
            for i := range board {
                sol[i] = string(board[i])
            }
            res = append(res, sol)
            return
        }

        for c := 0; c < n; c++ {
            if col[c] || posDiag[r+c] || negDiag[r-c] {
                continue
            }

            col[c] = true
            posDiag[r+c] = true
            negDiag[r-c] = true
            board[r][c] = 'Q'

            dfs(r+1)

            col[c] = false
            posDiag[r+c] = false
            negDiag[r-c] = false
            board[r][c] = '.'
        }
    }

    dfs(0)
    return res
}
