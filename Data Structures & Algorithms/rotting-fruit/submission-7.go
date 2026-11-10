func orangesRotting(grid [][]int) int {
    rows, cols := len(grid), len(grid[0])
    fresh, mins := 0, 0
    q := [][]int{}

    var rot func(r, c int)
    rot = func(r, c int) {
        if r < 0 || r == rows || c < 0 || c == cols || grid[r][c] != 1{
            return
        } 

        fresh--
        grid[r][c] = 2
        q = append(q, []int{r, c})
    }
    
    for r := range rows {
        for c := range cols {
            if grid[r][c] == 1{
                fresh++
            } else if grid[r][c] == 2{
                q = append(q, []int{r, c})
            }
        }
    }

    for len(q) > 0 && fresh > 0 {
        for _ = range len(q) {
            popped := q[0]
            q = q[1:]
            row, col := popped[0], popped[1]
            rot(row + 1, col)
            rot(row - 1, col)
            rot(row, col + 1)
            rot(row, col - 1)
        }
        mins++
    }

    if fresh == 0{
        return mins
    } else {
        return -1
    }
}
