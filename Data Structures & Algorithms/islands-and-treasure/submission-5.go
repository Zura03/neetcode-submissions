func islandsAndTreasure(grid [][]int) {
    rows, cols := len(grid), len(grid[0])
    q := [][]int{}

    for r := range rows{
        for c := range cols {
            if grid[r][c] == 0{
                q = append(q, []int{r, c})
            }
        }
    }

    dist := 0

    var addRoom func(r, c int)
    addRoom = func(r, c int){
        if r < 0 || r >= rows || c < 0 || c >= cols || 
            grid[r][c] != 2147483647 {
            return
        }
        grid[r][c] = dist + 1
        q = append(q, []int{r, c})
    }
    
    for len(q) > 0{
        for _ = range len(q){
            rowcol := q[0]
            q = q[1:]
            grid[rowcol[0]][rowcol[1]] = dist
            addRoom(rowcol[0] + 1, rowcol[1])
            addRoom(rowcol[0] - 1, rowcol[1])
            addRoom(rowcol[0], rowcol[1] + 1)
            addRoom(rowcol[0], rowcol[1] - 1)
        }
        dist++
    }
}
