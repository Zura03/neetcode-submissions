func subsets(nums []int) [][]int {
    res := [][]int{}
    subres := []int{}

    var dfs func(int)

    dfs = func(i int) {
        if i == len(nums) {
            temp := make([]int, len(subres))
            copy(temp, subres)
            res = append(res, temp)
            return
        }

        subres = append(subres, nums[i])
        dfs(i + 1)

        subres = subres[:len(subres) - 1]
        dfs(i + 1)
    }

    dfs(0)
    return res
}
