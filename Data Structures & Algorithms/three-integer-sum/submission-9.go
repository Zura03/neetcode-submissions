func threeSum(nums []int) [][]int {
    res := [][]int{}
    sort.Ints(nums)

    for i, a := range nums{
        if a > 0{
            break
        }

        if i > 0 && a == nums[i-1]{
            continue
        }

        l, r := i + 1, len(nums) - 1
        for l < r {
            s := a + nums[l] + nums[r]
            if s < 0{
                l++
            } else if s > 0{
                r--
            } else {
                res = append(res, []int{a, nums[l], nums[r]})
                l++
                r--
                for l < r && nums[l] == nums[l-1]{
                    l++
                }
            }
        }
    }
    return res
}
