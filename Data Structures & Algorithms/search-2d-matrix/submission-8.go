func searchMatrix(matrix [][]int, target int) bool {
    rows, cols := len(matrix), len(matrix[0])
    top, bottom :=  0, rows - 1

    for top <= bottom {
        m := (top + bottom) / 2
        if target > matrix[m][cols - 1] {
            top = m + 1
        } else if target < matrix[m][0] {
            bottom = m - 1
        } else {
            break
        }
    }
    
    if !(top <= bottom) {
        return false
    } 

    row := (top + bottom) / 2
    l , r := 0, cols - 1
    for l <= r {
        m := (l + r) / 2
        if target > matrix[row][m] {
            l = m + 1
        } else if target < matrix[row][m] {
            r = m - 1
        } else {
            return true
        }
    }
    return false
}
