func twoSum(nums []int, target int) []int {
    difs := make(map[int]int)

    for i, n := range nums {
        var d int = target - n
        if j, found := difs[d]; found {
            return []int{j, i}
        }
        difs[n] = i
    }
    return []int{}
}
