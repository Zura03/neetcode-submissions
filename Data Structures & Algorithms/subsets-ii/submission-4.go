func subsetsWithDup(nums []int) [][]int {
    sort.Ints(nums)
    res := [][]int{}
    subres := []int{}

    var dfs func(i int)
    dfs = func(i int) {
        if i == len(nums){
            tmp := make([]int, len(subres))
            copy(tmp, subres)
            res = append(res, tmp)
            return
        }

        subres = append(subres, nums[i])
        dfs(i + 1)

        subres = subres[:len(subres) - 1]
        for i + 1 < len(nums) && nums[i] == nums[i+1] {
            i++
        }
        dfs(i + 1)
    }

    dfs(0)
    return res
}
