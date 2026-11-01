func combinationSum2(candidates []int, target int) [][]int {
    res := [][]int{}
    subres := []int{}
    sort.Ints(candidates)

    var dfs func(i, curSum int)
    dfs = func(i, curSum int) {
        if curSum == target {
            tmp := make([]int, len(subres))
            copy(tmp, subres)
            res = append(res, tmp)
            return
        }

        if i >= len(candidates) || curSum > target {
            return
        }

        subres = append(subres, candidates[i])
        dfs(i + 1, curSum + candidates[i])

        subres = subres[:len(subres) - 1]
        for i + 1 < len(candidates) && candidates[i] == candidates[i+1] {
            i++
        }
        dfs(i + 1, curSum)
    }

    dfs(0,0)
    return res
}
