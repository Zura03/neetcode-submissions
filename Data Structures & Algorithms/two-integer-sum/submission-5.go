func twoSum(nums []int, target int) []int {
    diffs := make(map[int]int)

    for i, num := range nums {
        if j, found := diffs[num]; found {
            return []int{j, i}
        }
        d := target - num
        diffs[d] = i
    }
    return []int{}
}
