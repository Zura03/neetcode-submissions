func findOrder(numCourses int, prerequisites [][]int) []int {
    preMap := make(map[int][]int)
    visit, cycle := make(map[int]bool), make(map[int]bool)
    res := []int{}

    for i := range numCourses {
        preMap[i] = []int{}
    }

    for _, cp := range prerequisites {
        c, p := cp[0], cp[1]
        preMap[c] = append(preMap[c], p)
    }

    var dfs func(x int) bool
    dfs = func(x int) bool {
        if cycle[x] {
            return false
        }
        if visit[x] {
            return true
        }

        cycle[x] = true
        for _, n := range preMap[x] {
            if !dfs(n) {
                return false
            }
        }
        cycle[x] = false
        visit[x] = true
        res = append(res, x)
        return true
    }

    for x := range numCourses {
        if !dfs(x) {
            return []int{}
        }
    }

    return res
}
