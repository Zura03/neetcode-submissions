func solve(board [][]byte) {
    rows, cols := len(board), len(board[0])
    visit := make(map[[2]int]bool)

    var dfs func(r, c int)
    dfs = func(r, c int) {
        coord := [2]int{r, c}
        if r < 0 || r >= rows || c < 0 || c >= cols || visit[coord] ||
            board[r][c] != 'O'{
            return
        }

        board[r][c] = 'T'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    }

    for r := range rows{
        dfs(r, 0)
        dfs(r, cols - 1)
    }

    for c := range cols {
        dfs(0, c)
        dfs(rows - 1, c)
    }

    for r := range rows {
        for c := range cols {
            if board[r][c] == 'O' {
                board[r][c] = 'X'
            }
        }
    }

    for r := range rows {
        for c := range cols {
            if board[r][c] == 'T' {
                board[r][c] = 'O'
            }
        }
    }
}
