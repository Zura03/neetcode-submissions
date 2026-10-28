func combinationSum(nums []int, target int) [][]int {
    res := [][]int{}
    subres := []int{}

    var dfs func(i, total int)

    dfs = func(i, total int) {
        if i == len(nums) || total > target {
            return
        }

        if total == target{
            temp := make([]int, len(subres))
            copy(temp, subres)
            res = append(res, temp)
            return
        }

        subres = append(subres, nums[i])
        dfs(i, total + nums[i])

        subres = subres[:len(subres) - 1]
        dfs(i + 1, total)
    }

    dfs(0, 0)
    return res
}
