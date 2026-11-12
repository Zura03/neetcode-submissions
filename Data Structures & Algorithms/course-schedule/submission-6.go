func canFinish(numCourses int, prerequisites [][]int) bool {
    preMap := make(map[int][]int, numCourses)
    for _, cp := range prerequisites {
        c, p := cp[0], cp[1]
        preMap[c] = append(preMap[c], p)
    }

    visit := make(map[int]bool)

    var dfs func(x int) bool
    dfs = func(x int) bool {
        if visit[x] {
            return false
        }
        if len(preMap[x]) == 0{
            return true
        }

        visit[x] = true
        for _, pre := range preMap[x]{
            if !dfs(pre){
                return false
            }
        }
        visit[x] = false
        preMap[x] = []int{}
        return true
    }

    for x := range numCourses {
        if !dfs(x){
            return false
        }
    }
    return true
}
