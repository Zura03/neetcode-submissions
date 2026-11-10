func maxAreaOfIsland(grid [][]int) int {
    rows, cols := len(grid), len(grid[0])
    res := 0
    directions := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

    var bfs func(r, c int) int
    bfs = func(r, c int) int {
        q := [][]int{{r, c}}
        grid[r][c] = 0
        temp := 1

        for len(q) > 0 {
            first := q[0]
            q = q[1:]

            for _, direction := range directions {
                dr, dc := first[0] + direction[0], first[1] + direction[1]
                if dr < 0 || dr == rows || dc < 0 || dc == cols || 
                    grid[dr][dc] == 0 {
                        continue
                }
                grid[dr][dc] = 0
                q = append(q, []int{dr, dc})
                temp++
            }
        }

        return temp
    }

    for r := range rows{
        for c := range cols {
            if grid[r][c] == 1 {
                res = max(res, bfs(r, c))
            }
        }
    }
    
    return res
}
